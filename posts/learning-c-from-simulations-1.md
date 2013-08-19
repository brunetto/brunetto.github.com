<!-- 
.. link: 
.. description: 
.. tags: astro/physics, C, code, N-body, numerical, PhD, program, simulations, imported
.. date: 2012-02-20
.. title: Learning C from simulations, #1
.. slug: learning-c-from-simulations-1
-->

Coming from the beauty of Python, now I have to learn C/C++ again (after the course some semesters ago!:P) because of my work. I'm doing this working with the simulation code Gadget2 and the ICs (initial conditions) generator N-GenIC. Here I would like to pin the serious and less serious things I'm learning for my and maybe other's usefulness and fun!    

<!-- TEASER_END -->    

<strong>The IDE</strong>    
When I write little pieces of code I usually find <a href="http://kate-editor.org/" target="_blank" title="Kate Editor">Kate</a> comfortable enough but to explore projects like <a href="http://www.mpa-garching.mpg.de/gadget/" target="_blank" title="Gadget2">Gadget2</a> I prefer to use something like <a href="http://kdevelop.org/" target="_blank" title="KDevelop">KDevelop</a> because it's easier to manage where a variable is defined, declared and used. And it do this only by positioning the mouse on the variable name. If you put the mouse on a known function (from the standard library for example), KDevelop will open the documentation for you.    
    
<strong>Doxygen</strong>    
<a href="http://www.stack.nl/~dimitri/doxygen" target="_blank" title="Doxygen">Doxygen</a> is a documentation system. It allows you to produce documentation for a project from the comments in the code. With no additional work you can <a href="http://www.stack.nl/~dimitri/doxygen/docblocks.html#specialblock" target="_blank" title="Comment in Doxigen">comment</a> your code and be ready to produce the documentation. In KDevelop Doxygen style for comments has a different (and nice) coloring.    
    
<strong>Single file compilation</strong>    
I your C program is simple and short, and fit in a single file you can compile it to produce the executable file with    
<pre>gcc -O3 -Wall sort.c -o sort.exe</pre>
    
where `gcc` is the GNU compiler, `-O3` is the level of optimization, `-Wall` activate the print of all the warnings, `sort.c` is your source code file and `-o sort.exe` specify the output file (default is "a.out").    
    
I've also learned some other things, but a good combination of my laziness and the fact that it's not always useful to rewrite things already well-written let me give you the links to those resources!:)    
    
* <a href="http://www.network-theory.co.uk/docs/gccintro/gccintro_16.html" target="_blanck" title="Makefile">Makefile</a>
    
* <a href="http://duramecho.com/ComputerInformation/WhyCPointers.html" target="_blank" title="Why pointers in C">Pointers</a>
    
* <a href="http://www.cprogramming.com/tutorial/cpreprocessor.html" target="_blank" title="Macros">Macros</a>

    
    
Maybe in the next episodes I will understand how to manage <a href="http://www.cplusplus.com/forum/articles/10627/" target="_blank" title="headers">headers</a>, implementations, object files and other funny things!:P
