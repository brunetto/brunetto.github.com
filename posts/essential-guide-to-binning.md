<!-- 
.. link: 
.. description: 
.. tags: binning, PhD, Python, histogram, imported
.. date: 2012-05-25
.. title: Essential guide to binning
.. slug: essential-guide-to-binning
-->

Often I found myself fighting against data binning, trying to understand the relation between linear and logarithmic bins and how to create the bin starting from the bins number or the bins spacing.    
It's time to write down some consideration and snippet!    
    
<!-- TEASER_END -->    
    
<strong>Linear vs logarithmic</strong>    
    
I live in a linear space. My advisor and a lot of other scientists live in a logarithmic space. It's quite difficult to easily communicate, but trying to "mask" this difference life can be more peaceful.    
Hereafter I would like to thing about "equally spaced bins". It's not important if they are linearly or logarithmically equally spaced because you can take the same snippet of code and pass to it a logarithmic array, or logarithmic boundaries.    
    
<strong>From one to the other</strong>    
    
Suppose you have an array.  How much will be the bin spacing to obtain `n_bin` bins?     
It can be easily computed as    
$\delta_{bin} = (sup-inf)/n_{bin}$    
From this it's also straightforward to obtain the number of bins from the spacing:    
$n_{bin} = \lfloor(sup-inf)/\delta_{bin}\rfloor$    
Note that we choose the number of bins to be integer.    
    
<strong>Code</strong>    
    
Here some code to bin your arrays:    
    

````python
#!/usr/bin/env python
import sys
import numpy as np

def binning(inf, sup, n_bin=None, delta_bin=None):
	"""Given the inf and sup limits of an array and the number of equally spaced
	bins, it returns the bin centers, the bin limits and the bin spacing.
	It's possible to have a linear or a logarithmic spacing passing linear or
	logarithmic inf and sup, and searchsorting on a linear or logarithmic array, 
	or you can use a linear array and logarithmically spaced bins as
	new_bins = pow(10, logbins)
	"""
	if (n_bin == 0) or (n_bin == 0):
	print "Error, n_bin and/or delta_bin are/is zero, exit!"
	sys.exit()    
	elif (n_bin == None) and (delta_bin != None):
	n_bin = (sup-inf)/delta_bin
	elif (n_bin == None) and (delta_bin == None):
	print "Error, n_bin and delta_bin are both None, exit!"
	sys.exit()
	temp, half_step = np.linspace(inf, sup, 2*n_bin+1, endpoint = True, retstep = True)
	xrange_limit = int(np.floor(temp.size / 2))
	bin_pos = np.zeros(xrange_limit)
	bin_limits = np.zeros(xrange_limit+1)
	for i in xrange(xrange_limit):
	bin_pos[i] = temp[2*i+1]
	bin_limits[i] = temp[2*i]
	bin_limits[-1] = temp[-1]
	del temp
	return [bin_pos, bin_limits, 2*half_step]

def base_binning(inf, sup, n_bin=None, delta_bin=None):
	"""More C-like...
	"""
	if (n_bin == 0) or (n_bin == 0):
	print "Error, n_bin and/or delta_bin are/is zero, exit!"
	sys.exit()    
	elif (n_bin == None) and (delta_bin != None):
	n_bin = int((sup-inf)/(1.*delta_bin))
	elif (n_bin != None) and (delta_bin == None):
	delta_bin = (sup-inf)/(1.*n_bin)
	elif (n_bin == None) and (delta_bin == None):
	print "Error, n_bin and delta_bin are both None, exit!"
	sys.exit()
	bin_pos = np.zeros(n_bin)
	bin_limits = np.zeros(n_bin+1)
	for i in range(n_bin):
	if i%2 == 0:
		bin_limits[i] = inf + i * delta_bin
		bin_limits[i+1] = bin_limits[i] + delta_bin
	bin_pos[i] = bin_limits[i] + delta_bin/2.
	bin_limits[n_bin] = inf + n_bin * delta_bin
	return [bin_pos, bin_limits, delta_bin]
````

