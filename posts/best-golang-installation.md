<!-- 
.. title: Best Golang installation
.. slug: best-golang-installation
.. date: 2014/06/19 12:46:28
.. tags: 
.. link: 
.. description: 
.. type: text
-->

Best way to install Golang, from:

* [http://blog.labix.org/2013/06/15/in-flight-deb-packages-of-go](http://blog.labix.org/2013/06/15/in-flight-deb-packages-of-go)
* [http://dave.cheney.net/2012/09/08/an-introduction-to-cross-compilation-with-go](http://dave.cheney.net/2012/09/08/an-introduction-to-cross-compilation-with-go)

Assuming you already have the correct environment and you are on an ubuntu workstation.

* Download and install `godeb` if you haven't already done.
* Then with `godeb list` and godeb install <version> install your favourite Go version (the last, obviously!:P).
* To be able to cross-compile with the new installed Go:

````bash 
sudo -i
cd /usr/local/go/src
git clone git://github.com/davecheney/golang-crosscompile.git
source golang-crosscompile/crosscompile.bash
go-crosscompile-build-all
````

done.
