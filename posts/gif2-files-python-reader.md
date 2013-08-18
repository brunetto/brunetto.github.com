<!-- 
.. link: 
.. description: 
.. tags: astro/physics, Cosmology, Master Thesis, millennium, N-body, Python, simulation, imported
.. date: 2011-12-06
.. title: GIF2 files Python reader
.. slug: gif2-files-python-reader
-->

I create this script on the basis of the code to read the Millennium II data (the same used <a href="http://elbrunz.wordpress.com/2011/12/02/from-binaries-to-hdf5-using-python/" title="From binaries to HDF5 using Python">here</a>) provided by <a href="http://mbk.ps.uci.edu/index.html" title="Mike Boylan-Kolchin">Mike Boylan-Kolchin</a>. Being allowed to read the Fortran code to write and read the GIF2 files I could adapt this script to exactly fit this problem.    

<!-- TEASER_END-->    

````python
import numpy as np
import sys

class head:
    def __init__(self, fname):
        import types
        bo_mark='>'
        # start by reading in header:    
        if type(fname) is types.StringType:
            f=open(fname, 'rb')
        elif type(fname) is not types.FileType:
            raise TypeError('argument must either be an open file or ' + 
                            'a string containing a file name')
        else:
            f=fname
````
    
After the usual imports we define a class to read and contain the file header. These first lines check the "filename" argument.    
    
````python
self.pad = np.fromfile(f, count=1, dtype=bo_mark+'i4')
````
    
In the unformatted Fortran binary files the "pad" is a 4-byte space to separate the values of different quantities in the file. `bo_mark` contains the endianess ("bo" means byte order) of the system allowing Python to correctly interpret the numbers from the binary file. `count` sets the number of item of type `dtype` to be read. For example `count=3` and `dtype=bo_mark+'i4'` will store three 4-byte integer in the variable, with the byte order expressed by `bo_mark`, `<` for big-endian, `>` for little-endian.    
````python
# npart is an array containing the number of particles in the
        # file divided by type (gas, ...)
        self.npart = np.fromfile(f, count=6, dtype=bo_mark+'i4')
        self.massarr = np.fromfile(f, count=6, dtype=bo_mark+'f8')
        self.aaa = np.fromfile(f, count=1, dtype=bo_mark+'f8')
        self.redshift = np.fromfile(f, count=1, dtype=bo_mark+'f8')
        self.flag_sfr = np.fromfile(f, count=1, dtype=bo_mark+'i4')
        self.flag_feedback = np.fromfile(f, count=1, dtype=bo_mark+'i4')
        self.nall = np.fromfile(f, count=6, dtype=bo_mark+'i4')
        self.cooling_flag = np.fromfile(f, count=1, dtype=bo_mark+'i4')
        self.numfiles = np.fromfile(f, count=1, dtype=bo_mark+'i4')
        self.boxsize = np.fromfile(f, count=1, dtype=bo_mark+'f8')
        self.Omega = np.fromfile(f, count=1, dtype=bo_mark+'f8')
        self.OmegaL0 = np.fromfile(f, count=1, dtype=bo_mark+'f8')
        self.Hubblepar = np.fromfile(f, count=1, dtype=bo_mark+'f8')
        self.version = np.fromfile(f, count=1, dtype=bo_mark+'a96')
        self.pad2=np.fromfile(f, count=1, dtype=bo_mark+'i4')
        if type(fname) is types.StringType: f.close()
````
    
These lines read and store the values of the quantities saved in the header of the file.    
````python
def read_gif2_file(fname):
    bo_mark = '>'
    f=open(fname, 'rb')
    # start by reading in header:    
    ghead=head(f)
    npt=ghead.npart.sum()````
    
This is the function we use to read the files: it set the endianness to "big-endian", open the file in read-only mode, read the header and extract the total number of particles.    
````python
f.seek(4, 1)
    pos=np.fromfile(f, count=npt*3, dtype=bo_mark + 'f4').reshape((npt, 3))
    return pos
````
    
`f.seek(offset, from_what)` move the pointer through the file to read bits from one position to another. The position is computed from adding `offset` to a reference point; the reference point is selected by the `from_what` argument. A `from_what` value of 0 measures from the beginning of the file, 1 uses the current file position, and 2 uses the end of the file as the reference point. `from_what` can be omitted and defaults to 0, using the beginning of the file as the reference point (from the <a href="http://docs.python.org/tutorial/inputoutput.html" title="Python documentation">Python documentation</a>).    
    
This last piece of code read the GIF2 galaxy catalogue (an ASCII file with "space separated values"):    
````python
#! /usr/bin/env python

file = open('lcdm_galaxy_cat.z0.00', 'rb')
i = 0
for riga in file.readlines():
    parole = riga.split()
    if len(parole) == 11:
        print "iterazione ", i 
        print "aggiungo "
        x.append(parole[5])
        y.append(parole[6])
        z.append(parole[7])
    i+=1
````

    