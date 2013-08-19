<!-- 
.. link: 
.. description: 
.. tags: asterisk, Computer, function, PhD, Python, imported
.. date: 2012-05-07
.. title: Asterisks and Python
.. slug: asterisks-and-python
-->

There are many possible uses of the "*" in Python, to be not confused, this is a brief summary of them.    
<!-- TEASER_END -->    
<strong>Math</strong>    
As usual, one asterisk means multiplication, two asterisks mean power with integer index:    

````python
2*3 = 6
2**3 = 8
````
<strong>Functions</strong>    
In functions declarations "a parameter preceded by * in the parameter list for a function will result in any extra positional parameters being aggregated into a tuple [...] and likewise in Python a parameter preceded by ** will result in any extra keyword parameters being aggregated into a dictionary." (from <a href="http://en.wikipedia.org/wiki/Asterisk#Programming_languages" target="_blank">Wikipedia</a>). In a function call the asterisk before a (list or tuple) parameter expand it as the arguments of that function. You can find some examples <a href="http://www.saltycrane.com/blog/2008/01/how-to-use-args-and-kwargs-in-python/" target="_blank">here</a>.    
Just to give a little example, consider this:    

````python
In: def pippo(\*args):
		for i in args:
		print i
In: pippo(1,2,3,4)
Out:
1
2
3
4

In: def pippo(a, b, c):
		print a,b,c
In: pluto = [1,2,3]
In: pippo(*pluto)
Out:
1 2 3
````