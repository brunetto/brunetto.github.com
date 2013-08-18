<!-- 
.. link: 
.. description: 
.. tags: code, Python
.. date: 2011-12-02
.. title: From .csv to HDF5 in Python
.. slug: from-csv-to-hdf5-in-python
-->

PyTables is a Python library that provide a simple but really useful interface to manage the HDF5 files with some other interesting features (compression, optimizations, ...). To the library presentation and documentation, for now refers, to the <a href="http://www.pytables.org/moin" target="_blank" title="site">site</a>.    
I used it a lot during my master thesis to manage the dataset from the Millennium database.    
Here I provide a brief review of how I used it to store data obtained in .csv (comma separated values) format.    

<!-- TEASER_END -->    

````python 
#!/usr/bin/env python

import numpy as np
import tables as tb
import time

t = time.time()
````
    
As usual, we have the initial import of the modules we need and start the timing of the code.    
    
````python 
fofhdf5 = tb.openFile('mill2_fof_snap67.h5', 'w')
````
    
This create the HDF5-file object we use to work on the file, in write (`'w'`) mode. Read-only (`'r'`) mode is also possible.    
````python 
fof_data = np.genfromtxt('fof0.csv', dtype=([('fofId', 'i8'), ('np', 'i4'), ('mass', 'f4'), ('x', 'f4'), ('y', 'f4'), ('z', 'f4'), ('ix', 'i4'), ('iy', 'i4'), ('iz', 'i4'), ('m_crit_200', 'f4'), ('r_crit_200', 'f4'), ('m_mean_200', 'f4'), ('r_meam_200', 'f4'), ('m_tophat', 'f4'), ('r_tophat', 'f4'), ('numSubs', 'i4')]), comments='#', delimiter=',', skiprows=26)
````
    
Here we read the .csv/ASCII table and from this we create a table of numpy arrays, each of them with its own name and type. It's also possible to specify the character for the comments in the file (`#`), the character separating the values (commas, spaces, ...) and the number of line to be skipped (file header).    
    
````python 
table = fofhdf5.createTable(fofhdf5.root, description=fof_data, name='fof_data_snap67', title="fof_data_snap67", expectedrows=11697806)
````
    
create the HDF5-table with the proper hierarchy, some metadata (description and title). Specify the number of rows one expects to put into the table helps the library to optimize the operations and the space.    
    
````python 
for i in range(1, 20):
    fof_data = np.genfromtxt('fof'+str(i)+'.csv', dtype=([('fofId', 'i8'), ('np', 'i4'), ('mass', 'f4'), ('x', 'f4'), ('y', 'f4'), ('z', 'f4'), ('ix', 'i4'), ('iy', 'i4'), ('iz', 'i4'), ('m_crit_200', 'f4'), ('r_crit_200', 'f4'), ('m_mean_200', 'f4'), ('r_meam_200', 'f4'), ('m_tophat', 'f4'), ('r_tophat', 'f4'), ('numSubs', 'i4')]), comments='#', delimiter=',', skiprows=26)
    
    table.append(fof_data)
    table.flush()
    print "Loop ", i, " done."

fofhdf5.close()
print "Done in ", time.time()-t, "seconds !!!"
````
    
The `for` loop opens other ASCII tables and append them to the existing HDF5-table. The `table.flush()` command let the library physically write the data on the disk instead of maintaining them in memory and write them periodically. After that we close the file object.