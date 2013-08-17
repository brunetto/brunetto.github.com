<!-- 
.. link: 
.. description: 
.. tags: latex, imported
.. date: 2011-05-13
.. title: Subfile package for latex
.. slug: subfile-package-for-latex
-->

If you have a complex Latex document and you want to split it in several files, the [subfile](http://ctan.org/tex-archive/macros/latex/contrib/subfiles) package can help you.    
The main difference between this and the `\input` or `\import` methods is that with `subfile` you can compile also each file, without need to copy the preamble.    

<!-- TEASER_END -->

What you have to do is to add

````latex
\usepackage{subfiles}
````
in the preamble of the master file and
````latex
\documentclass[tesi.tex]{subfiles}
\begin{document}
...
\end{document}
````
in your subfiles.    
Now you can import your subfiles in the master file with
````latex
\subfile{subfile.tex}
<br />    
Sources:<br />
<ul><br />
<li><a href="http://en.wikibooks.org/wiki/LaTeX/Multiple_files">http://en.wikibooks.org/wiki/LaTeX/Multiple_files</a></li>
<li><a href="https://help.ubuntu.com/community/LaTeX">How to install in Ubuntu</a></li>
</ul>
