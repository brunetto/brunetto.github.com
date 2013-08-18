<!-- 
.. link: 
.. description: 
.. tags: astro/physics, Cosmology, Master Thesis, millennium, N-body, Python, simulation, imported
.. date: 2011-12-04
.. title: GIF2 substructures coordinates correction
.. slug: gif2-substructures-coordinates-correction
-->

I used this script to change the coordinates of the substructures in the GIF2 simulation output from the center of mass coordinates to the global ones. The substructures were stored in our server in files referring to the index of the halo to which they belong and their coordinates were respect to the center of the halo. For each halo this script read the subhaloes center of mass coordinates in kpc and change them to global coordinates in Mpc managing the periodic boundary conditions .    

<!-- TEASER_END -->    

````python
#!/usr/bin/env python
import numpy as np
import tables as tb
import time
import sys

"""Legge il file con id e centri degli aloni con sottostrutture, per
ogni alone (id) apre il file Sub.3..053.gv, legge le coordinate
alle colonne 8, 9, 10 (in kpc!!!) e le corregge (tenendo conto delle
condizioni periodiche) con le coordinate del centro prese dalla lista
degli aloni iniziale.  Le coordinate vengono aggiunte ad un vettore
che alla fine viene salvato in un file hdf5.
"""

t = time.time()
print "Start"
````
    
As usual: imports, documentation and timing initialization.    
    
````python
halo_centers_file = 'haloes_with_substructures_centers.h5'

h5 = tb.openFile(halo_centers_file, 'r')
haloes = h5.root.data.read()
h5.close()

haloes = haloes.astype(float)
````
    
This piece of code reads the halo centers from a file.    
    
````python
substructure_coord = np.empty((0, 3))
files_num = haloes[:, 0].shape[0]
void_files = 0
````
    
Here we create the first (void) record of the substructures coordinates table, find the number of haloes and create a variable which will tell us how many haloes without subtructures we have.    
    
Now, for each halo we    
````python
for i in xrange(files_num):
    print "Loop ", i, " di ", files_num 
    sub_file = "cm/Sub.3."+'%07d'%int(haloes[i,0])+".053.gv"
    ````
    
open the related substructures file     
````python
try:
        sub_coord = np.genfromtxt(sub_file, dtype='float', usecols=(8, 9, 10))
        file_check = True
    except:
        print "Void file ", sub_file
        file_check = False
        void_files += 1
````
    
try to read the substructures coordinates, if it fails, we assume that the file is empty (and the halo has no substructures). In this case we increment the counter of the empy files.    
````python
if file_check:
        if sub_coord.ndim == 1:
            sub_coord = sub_coord.reshape((1, sub_coord.shape[0]))
            #print "sh min ", np.amin(sub_coord, 0)
            #print "sh min ", np.amax(sub_coord, 0)
````
    
This reshape the array in case we have only one subhalo: in this case (I hope I remember correct!:P) instead of one row and three columns we should have three values, so we have to reshape the array to pass it to the rest of the code.    
````python
try:
            sub_x = sub_coord[:, 0]/1000. + haloes[i,1]
            if not np.all(sub_x &gt; 0):
                sub_x[sub_x&lt;0]+=110 # condizioni periodiche
            if not np.all(sub_x 110]-=110
            if not (np.all(sub_x &gt; 0) and np.all(sub_x  0)
                print sub_x 
                print haloes[i, 1:3]
                sys.exit()
            sub_y = sub_coord[:, 1]/1000. + haloes[i,2]
            if not np.all(sub_y &gt; 0):
                sub_y[sub_y&lt;0]+=110 # condizioni periodiche
            if not np.all(sub_y 110]-=110
            if not (np.all(sub_y &gt; 0) and np.all(sub_y  0)
                print sub_y
                print haloes[i, 1:3]
                sys.exit()
            sub_z = sub_coord[:, 2]/1000. + haloes[i,3]
            if not np.all(sub_z &gt; 0):
                sub_z[sub_z&lt;0]+=110 # condizioni periodiche
            if not np.all(sub_z 110]-=110
            if not (np.all(sub_z &gt; 0) and np.all(sub_z  0)
                print sub_z 
                print haloes[i, 1:3]
                sys.exit()
            substructure_coord = np.vstack((substructure_coord, np.hstack((sub_x.reshape((sub_x.shape[0], 1)), 
                                                                           sub_y.reshape((sub_y.shape[0], 1)), 
                                                                           sub_z.reshape((sub_z.shape[0], 1))))))
````
    
This corrects the coordinates keeping in mind the periodic boundary conditions and add the new substructures coordinates to the corrected substructures array.    
````python
except:
            print "file ", sub_file
            print "sub_coord.shape ", sub_coord.shape
            print "sub_coord ", sub_coord
            print "haloes coord ", haloes[i, :]
            print "exit"
            sys.exit()
    else:
        pass
````
    
If something goes wrong, we handle the failure printing some information.    
````python
h5 = tb.openFile('sub_haloes_global_coords.h5', 'w')
h5.createArray(h5.root, 'data', substructure_coord)
h5.flush()
h5.close()
print "Done in ", time.time()-t, " with ", void_files, " void files"
````
    
In the end, we save the array in an HDF5 file!:)
