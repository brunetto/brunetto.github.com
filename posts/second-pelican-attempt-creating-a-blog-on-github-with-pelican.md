<!-- 
.. link: 
.. description: 
.. tags: blogging, Python, Pelikan
.. date: 2013-03-08
.. title: Second Pelican attempt: creating a blog on GitHub with Pelican
.. slug: second-pelican-attempt-creating-a-blog-on-github-with-pelican
-->

# How to create a blog with GitHub and Pelican (Python)

###Suppose that you are curios about GitHub pages... but I don't understand their guide.     
###And suppose that you don't like Ruby but prefer Python...    

First of all create a repo named `youname.github.com` on your GitHub account 
(ok, maybe, before this, you have to create a GitHub account!).    
Then set the remote origin locally with    
````bash
    # I use ssh because I can log in without a password saving my key at https://github.com/settings/ssh    
    git remote add origin ssh://git@github.com/yourname/yourname.github.com.git    
````
Now you can follow the excellent guide by [Martin](http://martinbrochhaus.com/2012/02/pelican.html).

Maybe you need to change     

````bash
    mkvirtualenv -p python2.7 blog    
````

with something like     

````bash
    mkvirtualenv -p /usr/bin/python blog    
````

If you need to write equation, use [MathJax](http://www.mathjax.org/) is straightforward.
Following [this post](http://www.ceremade.dauphine.fr/~amic/en/blog/mathjax-and-pelican.html)
you only need to add few lines to the `base.html` of your theme and write latex-style equation like
`$$\frac{x_n}{x_{n+1}}$$` to obtain    

$$\frac{x_n}{x_{n+1}}$$    

If you want to show code you only need to indent it with four spaces and put the 
languade identifier (`:::python`) on the top, indented in the same way (.=space):

````
....:::python    
....def print_python():    
........print "Python:)"    
````

produces

````python
def print_python():
    print "Python:)"
````

Now, if can also blog from the [IPython Notebook](http://ipython.org/notebook.html)
following the [guide by Daniel](http://danielfrg.github.com/blog/2013/03/08/pelican-ipython-notebook-plugin/).    

And That's all Folks!:P

PS: see also [this](http://blog.xlarrakoetxea.org/posts/2012/10/creating-a-blog-with-pelican/) great guide

