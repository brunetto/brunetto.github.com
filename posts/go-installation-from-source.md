<!-- 
.. link: 
.. description: 
.. tags: code, go, golang
.. date: 2013/08/30 16:59:36
.. title: Go installation from source
.. slug: go-installation-from-source
-->

Summary of the Go installation instruction from source as presented in:    

* [Go installation](http://golang.org/doc/install)
* [Go installation from source](http://golang.org/doc/install/source)
* [Write Go code](http://golang.org/doc/code.html)

<!--TEASER_END-->

The installation path will be `/usr/local/go` and the workspace in 
`$HOME/Code/go`

````bash
cd /usr/local
hg clone -u release https://code.google.com/p/go
cd go/src
./all.bash
echo "export PATH=$PATH:/usr/local/go/bin" >> $HOME/.bashrc
echo "export GOPATH=$HOME/Code/go/" >> $HOME/.bashrc
````

