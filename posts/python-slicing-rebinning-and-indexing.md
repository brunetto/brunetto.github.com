<!-- 
.. link: 
.. description: 
.. tags: code, Python
.. date: 2011-11-25
.. title: Python slicing, rebinning and indexing
.. slug: python-slicing-rebinning-and-indexing
-->

During my master thesis I had to manage a lot of (different) data from GIF and GIF2 projects, Millimillennium, Millenium and Millennium 2 simulations and so on. Sometimes there were the need to sort, divide or rearrange these dataset.     
Here some examples.    

<!-- TEASER_END -->    

<strong>Sort the Millennium 2 data</strong>    
    
I developed this script to sort the Millennium 2 data in the $x$ coordinate. The dataset was composed of 512 hdf5 files and I would like to create 1000 files of 100 kpc/h each, taking particles for all the original files.    
````python
#!/bin/env python
import time
import numpy as np
import tables as tb
````
    
This is the usual modules importing. <code>tables</code> is the module provided by PyTables to manage, in a great way, hdf5 file under Python.    
    
````python
t_glob = time.time()
````
    
Timing is always good!!!    
    
````python
# This create the first "5 Mpc/h" file, every loop operate on 100 kpc/h of data 
for i in range(0,50):
    t = time.time()
    i_dist = i/10.0
    j_dist = i_dist + 0.1
    print "Starting with limits [Mpc/h]", i_dist, j_dist
    temp2 = np.array([])
    temp2.shape = (0,3)
    # This loop open each of the 512 original files
    # selecting the particles inside the limits
    # and stacking them into the array that will 
    # be saved in the new file
    for j in range(0,512):
        filename = '../../hdf5/data_'+str(j)
        print "Open ", filename
        h5 = tb.openFile(filename, 'r')
        original = h5.root.data.read()
        h5.close()
        temp = original[original[:,0]&gt;i_dist]
        if temp.size &lt; 3:
            temp3 = np.array([])
            temp3.shape=(0,3)
        else:
            temp3 = temp[temp[:,0]&lt;=j_dist]
        try:
            temp2 = np.vstack((temp2,temp3))
        except:
            print "Error in stacking"
            print "temp2 dimensions ", temp2.shape
            print "temp3 dimensions ", temp3.shape
            exit()
    tt=time.time()

    # Sorting the array in the x direction
    temp2[temp2[:,0].argsort(),]
    print "Time for argsort ", time.time()-tt

    # Writing data to file
    destname = '../../hdf5_sorted/mill2sort-'+str(i)
    print "Writing ", destname
    dest = tb.openFile(destname, 'w')
    dest.createArray(dest.root, 'data', temp2, title='data')
    dest.flush()
    dest.close()
    print "Time for loop  ", i, " is ", time.time()-t
print "Done in ",time.time()-t_glob, "seconds"
````
    
<strong>Rebin the sorted Millennium 2 data</strong>    
    
After I have sorted the data, we need to rebin the dataset because it doesn't fit into our machine memory.    
This script make use of the <a href="http://brunettoziosi.blogspot.it/2011/11/python-parallel-job-manager.html" target="_blank" title="Python parallel job manager"> parallel job manager</a> to break the 1000 files of the sorted dataset into 5000 files each containing 20 kpc/h of data, sorted in the $x$ direction.    
````python
#! /usr/bin/env python

import sys, os
import numpy as np
import tables as tb
from subprocess import Popen, PIPE
from multiprocessing import Process, Queue


#############################################
sub_slice_dim = 0.02    #Mpc/h
sub_slice_num = 5 # for each of the original slice
n_procs = 5
tot_mill_slice = 999   # number of original slices
############################################


def slicing(i, j, sub_slice_dim, sub_slice_num):
    """Given a mill2 slice it creates 5 subslices.
    """
    start_dim = j\*sub_slice_dim
    stop_dim = start_dim + sub_slice_dim
    print "Loop ", j, " of ", sub_slice_num , " between ", start_dim, " and ", stop_dim, " in slice ", i 
    pos_greater = mill_slice[start_dim &lt; mill_slice[:,0]]
    pos = pos_greater[pos_greater[:,0] &lt;= stop_dim]
    h5=tb.openFile('/home/ziosi/mill2_data/hdf5_sorted_rebinned/mill2sort-'+str(i*5+j)+'.h5', 'w')
    h5.createArray(h5.root, 'data', pos, title='mill2_sorted_rebinned_pos')
    h5.flush()
    h5.close()

def breakmill(in_queue):
    """Bring a slice from the queue and start the function to
    sub_slice it.
    """
    while in_queue.qsize != 0:
        ii = in_queue.get()
        i = ii[0]
        sub_slice_dim = ii[1]
        sub_slice_num = ii[2]
        original_slice = "/home/ziosi/mill2_data/hdf5_sorted/mill2sort-"+str(i)
        mill_slice = tb.openFile(original_slice, 'r')
        slice_data = mill_slice.root.data.read()
        slice_min = np.amin(slice_data[:,0])
        for j in xrange(5):
            slicing(i, j, sub_slice, slice_dim, sub_slice_num)
    
# Create the queues.
in_queue = Queue()
out_queue = Queue()

# Fill the input queue.
try:
    for i in xrange(tot_mill_slice):
        in_queue.put([i, sub_slice_dim, sub_slice_num])
except:
    print "Input queue not filled, exit!"
    sys.exit(1)

procs = []

# Create the processes.
try:
    for i in range(n_procs):
        print "Process creation loop ", i
        procs.append(Process(target=breakmill, args=(in_queue, out_queue)))
except:
    print "Creating processes not complete, exit..."
    sys.exit(1)

# Start the processes.
try:
    for i in procs:
        i.start()
except:
    print "Start processes not complete, exit...";
    sys.exit(1)

# Check for processes status.
for i in procs:
    print "Process ", i," @ " , i.pid, " is ", status(i)

print "Done."
````
    
    
<strong>Indexing data</strong>    
    
We also need to index a data file to can retrieve only a slice from the entire file. We did it using the following three elements:    
````python
flags = np.arange(0, 110, 0.1)
````
    
is the array containing the markers for the distances we want to index. This means that if we want to index distances from 0 to 10 every 1, we get: 0,1,2,3,4,5,6,7,8,9,10, so we can select, for example, the element between 0 and 1 without load the entire list.    
````python
start = indexes[np.maximum(np.searchsorted(indexes[:,0], xstart, side='left')-1, 0), 1]
````
    
contains the index of the cell in the array that contains the first element we want    
````python
stop = indexes[np.minimum(np.searchsorted(indexes[:+1], xstop, side='right')+1, indexes.shape[0]-1), 2]
````
    
contains the index of the cell in the array that contains the first element we want.    
    
````python
indexes = np.hstack((flags.reshape((flags.shape[0], 1)), start.reshape((start.shape[0], 1)), end.reshape((end.shape[0], 1))))
````
    
is the $(n,3)$ array with the flag, the start and the stop indexes. It is saved into the data file.
