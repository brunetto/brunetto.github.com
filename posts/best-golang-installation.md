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

If you need a non-root installation or want to do everything from scratch it is 
just easy as:

```bash
git clone https://go.googlesource.com/go
cd go
git checkout go1.4.1 # or the latest release
cd src
./all.bash
git clone git://github.com/davecheney/golang-crosscompile.git
source golang-crosscompile/crosscompile.bash
go-crosscompile-build-all
cd ../../
mv go goroot
mkdir -p gopath/bin
mkdir -p gopath/docs
mkdir -p gopath/pkg
mkdir -p gopath/src/github.com/$USER # here you will put your github project sources
echo "export GOROOT=/home/$USER/goroot" >> ~/.bashrc
echo "export GOPATH=/home/$USER/gopath" >> ~/.bashrc
echo "export PATH=$PATH:$GOROOT/bin:$GOPATH/bin" >> ~/.bashrc
```



