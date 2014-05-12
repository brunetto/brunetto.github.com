<!-- 
.. link: 
.. description: 
.. tags: Latex, matplotlib, Python, plot, imported
.. date: 2012-06-01
.. title: Latex together with matplotlib!
.. slug: latex-together-with-matplotlib
-->

Sometimes you need to label your plot with math expression or Greek letters and ASCII is not enough.    
Everything you need is to add to your script    
    
````python
from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
## for Palatino and other serif fonts use:
#rc('font',**{'family':'serif','serif':['Palatino']))
rc('text', usetex=True)
````
    
and write you text label like    
    
````python
label = r'theoretical $f(nu)$')
````



