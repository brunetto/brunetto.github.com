<!-- 
.. link: 
.. description: 
.. tags: astro/physics, code, Gadget2, Cosmology, millennium, N-body, PhD, simulation, imported
.. date: 2012-01-07
.. title: My first Gadget2 tests
.. slug: my-first-gadget2-tests
-->

This post is about my first experience with the cosmological simulation code <a href="http://www.mpa-garching.mpg.de/gadget/" title="Gadget2">Gadget2</a>. To start I followed the instructions found <a href="http://astrobites.com/2011/04/02/installing-and-running-gadget-2/">here</a>. All I'm going to write refers to an Ubuntu/Kubuntu 11.10 installation.    

<!-- TEASER_END -->    

<strong>Installation of GSL and fftw</strong>    
    
We can download Gadget <a href="http://www.mpa-garching.mpg.de/gadget/" title="Gadget download">here</a>, the GSL (GNU scientific library) <a href="http://mirror.rit.edu/gnu/gsl/gsl-1.9.tar.gz" title="GSL download">here</a> and the FFTW (fastest Fourier transform in the West library) <a href="http://www.fftw.org/fftw-2.1.5.tar.gz" title="FFTW download">here</a>. We also need an MPI library (Open-MPI or MPICH, try install it using your package manager).    
Following the Astrobites suggestions let's decompress the archives with `tar -xzf &lt;archive name&gt;`. Now we can install the libraries following the Astrobites post:    
    
````bash
goldbaum@~/Documents/code: cd gsl-1.9/
goldbaum@~/Documents/code/gsl-1.9: ./configure
snip: lots of diagnostic ouput
goldbaum@~/Documents/code/gsl-1.9: make
snip: lots of compilation output
goldbaum@~/Documents/code/gsl-1.9: sudo make install
Password:
snip: lots of diagnostic output
goldbaum@~/Documents/code/gsl-1.9: cd ..
goldbaum@~/Documents/code: cd fftw-2.1.5
goldbaum@~/Documents/code/fftw-2.1.5: ./configure --enable-mpi --enable-type-prefix --enable-float
snip: lots of diagnostic output
goldbaum@~/Documents/code/gsl-1.9: make
snip: lots of compilation output
goldbaum@~/Documents/code/gsl-1.9: sudo make install
Password:
snip: lots of diagnostic output
goldbaum@~/Documents/code/gsl-1.9: cd ..
````
    
    
As described <a href="http://www.fftw.org/fftw2_doc/fftw_6.html#SEC69" target="_blank" title="FTTW installation and customization">here</a> is convenient to install both the single and the double precision version of the FFTW (for example to compile the initial conditions generators) with (that is, without `--enable-float`)    
    
````bash 
goldbaum@~/Documents/code: cd fftw-2.1.5
goldbaum@~/Documents/code/fftw-2.1.5: ./configure --enable-mpi --enable-type-prefix
snip: lots of diagnostic output
goldbaum@~/Documents/code/gsl-1.9: make
snip: lots of compilation output
goldbaum@~/Documents/code/gsl-1.9: sudo make install
Password:
snip: lots of diagnostic output
````
    
<strong>Play with Gadget2</strong>    
    
Now it's time to play with Gadget!:) In this code, for performance reasons, requires to specify some parameters at compile time while other can be set at run time, so that we have to customize the Makefile. This also imply that we should have separate binary files and directories for each simulation.    
To start with something easy, we will customize one of the examples given with the code, the "galaxy" one. It simulate the collision of two galaxies using 40000 DM particles for the haloes and 20000 baryonic particles for the disks.    
    
Inside the Gadget directory we have    
````
Analysis
AUTHORS
COPYING
COPYRIGHT
Documentation
Gadget2
ICs
README
````
    
In the `Analysis` folder we can fin some analysis routines provided by the author, the `Documentation` folder contains the user guide and the original paper, and the `AUTHORS, COPYING, COPYRIGHT` self-explanatory. The `ICs` folder contains the initial conditions for the example simulations and the `Gadget2` folder contains the sources and the html documentation.    
    
To be tidy and organized is better to have a folder for every simulations, so we will create a (descriptive) with everything we need to customize     
````bash 
mkdir 2012-01-07-Gadget2-galaxy_test_01
cd 2012-01-07-Gadget2-galaxy_test_01
mkdir out
cp ../ICs/galaxy_littleendian.dat ./
cp ../Gadget2/parameterfiles/galaxy.param ../Gadget2/parameterfiles/galaxy.Makefile ./
````
    
In the folder Gadget2 we can find the general `Makefile` but for now let's use the galaxy's one provided by the author and just copied to our position. Open it with your preferred text editor (for example, in a command line environment, `emacs -nw Makefile`).    
This `Makefile` is already customized for the galaxy collision simulation and if you want to understand every option you can read the description in the guide, but we need some more customization. Here what I've changed:    

````bash
OPT   +=  -DHAVE_HDF5  
````
    
so I activate the HDF5 format for the output and    

````bash
#--------------------------------------- Select target computer

SYSTYPE="Uno"
\#SYSTYPE="MPA"
\#SYSTYPE="Mako"
\#SYSTYPE="Regatta"
\#SYSTYPE="RZG_LinuxCluster"
\#SYSTYPE="RZG_LinuxCluster-gcc"
\#SYSTYPE="Opteron"

\#--------------------------------------- Adjust settings for target computer

