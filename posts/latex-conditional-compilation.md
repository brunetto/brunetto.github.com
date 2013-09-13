<!-- 
.. link: 
.. description: 
.. tags: 
.. date: 2013/09/13 11:24:45
.. title: Latex conditional compilation
.. slug: latex-conditional-compilation
-->

It's a long time I'm looking for a way to conditional-compiling my 
[Beamer](http://en.wikipedia.org/wiki/Beamer_(LaTeX)) presentation in order to 
decide on the fly if I want to print an handout version of the presentation.

<!--TEASER_END-->

Inside the `.tex` file you have to write

````latex
\ifdefined\HANDOUT
  \setbeameroption{show notes} %un-comment to see the notes
  \usepackage{pgfpages}
  \pgfpagesuselayout{8 on 1}[a4paper]%, landscape]
\fi
````
where the `pgfpages` package is used to print 8 slide per page.    
Before this if you want you can put `\newcommand*{\HANDOUT}{}%`
to decide in the source if you want the handout version or not...    
... or you can decide it via command line:
````bash
pdflatex -jobname=handout.pdf  "\def\HANDOUT{}\input{sourcefile.tex}"
````

