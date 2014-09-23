<!-- 
.. title: Change a line in all of your files at once
.. slug: change-a-line-in-all-of-your-files-at-once
.. date: 2014/09/23 10:25:00
.. tags: unix, sed, cli
.. link: 
.. description: 
.. type: text
-->

Sometimes you need to change a single line in a lot of files. May be you made a mistake in your configuration files or you want to change the number of initial conditions to be generated automatically.    
With `sed` it is super-easy:

````bash
sed -i 's/"Runs": 10,/"Runs": 50,/g' *.txt
````