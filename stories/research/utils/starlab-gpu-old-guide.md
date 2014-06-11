<!-- 
.. link: 
.. description: 
.. tags: GPU, simulations, N-body
.. date: 2013/08/20 09:34:11
.. title: StarLab (GPU) old guide
.. slug: starlab-gpu-old-guide
-->

## To install CUDA you can try with the CUDA packages in the Ubuntu repositories.
If they fail, you have to download CUDA from ****

To locate the CUDA files you can try:

* `locate cuda | grep nvcc`
* `locate cuda | grep include`
* `locate cuda | grep include | grep toolkit` (for the SDK files of the new release)
* `locate cuda | grep lib | grep cudaart`

<!-- TEASER_END -->

## Sapporo

* in setup_sapporo.sh change 
````bash
export LD_LIBRARY_PATH=/usr/local/cuda-5.0/:/usr/local/cuda-5.0/samples/common/inc:/usr/include/boost/
````
(installation of the binary drivers from the NVIDIA site) to
````bash
export LD_LIBRARY_PATH=/usr/include/:/usr/lib/nvidia-cuda-toolkit/include/:/usr/include/boost/
````
(ubuntu CUDA distro packages)

* in Makefile put the right path in `NVCC := /usr/bin/nvcc` and be sure to have the right 
paths in 
````bash
CUDAPATH    := /usr/include/
#/usr/local/cuda-5.0
CUDASDKPATH := /usr/lib/nvidia-cuda-toolkit/include/
#/usr/local/cuda-5.0/samples/common/inc
CUDAINCLUDE := -I$(CUDAPATH)/include -I$(CUDASDKPATH)
# RE - added these path/includes (added to NVCCFLAGS and CXXFLAGS, too)
BOOSTPATH := /usr/include/boost 
BOOSTINCLUDE := -I$(BOOSTPATH)
````
the commented path refers to the binary installation from the NVIDIA site.

* Launch `bash ./setup_sapporo.sh` and if you get
````bash
host_evaluate_gravity.cu:3: fatal error: multithreading.h: No such file or directory
````
puth `multithreading.h` in the sapporo folder and then in `host_evaluate_gravity.cu` change 
````c
#include <multithreading.h>
````
to 
````c
#include "multithreading.h"
````
so c++ can find the header in the current directory.

* if all is going right, by running again `bash setup_sapporo.sh` you should
obtain something like 
````bash
/bin/rm -rf *.o *.cu_o libsapporo.a
/bin/rm -rf test_gravity_block test_gravity_N2ngb
g++ -O3 -DNGB -I/usr/include//include -I/usr/lib/nvidia-cuda-toolkit/include/ -I/usr/include/boost    -c -o GPUWorker.o GPUWorker.cc
g++ -O3 -DNGB -I/usr/include//include -I/usr/lib/nvidia-cuda-toolkit/include/ -I/usr/include/boost  -c sapporo.cpp -o sapporo.o
sapporo.cpp: In member function ‘int sapporo::open(int)’:
sapporo.cpp:40:25: warning: ignoring return value of ‘char* fgets(char*, int, FILE*)’, declared with attribute warn_unused_result [-Wunused-result]
sapporo.cpp:42:25: warning: ignoring return value of ‘char* fgets(char*, int, FILE*)’, declared with attribute warn_unused_result [-Wunused-result]
sapporo.cpp:67:24: warning: ignoring return value of ‘char* fgets(char*, int, FILE*)’, declared with attribute warn_unused_result [-Wunused-result]
g++ -O3 -DNGB -I/usr/include//include -I/usr/lib/nvidia-cuda-toolkit/include/ -I/usr/include/boost  -c send_fetch_data.cpp -o send_fetch_data.o
g++ -O3 -DNGB -I/usr/include//include -I/usr/lib/nvidia-cuda-toolkit/include/ -I/usr/include/boost  -c sapporoG6lib.cpp -o sapporoG6lib.o

*/usr/bin/nvcc -O0 -g -D_DEBUG  -maxrregcount=64 -I/usr/include//include -I/usr/lib/nvidia-cuda-toolkit/include/ -I/usr/include/boost  -c host_evaluate_gravity.cu -o host_evaluate_gravity.cu_o
 Iar qv libsapporo.a GPUWorker.o sapporo.o send_fetch_data.o sapporoG6lib.o host_evaluate_gravity.cu_o
ar: creating libsapporo.a
a - GPUWorker.o
a - sapporo.o
a - send_fetch_data.o
a - sapporoG6lib.o
a - host_evaluate_gravity.cu_o
ranlib libsapporo.a
````

* to test the compilation run 
````bash 
test_gravity_N2ngb 900
````
and
````bash 
test_gravity_block 900
````
where 900 is the number of particles involved in the test. You can choose the number you prefer
but the test fail if the number is less than ~800.

## StarLab

* change configure CUDA lines:
````bash
CUDAINC="-I/usr/include -I/usr/lib/nvidia-cuda-toolkit/include/ -I/usr/include/boost" 
CUDALIB="-L/usr/libx86_64-linux-gnu/ -lcudart"
LIBS="$CUDAINC $CUDALIB -lboost_system -lboost_thread -lpthread -DNGB"
````
* and change local/grape.sh
````bash
CUDAINC="-I/usr/include -I/usr/lib/nvidia-cuda-toolkit/include/ -I/usr/include/boost" 
CUDALIB="-L/usr/libx86_64-linux-gnu/ -lcudart"

# CUDAINC="-I/usr/local/cuda-5.0/include -I/usr/local/cuda-5.0/samples/common/inc -I/usr/include/boost" 
# CUDALIB="-L/usr/local/cuda-5.0/lib64/ -lcudart" 

LIBS1="$CUDAINC $CUDALIB -lboost_system -lboost_thread -lpthread -DNGB"

#g++ -O3 $flags -g -o test_gravity_block test_gravity_block.cpp -L. -lsapporo $CUDAINC $CUDALIB -lboost_thread
g++ -O3 $flags -g -o test_gravity_block test_gravity_block.cpp -L. -lsapporo $CUDAINC $CUDALIB $LIBS1

# Where to find GRAPE libraries:
# GRAPE_LDFLAGS_='-L/home/mapelli/MICMAP/programmi/sapporo161_release/'
GRAPE_LDFLAGS_='-L/home/ziosi/Code/Mapelli/starlab/sapporo/sapporo161_release'
````

* run `make clean`

* run `./configure --without-fortran` (`--without-f77`)

* `make`

* `make install`

* now you can find the `kira` binary in `/usr/local/bin` or`/usr/bin`

* run 
````bash
./kira -t 500 -d 1 -D 1 -b 1 \
             -n 10 -e 0.000 -B   \
	 <  cineca95_bin_N5000_frac01_W5_Z001_IC.txt \
	 > new_cineca95_bin_N5000_frac01_W5_Z001.txt \
	 2> ew_cineca95_bin_N5000_frac01_W5_Z001.txt
````