ifeq ($(SYSTYPE),"Uno")
CC       =  mpicc   
OPTIMIZE =  -O3 -Wall
GSL_INCL =  -I/usr/local/include
GSL_LIBS =  -L/usr/local/lib
FFTW_INCL=  -I/usr/local/include
FFTW_LIBS=  -L/usr/local/lib
MPICHLIB =  -L/usr/lib
HDF5INCL =  
HDF5LIB  =  -lhdf5 -lz 
endif
````
    
    
to select the set the options for my system.    
Now we have to customize the `run/galaxy.param` file changing it like this:    

````bash
InitCondFile      ./galaxy_littleendian.dat
OutputDir          ./galaxy_out/
OutputListFilename ./out/output_list.txt
SnapFormat         3  %to select the HDF5 format
TimeBegin           0.0        % Begin of the simulation
TimeMax             40.0        % End of the simulation

% Output frequency
TimeBetSnapshot        0.1% original 0.5 </pre>
    
    
Now we should go to the sources folder and compile the code with    
<pre>cd ../Gadget2
make -f 2012-01-07-Gadget2-galaxy_test_01/galaxy.Makefile
cp Gadget2 ../2012-01-07-Gadget2-galaxy_test_01/Gadget2
make clean
cd 2012-01-07-Gadget2-galaxy_test_01
````
    
The last command clean the build leaving only the sources files, so we are ready for a new build.    
We can also create a script for automatize all this steps, something like:    

````bash
#!/bin/bash
dir=$1
ics=$2
param_file=$3
mk_file=$4
CPUs=$5

if [ $# -lt 5 ] ; then
  echo "usage: gadget_set directory_name initial_conditions_file
parameters_file make_file number_of_CPUs"
  exit 0
fi

echo "Assuming to use $dir as the run folder," 
echo "$ics as initial conditions,"
echo "$paramfile as parameter file, "
echo "$mk_file as makefile "
echo "and to run on $CPUs CPUs."

mkdir $dir
cd $dir
mkdir out
cp ../ICs/$ics ./
cp ../Gadget2/parameterfiles/$param_file
../Gadget2/parameterfiles/mk_file ./
cd ../Gadget2
make -f ../$dir/$mk_file
cp Gadget2 ../$dir/Gadget2
make clean
cd $dir
mpirun -np $CPUs ./Gadget2 $param_file
````
    
This is a very raw and untested script, but it's just to give an idea.    
    
Now we are ready to start the simulation with     

````bash
mpirun -np 2 ./Gadget2 galaxy.param
````
    
where `-np` sets the number of processes/processors to be used in parallel.    
When the simulation stops we can analyze it with the tools provided in the `Analysis` folder or, if you like me don't own an IDL license and don't feel comfortable with IDL/Fortran/C for the data analysis, with something like (to be run in out/plots/):    
    
````python
#!/use/bin/env python
import sys, os
from subprocess import Popen, PIPE
from multiprocessing import Process, Queue

import numpy as np
import tables as tb
import time
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

"""This script will plot in parallel the .h5 snapshots created by Gadget2 test
runs one after the other!:).
FIXME: i need a way to wait for the final time count the end of the processes
and a way to print the status
"""

# Set the max number of processes
n_procs = 3

# Set the number of snapshot to be plotted
n_snap = 401

t = time.time()

print "Defining workers..."

def worker(input, output):
    while input.qsize() != 0:
        item = input.get()
        if item[0]= 10 and item[0]&lt;100: j="0"+str(item[0])
        else: j=str(item[0])
        try:
#     print "considering file ../snapshot_"+j+".hdf5"
#     print "open file "
            h5 = tb.openFile("../snapshot_"+j+".hdf5", 'r')
#     print "file opened, set variables"
            halo = h5.root.PartType1
            disk = h5.root.PartType2
#            print "setted, inizialize figure"
            fig2 = plt.figure()
            ax = Axes3D(fig2)
            ax.scatter(disk.Coordinates[:,0], 
                       disk.Coordinates[:,1],
                       disk.Coordinates[:,2],
                       color='red', s=0.5)
            ax.scatter(halo.Coordinates[:,0], 
                       halo.Coordinates[:,1],
                       halo.Coordinates[:,2],
                       color='blue', s=0.01)
            plt.savefig('snap_'+j)
#            print "done, closing file"
            h5.close()  
#            print "closed"

        except:
            print "Work "+j+" not done, exit..."
            sys.exit()

def fill_queue(task_queue):
    for i in range(n_snap):
        task_queue.put([i])
    return task_queue

def status(proc):
    if proc.is_alive==True:
        return 'alive'
    elif proc.is_alive==False:
        return 'dead'
    else:
        return proc.is_alive()

print "Define queues..."

input_queue = Queue()
output_queue = Queue()

try:
    input_queue = fill_queue(input_queue)
except:
    print "Queue not filled, exit..."
    sys.exit()

procs = []

try:
    for i in range(n_procs):
        procs.append(Process(target=worker, args=(input_queue,
output_queue)))
except:
    print "Creating processes not complete, exit..."
    sys.exit()

try:
    for i in procs:
        i.start()
except:
    print "Start processes not complete, exit..."
    sys.exit()

for i in procs:
    print "Process ", i," @ " , i.pid, " is ", status(i)

print "Done in "+str(time.time()-t)+" seconds."
````
Now we have one image for each snapshot, and if we are interested we can produce a video with:    
````bash 
mencoder mf://*.png -mf fps=25:type=png -ovc lavc -lavcopts vcodec=mpeg4:mbd=2:trell -vf scale=720:360 -oac copy -o output.mp4
````
    
    
[This](youtube http://www.youtube.com/watch?v=b7HyafKMkxI&amp;w=560&amp;h=315) is the first basic video, with logarithmic time and perhaps there's something wrong with the coordinates on the axes.    
