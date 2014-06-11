<!-- 
.. link: 
.. description: 
.. tags: GPU, simulations, N-body
.. date: 2013/08/20 09:34:11
.. title: StarLab (GPU) guide
.. slug: starlab-gpu-guide
-->

Well, probably you landed here searching information about StarLab, how to 
install it, how to run it, how prevent it to harm your cat.

**DISCLAIMER 1:** I won't promise anything about your cat but I will try to help you having a 
reasonable well running installation of StarLab.

**DISCLAIMER 2:** I'm not a programmer, I'm not a system administrator and I don't even 
know how to program in CUDA (yet). Maybe something here is wrong ore outdated. 
I'm only giving you some of the experienced I collected in $n+1$ times I installed StarLab. 
Nothin less, nothing more.    
Also note that most of the knowledge I put here come 
from my [supervisor](http://web.pd.astro.it/mapelli/).

## StarLab

[StarLab](http://www.sns.ias.edu/~starlab/) is "A Software Environment for Collisional Stellar Dynamics".
[Here](http://www.sns.ias.edu/~starlab/) you can find useful information about it that 
is not useful to rewrite here, so have a look and then come back!:)

## StarLab-GPU

Welcome back!!    
Next step: StarLab was designed to run on [GRAPE](http://en.wikipedia.org/wiki/Gravity_Pipe) 
but thanks to the [Sapporo](http://castle.strw.leidenuniv.nl/software/sapporo.html) 
library you can run it on GPUs.    

Now we will try to install a GPU-ready version of StarLab. To be honest, we run 
a **private** version of StarLab for GPU with some customizations (if you are interested, 
see [Mapelli et al. 2013](); [Mapelli & Bressan 2013]()).    
Unfortunately you can't download it now, but I hope the differences in the installation 
process are negligible. Otherwise ask us for our StarLab version.    
Because I'm not sure about what you will find in the public version os Sapporo and StarLab, 
I will show my version of the relevant files you need to install everything. 
The installation is done on a Ubuntu 14.04 workstation so change them accordingly to 
your OS. I will also provide some examples on what you need to install StarLab on 
the clusters I tested.    

Let's start!!

#### Download

Be sure you have boost libraries, nVidia driver and CUDA correctly installed. 
You can try to check them using 

* `locate cuda | grep nvcc` (cuda compiler)
* `locate cuda | grep include`
* `locate cuda | grep include | grep toolkit` (for the SDK files of the new release)
* `locate cuda | grep lib | grep cudart` (CUDA runtime)
* `locate cuda | grep lib`
* `locate cuda | grep include`

It could be also useful to have a copy of the old CUDA SDK. Yes, I know, it's a mess, 
but it's not my fault!:P

Download 

* [StarLab](http://www.sns.ias.edu/~starlab/download/starlab.tar.gz)
* [Sapporo](http://castle.strw.leidenuniv.nl/documents/Sapporo/sapporo161.tgz)

and decompress the archives with `tar -xvf archiveName`.    
Try to have the following folder tree:    

* `$SLPATH/slpack`
* `$SLPATH/slpack/NVIDIA`
* `$SLPATH/slpack/NVIDIA/NVIDIA_CUDA-5.0_Samples`
* `$SLPATH/slpack/NVIDIA/NVIDIA_GPU_Computing_SDK`
* `$SLPATH/slpack/sapporo`
* `$SLPATH/slpack/starlab`

The NVIDIA folder is optional, but I would sugest to have with you alle the NVIDIA 
file you can find, soon or later you will need them. CUDA is continuosly changing, 
SDK is not toolkit, dependencies are different and broken between different versions.
We will try to survive and to have the most standard installation we can.    

`$SLPATH` should be the path where you put your StarLab installation.     
I'm not sure about what you will find in the public version of StarLab and Sapporo.

### Sapporo

Enter in the sapporo folder, and to be sure to start a clean installation run 
`make clean`. 
Here you need to find:

* `Makefile`
* `compile.sh`
* `host_evaluate_gravity.cu`

`compile.sh` is the script StarLab will run later to decide if you are worthy of 
its presence in your computer. If `compile.sh` fail, StarLab won't install.    

You also need to find somewhere (= in an old CUDA SKD?) 

* `cutil.h`
* `multithreading.h`

and to copy them in this folder.    

Open `host_evaluate_gravity.cu` and change 

````C
#include <cutil.h>
#include <multithreading.h>
````
to 

````C
#include "cutil.h"
#include "multithreading.h"
````
Now open `Makefile` and fit 

````Makefile
CXX  := g++
CC   := gcc
NVCC := /usr/bin/nvcc
CUDAPATH    := /usr/include/
CUDAINCLUDE := -I$(CUDAPATH) 
BOOSTPATH := /usr/include/boost 
BOOSTINCLUDE := -I$(BOOSTPATH)
````
to your case.    
Open `compile.sh` and be sure to have something like this:

````bash
#!/bin/sh

flags=-DNGB

CUDAINC="-I/usr/include -I/usr/lib/nvidia-cuda-toolkit/include/"
CUDALIB="-L/usr/lib/x86_64-linux-gnu/"
CUDAFLAG='-lcudart'
BOOSTINC='-I/usr/include/boost'
BOOSTLIB='-L/usr/lib/x86_64-linux-gnu/'
BOOSTFLAG='-lboost_system -lboost_thread -lpthread'


g++ -O3 $flags -g -o test_gravity_block test_gravity_block.cpp -L. -lsapporo $CUDAINC $CUDALIB $CUDAFLAG $BOOSTINC $BOOSTLIB $BOOSTFLAG
g++ -O3 $flags -g -o test_gravity_N2ngb test_gravity_N2ngb.cpp -L. -lsapporo $CUDAINC $CUDALIB $CUDAFLAG $BOOSTINC $BOOSTLIB $BOOSTFLAG
````
Try to compile with `make`. If it works, try to tun `bash compile.sh`. If this works too, 
then test sapporo with 

* `./test_gravity_block 800`
* `./test_gravity_block 800`

Be aware that a number (of particles) too small would crash the tests.

Assuming `sapporo` is ready, let's move to starlab.

### StarLab

In StarLab the relevant files you have to worry about are 

* `sbin/sqrt.c`
* `configure`
* `local/grape.sh`

Rename `sbin/sqrt.c` to `sbin/sqrt.C` otherwise 
you could have linker problems again the C math library.    
Now open `configure` and search for CUDA. Probably you won't find anything.     
Search for ` Check all named libraries for g6_open`, you should find something like 

````bash
#   Check all named libraries for g6_open() (GRAPE-6).

    grape6=no

    for gl in $GRAPE_LIBS_; do
        as_ac_Lib=`echo "ac_cv_lib_${gl/-l/}''_g6_open_" | $as_tr_sh`
echo "$as_me:$LINENO: checking for g6_open_ in -l${gl/-l/}" >&5
````

modify it to include boost and CUDA like:

````bash
for gl in $GRAPE_LIBS_; do
	CUDAINC="-I/usr/include -I/usr/lib/nvidia-cuda-toolkit/include/"
	CUDALIB="-L/usr/lib/x86_64-linux-gnu/"
	CUDAFLAG='-lcudart'
	BOOSTINC='-I/usr/include/boost'
	BOOSTLIB='-L/usr/lib/x86_64-linux-gnu/'
	BOOSTFLAG='-lboost_system -lboost_thread -lpthread'
	
	LIBS="$CUDAINC $CUDALIB $CUDAFLAG $BOOSTLIB $BOOSTFLAG -DNGB"
		
	as_ac_Lib=`echo "ac_cv_lib_${gl/-l/}''_g6_open_" | $as_tr_sh`
````

Last edit is on `local/grape.sh` to let StarLab know where your sapporo installation is:

````bash
GRAPE_LDFLAGS_='-L$SLPATH/slpack/sapporo'
GRAPE_LIBS_='-lsapporo'
# For now, define this as `yes' for the AMD64 boxes only, `no' otherwise.
OLD_READ_NEIGHBOUR_LIST=no
````

Before compiling, if you want, you can check also `sapporo/sapporo.config`.    
Inside you will find something like that:

````bash
524288
-1
0
1
````
where 524288 should be the maximum number of particles you can handle, -1 the number 
of CUDA devices to use (-1 means all? maybe...), 0 and 1 are the GPU number you want to use.     
Recent CUDA seems to be smart enought to understand where to run without having to specify 
(but look after your cat!!!).    

Alright!! If you managed to reach this point, very good. Last three commands. In the 
`starlab` folder run 

* `configure --without-f77`
* `make`

go out for a walk

* `make install`

If you recompile StarLab AND/OR Sapporo, type `make clean` 2 times. delete the files in 
`starlab/usr/bin`, turn around 3 times, touch your nose and type `make` two times. Then 
`make install` again.     
No, `make clean` and `make` are not enought to update your object 
files or binaries.

### Run StarLab

Before run a simulation you need to create the initial conditions.

#### Initial Conditions

StarLab if provided with few tools to help (really?) you in this task. A common 
way to create ICs for [our simulations](http://arxiv.org/abs/1404.7147) is something like:     

`<ehm, I don't know if I can tell you, sorry man...:(>`


#### Launch

StarLab read ICs from the STDIN, write the output snapshots to STDOUT and everything 
you want to know about your simulations to STDERR, so, `<ehm.... see ICs>`


#### Tidal fields



### Known issues and Troubleshooting

If StarLab did not kill your cat in a horrile way, then , it can still ruin your life.    
Some of the things that can happen are:

* you can find binaries with eccentricity greater than one (StarLab does 
not update some binaries after they are disrupted? flybyes seen as binaries? don't know)
* StarLab can crash if you try to simulate a number of centers of mass greater than 
$5*10^4$ together with a fraction of primordial binaries $\geq0.1$
* boost problems? check the correct flags for your version (choose among some combination of 
`-lboost_system, -lboost_system-mt, -lboost_thread, -lpthread`)
* check you put all the `_`, "-I", "-l", "-L" in the right places
* check all the libraries paths

### Clusters 

`<can I....?>`


### Additional material

* Code units
* StarLab internals
* Our repo
* [StarLab tools wiki](http://www.science.uva.nl/sites/modesta/wiki/index.php/Starlab_tools)














