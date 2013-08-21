<!-- 
.. link: 
.. description: 
.. tags: array, code, PhD, pytables, Python, imported
.. date: 2012-05-14
.. title: Create, recreate and remove duplicates in array manipulation, obviously in Python!:)
.. slug: create-recreate-and-remove-duplicates-in-array-manipulation-obviously-in-python
-->

I would like to "pin" here a pair of quick solution to everyday problems I encounter manipulating arrays.    

<!-- TEASER_END -->    

<strong>Create</strong>    
    
First, the creation of a structured array (an array composed of records made by different data types) array from a file too big to be read at once with `np.genfromtxt`. The new array will be stored in an HDF5 file, so this is a conversion from .csv to .h5 file.    
    

````python
import numpy as np
import tables as tb
from StringIO import StringIO

f = open("filename.csv", 'r')
line = f.readline()
values = np.genfromtxt(StringIO(line), dtype=([('column_1', 'i8'), ('column_2', 'f4'), ('column_3', 'f4')]), delimiter=',')
values.shape = 1
h5 = tb.openFile('filename.h5', 'w')
table = h5.createTable(h5.root, description=values, name=table_name', title="table_description", expectedrows=12158536)
table.flush()

for line in f:
	values = np.genfromtxt(StringIO(line), dtype=([('column_1', 'i8'), ('column_2', 'f4'), ('column_3', 'f4')]), delimiter=',')
	values.shape = 1
	table.append(values)
	
table.flush()
h5.flush()
h5.close()
f.close()
````
    
The use of `StringIO` is necessary to convert the string containing the line read in a "I/O" object that `np.genfromtxt` can eat.    
    
<strong>Remove duplicates</strong>    
Consider the previous file, if there are duplicates row, `np.unique` can help in removing them. Note that we use the first column to identify the duplicates and that the result will be sorted respect to this column.    

````python
new_indexes = np.unique(table['column_1'], return_index=True, return_inverse=False)[1]
new_array = np.transpose(table[new_indexes])
````
    
In general, `numpy.unique(array, return_index=True, return_inverse=True)`    
returns an array sorted and without duplicates, the indexes of the original array to create the new array and the indexes of the new one to recreate the old one:    
    

````python
In: a = np.array([5,3,3,7,2,9,1])
In: np.unique(a, return_index=True, return_inverse=True)
Out: 
(array([1, 2, 3, 5, 7, 9]),
	array([6, 4, 1, 0, 3, 5]),
	array([3, 2, 2, 4, 1, 5, 0]))
````

<strong>Recreate</strong>    
    
Sometimes it's useful to split a structured array in different arrays, manipulate them and recreate the structured array, or maybe you need to create a structured array from different arrays to fill a Pytables table.     
To do this a possible solution is:    

````python
values = np.array(zip([column_1[0]], [column_2[0]]))
print "Creating table..."
table = h5.createTable(h5.root, description=values, name='fof_data_snap67', title="fof_data_snap67", expectedrows=11697806)

for i in xrange(1, fof.size):
	values = np.array(zip([column_1[i]], [column_2[i]]))
	table.append(values)

table.flush()
h5.flush()
h5.close()
````

It's also possible to zip the entire arrays if they fit into memory:    

````python
values = np.array(zip(column_1, column_2))
````
