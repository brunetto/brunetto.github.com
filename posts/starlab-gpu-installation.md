<!-- 
.. link: 
.. description: 
.. tags: GPU, simulations, N-body
.. date: 2013/08/20 09:34:11
.. title: StarLab-GPU installation
.. slug: starlab-gpu-installation
-->

* [Click here for the old guide!!!](../stories/research/utils/starlab-gpu-old-guide.html)    
* 2014/09/16: updated with installation instruction for g2@Swinburne and some troubleshooting.

---    

**UPDATE:** if you want to compile starlab **without GPU support**, you only need to     

* ignore the "`sapporo`"  and "`CUDA`" instructions
* rename `starlab/local/grape.sh` to `starlab/local/_grape.sh` 
* substitute `configure --without-f77` with `configure --with-grape=no --without-f77`)
* in case you can't `make` succesfully may be you need to copy the folder 
`starlab/src/gfx` and do not make clean

---

Well, probably you landed here searching information about StarLab, how to 
install it, how to run it, how prevent it to harm your cat.

**DISCLAIMER 1:** I won't promise anything about your cat but I will try to help you having a 
reasonable well running installation of StarLab.

**DISCLAIMER 2:** I'm not a programmer, I'm not a system administrator and I don't even 
know how to program in CUDA (yet). Maybe something here is wrong ore outdated. 
I'm only giving you some of the experienced I collected in n+1 times I installed StarLab. 
Nothin less, nothing more.    
Also note that most of the knowledge I put here come 
from my [supervisor](http://web.pd.astro.it/mapelli/).    
I also thanks Mario Spera for the usefull advices.

**DISCLAIMER 3:** StarLab still seems to **always** crash if you try to simulate a system 
with more than ~6000 binaries.

## StarLab

[StarLab](http://www.sns.ias.edu/~starlab/) is "A Software Environment for Collisional Stellar Dynamics".
[Here](http://www.sns.ias.edu/~starlab/) you can find useful information about it that 
is not useful to rewrite here, so have a look and then come back!:)

<!-- TEASER_END -->

## StarLab-GPU

Welcome back!!    
Next step: StarLab was designed to run on [GRAPE](http://en.wikipedia.org/wiki/Gravity_Pipe) 
but thanks to the [Sapporo](http://castle.strw.leidenuniv.nl/software/sapporo.html) 
library you can run it on GPUs.    

Now we will try to install a GPU-ready version of StarLab. To be honest, we run 
a **private** version of StarLab for GPU with some customizations (if you are interested, 
see [Mapelli et al. 2013](http://arxiv.org/abs/1211.6441); [Mapelli & Bressan 2013](http://arxiv.org/abs/1301.4227)).    
Unfortunately you can't download it now, but I hope the differences in the installation 
process are negligible. Ask us if you are interested in our version of StarLab.    
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
* `locate cuda | boost lib`
* `locate cuda | boost include`

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

The NVIDIA folder is optional, but I would suggest to have with you alle the NVIDIA 
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
If you are not able to find them, ask me, I have copies of those files.    

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
This is to make Sapporo read the local version of `cutil.h` and `multithreading.h` 
in case your CUDA version does not support them anymore.     

It's time to fix a bug (thanks Mario):
in `sapporo.cpp` change    

````c++
		fprintf(stderr, "\n");
		nCUDAdevices = how_many;
    } else {
		fprintf(stderr," sapporo::open - no config file is found \n");
		fprintf(stderr,"  using all %d CUDA device(s), nj_max= %d\n", nCUDAdevices, nj_max);
		//Set original_how_many to a positive number so we get assigned different devices
		//incase the devices are not in compute exclusive mode.
		original_how_many = 1;
  }
````

to    

````c++
		fprintf(stderr, "\n");
		nCUDAdevices = how_many;
		fclose(fd); // thanks Mario Spera, without this SL will crash after a while if using sapporo.config
  } else {
    fprintf(stderr," sapporo::open - no config file is found \n");
    fprintf(stderr,"  using all %d CUDA device(s), nj_max= %d\n", nCUDAdevices, nj_max);
    //Set original_how_many to a positive number so we get assigned different devices
    //incase the devices are not in compute exclusive mode.
    original_how_many = 1;
    }
````
so the `sapporo.config` file can be close and won't crash your run.    

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
CUDAFLAG="-lcudart"
BOOSTINC="-I/usr/include/boost"
BOOSTLIB="-L/usr/lib/x86_64-linux-gnu/"
BOOSTFLAG="-lboost_system -lboost_thread -lpthread"


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
	CUDAFLAG="-lcudart"
	BOOSTINC="-I/usr/include/boost/"
	BOOSTLIB="-L/usr/lib/x86_64-linux-gnu/"
	BOOSTFLAG="-lboost_system -lboost_thread -lpthread"
	
	LIBS="$CUDAINC $CUDALIB $CUDAFLAG $BOOSTINC $BOOSTLIB $BOOSTFLAG -DNGB"
		
	as_ac_Lib=`echo "ac_cv_lib_${gl/-l/}''_g6_open_" | $as_tr_sh`
````

Be sure to always use double quotes and to terminate the paths to folders with a slash (`/`), 
some machines are quite choosy.

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

* `configure --with-f77=no`
* `make`

go out for a walk

* `make install`

When running configure, avoid the `--without-option` version of an option, prefer 
`--with-option=no`, it's safer.

If you recompile StarLab AND/OR Sapporo, type `make clean` two times. delete the files in 
`starlab/usr/bin`, turn around 3 times, touch your nose and type `make` two times. Then 
`make install` again.     
No, `make clean` and `make` are not enought to update your object 
files or binaries.    

Depending on your environment, if you run into problems, be sure that:

* you loaded the correct modules (if you are in a cluster for examples
* you are into the right node (some machine let you compile your code on a 
node that is not the login node)
* if you encounter strange messages regarding missing rules for missing files, 
for example `libxhdyn.la` or something regarding `gfx`-something, may be tou need to 
tune your config file to exclude, for example, the X/Qt/... libraries, in case 
try to run `configure --with-f77=no --with-qt=no`; in case try to have a look at 
`configure --help`

### Run StarLab

Before run a simulation you need to create the initial conditions.

#### Initial Conditions

StarLab is provided with few tools to help (really?) you in this task. A common 
way to create ICs for [our simulations](http://arxiv.org/abs/1404.7147) is something like:     

`<ehm, I don't know if I can tell you, sorry man...:(>`


#### Launch

StarLab read ICs from the STDIN, write the output snapshots to STDOUT and everything 
you want to know about your simulations to STDERR, so, `<ehm.... see ICs>`


#### Tidal fields

Be patience...

### Known issues and Troubleshooting

If StarLab did not kill your cat in a horrile way, then, it can still ruin your life.    
Some of the things that can happen are:

* you can find binaries with eccentricity greater than one (StarLab does 
not update some binaries after they are disrupted? flybyes seen as binaries? don't know)
* StarLab can crash if you try to simulate a number of centers of mass greater than 
5*10^4 together with a fraction of primordial binaries >=0.1
* boost problems? check the correct flags for your version (choose among some combination of 
`-lboost_system, -lboost_system-mt, -lboost_thread, -lpthread`)
* check you put all the `_`, "-I", "-l", "-L" in the right places
* check all the libraries paths
* check for double quotes (`"`) instead of single ones (`'`) in the paths
* check the modules, environment variables
* check you are on the right node
* check your environment against the configure options you passed 
(have a look at `configure --help`)
* if you need to modify StarLab and you want to add your own flags, 
you need to comment 

````c++
  getia(b->get_log_story(), "step_slow",
        b->get_kira_counters()->step_slow, nss);
````

function call in `kira_counters.C` otherwise you won't be able to compile StarLab.    


### Clusters 

#### EURORA

* in `setup_sapporo.sh`
(if you want to compile sapporo using queues, or, load modules by hand if you want to 
compile interactively)

````bash
module purge
module load profile/advanced
module load gnu/4.6.3
module load boost/1.53.0--gnu--4.6.3
module load cuda

LD_LIBRARY_PATH=/cineca/prod/compilers/cuda/5.0.35/none/lib64:/cineca/prod/libraries/boost/1.53.0/gnu--4.6.3/lib
export LD_LIBRARY_PATH
cd $HOME/slPack/sapporo
````

* in `compile.sh`

````bash
CUDAINC="-I/cineca/prod/compilers/cuda/5.0.35/none/include/ -I/cineca/prod/compilers/cuda/5.0.35/none/samples/common/inc/ -I/cineca/prod/libraries/boost/1.53.0/gnu--4.6.3/include/"
CUDALIB="-L/cineca/prod/compilers/cuda/5.0.35/none/lib64 -L/cineca/prod/libraries/boost/1.53.0/gnu--4.6.3/lib -lcudart"
g++ -O3 $flags -g -o test_gravity_block test_gravity_block.cpp -L. -lsapporo $CUDAINC $CUDALIB -lboost_thread-mt
g++ -O3 $flags -g -o test_gravity_N2ngb test_gravity_N2ngb.cpp -L. -lsapporo $CUDAINC $CUDALIB -lboost_thread-mt
````
* in `Makefile`

````bash
NVCC := /cineca/prod/compilers/cuda/5.0.35/none/bin/nvcc
CUDAPATH    := /cineca/prod/compilers/cuda/5.0.35/none
CUDASDKPATH := /cineca/prod/compilers/cuda/5.0.35/none/samples
CUDAINCLUDE := -I$(CUDAPATH)/include -I$(CUDASDKPATH)/common/inc 
BOOSTPATH := /cineca/prod/libraries/boost/1.53.0/gnu--4.6.3/include
````
* in `configure`

````bash
CUDAINC="-I/cineca/prod/compilers/cuda/5.0.35/none/include -I/cineca/prod/compilers/cuda/5.0.35/none/samples/common/inc -I/cineca/prod/libraries/boost/1.53.0/gnu--4.6.3/include/"
CUDALIB="-L/cineca/prod/compilers/cuda/5.0.35/none/lib64 -lcudart" 
LIBS="$CUDAINC $CUDALIB -L/cineca/prod/libraries/boost/1.53.0/gnu--4.6.3/lib -lboost_thread-mt -DNGB"
````
* in `grape.sh`

````bash
GRAPE_LDFLAGS_='-L$HOME/slPack/sapporo/'
GRAPE_LIBS_='-lsapporo'

````
* in `setup_starlab.sh.sh`
(if you want to compile sapporo using queues, or, load modules by hand if you want to 
compile interactively)

````bash
module purge
module load profile/advanced
module load gnu/4.6.3
module load boost/1.53.0--gnu--4.6.3
module load cuda
LD_LIBRARY_PATH=/cineca/prod/compilers/cuda/5.0.35/none/lib64:/cineca/prod/libraries/boost/1.53.0/gnu--4.6.3/lib
export LD_LIBRARY_PATH
cd $HOME/slPack/starlab
````
#### Green II HPC system @ Swinburne University

Thanks to prof. Jarod Hurley I was able to test the installation of StarLab on the Green II HPC 
system at the Swinburne University. Here how to do that.    

* Log into the system and find yourself in the login node.
* Clone the private repo / download the folders and unpack them like described before.
* Then you need to log into one of the compile/test nodes from the head node: `ssh $USER@gstar001`
* load the right modules:

````bash
module load gcc/4.6.4
module load boost/x86_64/gnu/1.51.0-gcc4.6
module load cuda/4.0
````
You need that version of `gcc` and `boost` because of issues with boost threads in the default versions.
Just in case, check that the paths in the `Makefile` and `compile.h` agree with that shown in     
`module show boost/x86_64/gnu/1.51.0-gcc4.6`
and
`module show cuda`

Make sure you have no `'` around your path, maybe, if you need, only `"` otherwise `sapporo` won't compile.
Just in case, check that the paths in the `Makefile` and `compile.h` agree with that shown in     
`module show boost/x86_64/gnu/1.51.0-gcc4.6`
and
`module show cuda`

If you have our private version you can 
* `cp ../scripts/g2/Makefile ./`
* `cp ../scripts/g2/compile.sh ./`

otherwise try to modify them to have:

````bash
CXX  := g++
CC   := gcc
NVCC := /usr/local/cuda-4.0/bin/nvcc
CUDAINC := -I/usr/local/cuda-4.0/include -I/usr/local/cuda-4.0/C/common/inc 
BOOSTINC := -I/usr/local/x86_64/gnu/boost-1.51.0-gcc4.6
NVCCFLAGS := -O0 -g -D_DEBUG  -maxrregcount=64 $(CUDAINC) $(BOOSTINC) 
````
in the `Makefile` and 

````bash
flags=-DNGB

CUDAINC="-I/usr/local/cuda-4.0/include -I/usr/local/cuda-4.0/C/common/inc"
CUDALIB="-L/usr/local/cuda-4.0/lib64 -L/usr/local/cuda-4.0/lib:/usr/local/cuda-4.0/C/lib"
CUDAFLAG="-lcudart"
BOOSTINC="-I/usr/local/x86_64/gnu/boost-1.51.0-gcc4.6"
BOOSTLIB="-L/usr/local/x86_64/gnu/boost-1.51.0-gcc4.6"
BOOSTFLAG="-lboost_system  -lboost_thread-mt -lpthread"

g++ -O3 $flags -g -o test_gravity_block test_gravity_block.cpp -L. -lsapporo $CUDAINC $CUDALIB $CUDAFLAG $BOOSTINC $BOOSTLIB $BOOSTFLAG
g++ -O3 $flags -g -o test_gravity_N2ngb test_gravity_N2ngb.cpp -L. -lsapporo $CUDAINC $CUDALIB $CUDAFLAG $BOOSTINC $BOOSTLIB $BOOSTFLAG
````
in `compile.sh`.

Then run

* `make clean`
* `make`
* `bash compile.sh`

No go the the starlab folder (`cd ../starlab`) and fix the `configure` file accordingly to this

````bash

````

and the `local/grape.sh` file to point to your sapporo installation.

If you have our version of StarLab, just copy the right files:

* `cp ../scripts/g2/configure ./`
* `cp ../scripts/g2/grape.sh ./local/`

Make sure again `grape.sh` points to the right folder

* `./configure --without-f77 --with-qt=no` (if you want qt, load the modules and check the versions)
* `make clean && make clean && make clean`
* `make && make`
* `rm ./usr/bin/*`
* `make install`

** Troubleshooting **

If you get this error (or some other error)
````bash
make[2]: Entering directory `/mnt/home/bziosi/slpack/starlab/src/gfx/lux'
/bin/sh ../../../libtool --preserve-dup-deps --mode=link gcc  -g -O2  -L/usr/lib64/qt-3.3/lib -o libgfx-2.la   win.lo draw.lo draw1.lo color.lo dialog.lo mcd.lo interface.lo termio.lo utility.lo simple.lo  -I/usr/local/cuda-4.0/include -I/usr/local/cuda-4.0/C/common/inc -L/usr/local/cuda-4.0/lib64 -L/usr/local/cuda-4.0/lib:/usr/local/cuda-4.0/C/lib -lcudart -L/usr/local/x86_64/gnu/boost-1.51.0-gcc4.6 -lboost_system  -lboost_thread-mt -lpthread -DNGB
ar cru .libs/libgfx-2.a  win.o draw.o draw1.o color.o dialog.o mcd.o interface.o termio.o utility.o simple.o
ar: interface.o: No such file or directory
make[2]: *** [libgfx-2.la] Error 1
make[2]: Leaving directory `/mnt/home/bziosi/slpack/starlab/src/gfx/lux'
make[1]: *** [clibs23] Error 2
make[1]: Leaving directory `/mnt/home/bziosi/slpack/starlab/src/gfx'
make: *** [libs] Error 2
````
when compiling may be you can try to `make` and `make clean` some times.    
Also remember that make clean is not working properly, so you need to `make clean` more than once or delete the binaries by yourself.

If you have errors regarding no rules for `libxhdyn.la`, probably you forgot to exclude 
some options from the configure, so run `configure --with-f77=no --with-qt=no` or try `configure --help` 
to check for other options.

### Additional material

* Code units (coming soon...)
* StarLab internals (really???)
* [Our repo](https://bitbucket.org/brunetto/slpack)
* [StarLab tools wiki](http://www.science.uva.nl/sites/modesta/wiki/index.php/Starlab_tools)



