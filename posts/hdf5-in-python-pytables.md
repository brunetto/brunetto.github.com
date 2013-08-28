<!-- 
.. link: 
.. description: 
.. tags: code, Python, HDF5, storage, PyTables, imported
.. date: 2012-05-25
.. title: HDF5 in Python: PyTables
.. slug: hdf5-in-python-pytables
-->

<a href="http://www.hdfgroup.org/HDF5/" target="_blank" title="HDF5 Group homepage">HDF5</a> is a wonderful file format you can use to put into tons of data with easy, without the need to think about endianess, binary formats and so on.    
Pytables is an extremely optimized library built on top of HDF5 capabilities to make even simpler the use of this type of file.    
It's also possible to navigate into a file graphically with <a href="http://vitables.org/" target="_blank" title="ViTables homepage">ViTables</a>.    
Here I would like to present some of the features I use more often.    
<!--TEASER_END-->    
Open, flush and close a file    
    

````python
import tables as tb

h5 = tb.openfile("filename.h5", 'r')
...
h5.flush()
h5.close()
````

where `'r'` means "open the file in read-only mode". It's also possible to open it as `'w'` (create a new file: it overwrites the file if it still exists) and `'a'` (append: create if it does not exist, if it exists, read and modify it).    
    
Create a group to contain some data    

````python
group = h5.createGroup(h5.root, "group")
````

where `h5.root` is the location of the new object created (where we want to create the group) and can also be passe as string ("/") and `"group"` is the string with the name.    
    
Store an array    

````python
a = np.array([....])
array = h5.createArray(h5.root.group, 'name', array_to_store, 'title')
array = h5.createArray("/group", 'name', array_to_store, 'title')
````
    
Create a table (from [Create, recreate and remove duplicates in array manipulation, obviously in Python!:)](create-recreate-and-remove-duplicates-in-array-manipulation-obviously-in-python.html) or [From .csv to HDF5 in Python](from-csv-to-hdf5-in-python.html)    

````python
f = open("filename.csv", 'r')
line = f.readline()
values = np.genfromtxt(StringIO(line), dtype=([('column_1', 'i8'), ('column_2', 'f4'), ('column_3', 'f4')]), delimiter=',')
values.shape = 1

# or in an equivalent way, if the file dimensions permit to lad the entire file:
# values = np.genfromtxt("filename.csv", dtype=([('column_1', 'i8'), ('column_2', 'f4'), ('column_3', # 'f4')]), delimiter=',')

h5 = tb.openFile('filename.h5', 'w')
table = h5.createTable(h5.root, description=values, name='table_name', title="table_description", expectedrows=12158536)
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
    
It's also possible to walk all the nodes under a group:    
    

````python
for i in h5.walkNodes(h5.root.group):
	print i
````
    
and to delete a node/array/table:    
    

````python
h5.removeNode(h5.root.group, 'name')
````
    
All the nodes are available through their path:    

````python
h5.getNode("/group", "name")
h5.root.group.name
````

to read a table or an array, you can use the function `read()`    

````python
h5.getNode("/group", "name").read()
h5.root.group.name.read()
````





