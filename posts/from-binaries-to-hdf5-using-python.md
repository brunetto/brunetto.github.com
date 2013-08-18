<!-- 
.. link: 
.. description: 
.. tags: code, Python
.. date: 2011-12-02
.. title: From binaries to HDF5 using Python
.. slug: from-binaries-to-hdf5-using-python
-->

I have used this script to convert the Millennium II data from the unformatted fortran binary formato to the DF5 one.    
The core of the script is a module (<code>modified_read_snapshots</code>) built on the basis of a script kindly provided by <a href="http://mbk.ps.uci.edu/index.html" target="_blank" title="Mike Boylan-Kolchin">Mike Boylan-Kolchin</a> from the group that perform the Millennium II simulation.     

<!-- TEASER_END -->

````python
#!/usr/bin/env python    

import time
import kd3hdf5
import tables as tb
import modified_read_snapshots as rs

t = time.time()
````
    
The usual imports and time initialization!:P    
    
````python
def bin2hdf5(bin_file, h5_file, tree = False):
    snap = rs.read_snapshot(bin_file)
    h5f = kd3hdf5.KDTree(h5_file, 'w')
    h5f.data_store(snap['pos'])
    if tree == True:
        h5f.tree_build
    h5f.close()````
    
This function accept as arguments the name of the binary file, the name of the HDF5 file to be created and give the user the possibility to create a KDTree with the data. By default it won't create this tree. If no KDTree must be created the function only uses the part of the <code>kd3hdf5</code> module that store the data into the HDF5 file. We will have a brief view of this at the end of the post.    
````python
def main():
    print "start"
    for i in [0, 10, 100, 200, 511]:
        t2 = time.time()
        print "Loop ", i
        t3 = time.time()
        bin2hdf5('../binary/snap_newMillen_subidorder_067.'+str(i), '../hdf5/data_'+str(i))
        print "Loop ", i, " finished in ", time.time()-t2

    print "That's all folks, in ", time.time()-t, "!!!"

if __name__ == "__main__":
    main()
````
    
Nothing more than calling the previous function on the data files looping on their names!:)    
Respect to the other posts here we make use of the <code>main</code> function but is nothing extraordinary!:P    
    
The code from the <code>kd3hdf5</code> module is    
````python
class KDTree(object):
    #Docs [...]

    def __init__(self, filename, mode):
        if mode == 'read' or mode == 'r':
            self.h5file = tb.openFile(filename, mode = "r")
        elif mode == 'append' or mode == 'a':
            self.h5file = tb.openFile(filename, mode = "a")
        elif mode == 'build' or mode == 'w' or mode == 'write':
            self.h5file = tb.openFile(filename, mode = "w")
````
    
This provide the creation of the object, linked to an HDF5 file and    
    
````python    
def data_store(self, data):
        t = time.time()
        self.h5file.createArray(self.h5file.root, 'data', np.asarray(data), title='data')
        self.h5file.root.data._v_attrs.n_elements = data.shape[0]
        self.h5file.root.data._v_attrs.m_dimensions = data.shape[1]
        self.h5file.root.data._v_attrs.maxes = np.amax(data,axis=0)   # maxes and mins for each coord
        self.h5file.root.data._v_attrs.mins = np.amin(data,axis=0)
        print self.h5file.root.data._v_attrs.n_elements, " Stored in ", time.time()-t, "seconds."
        t = time.time()
        self.h5file.root.data.flush()
        print time.time()-t, " seconds to commit changes."
````
    
fill the file with the data and some metadata (table dimension and maxes and mins of the data).


