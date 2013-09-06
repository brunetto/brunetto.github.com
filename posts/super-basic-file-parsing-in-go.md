<!-- 
.. link: 
.. description: 
.. tags: golang, go, code
.. date: 2013/09/05 17:26:48
.. title: Super-basic file parsing in Go
.. slug: super-basic-file-parsing-in-go
-->

I want to parse all the files in a folder starting with a certain prefix 
searching for the lines containing a certain string.    


<!--TEASER_END-->

`package main` tells go that this source will be a main file, not a library/module. 
Then, we import the packages we need. If a package is not still needed, go will 
throw an error.    

`//` or `/* */` are, respectively, the one-line and multi-line comments.        


````go
package main

import (
	"bufio" // buffered input/output
	"compress/gzip" // compressed files handling
	"log" // logging
	"os" // OS related utilities
	"time" // timing
	"strings" // strings handling
	"path/filepath" // path handling
	"fmt" // basic printing
)
````        

The main body of the program has to be in the `main` function.
We would also like to know the time needed to execute the program so we use
`tGlob0 := time.Now()` to keep track of the time we launch the program.    
We also print a help message in case the number of arguments provided
do not match the needed ones.... id they are wrong, googd luck!:P        

````go
func main() {
	
	helpMessage :=`Hi! To use this program you must provide
	1 - the path
	2 - the file prefix
	3 - the output file
	4 - the string to be searched.`
	
	if len(os.Args) < 5{
		fmt.Println(helpMessage)
		os.Exit(0)
	}

	tGlob0 := time.Now()
 
````        

Go can create variables in two ways, by declaring them before or by assignement directly.
To have a clearer view of what is going on I will declare the variables before except
for `tGlob0` and `tGlob1`. If you want to know the type of a variable, you can 
create it by assignement and then inspect its type with the reflect package, 
using `reflect.TypeOf(variable)`.        

````go	
	var inPath string
	var prefix string
	var searchString string
	var outFile string
	var inFiles []string
	var inFile string
	var extString []string
	var ext string
	var PID int 
	var (fileStruct *os.File
	fOut *os.File)
	var err error
	var fZip *gzip.Reader
	var nReader *bufio.Reader
	var read_line string
```        

The `os` package provides the tools to interact with the OS, so we can retrieve the process
PID and the CLI arguments.        
	
````go
	PID = os.Getpid()
	log.Println("Process PID is ", PID)	
	
	inPath = os.Args[1]
	prefix = os.Args[2]+"*"
	outFile = os.Args[3]
	searchString = os.Args[4]
	
	log.Println("Parsing files in folder ", inPath, " selecting ", os.Args[2])
````        

The `Glob` function allows to search for the filenames matching a certain 
 wildcard pattern.    
 `defer` is used to mark functions to be executed on function exit.        

````go
	inFiles, err = filepath.Glob(filepath.Join(inPath, prefix))
	if err != nil {
		panic(err)
	}
	
	log.Println("Searching for ", searchString, " in ", filepath.Join(inPath, prefix))
	log.Println("Creating output file ", outFile)
	
	fOut, err = os.Create(outFile)
	if err != nil {
		panic(err)
	}
	defer fOut.Close()
````        

In the following piece of code is possible to see how to     

* work on strings
* write a counter that updates 
* use the switch construct
* make an assignement in the if construct        

````go
	log.Println("Starting main loop on file list of lenght ", len(inFiles))
	for fileIdx := range inFiles {
		
		inFile = inFiles[fileIdx]
		extString = strings.Split(inFile, ".")
		ext = extString[len(extString)-1]

		// Write an updating counter
		fmt.Print("Completed: ", 100. * fileIdx / len(inFiles), "% \r")
		
		// Creating file object
		if fileStruct, err = os.Open(inFile); err != nil {
			log.Fatal(os.Stderr, "%v, Can't open %s: error: %s\n", os.Args[0], inFile, err)
			os.Exit(1)
		}
		defer fileStruct.Close()
		
		switch ext {
			case "dat": {
				nReader = bufio.NewReader(fileStruct)
			}
			case "txt":{
				nReader = bufio.NewReader(fileStruct)
			}
			case "gz": {
				fZip, err = gzip.NewReader(fileStruct)
				if err != nil {
				log.Fatal(os.Stderr, "%v, Can't open %s: error: %s\n", os.Args[0], inFile, err)
				os.Exit(1)
				}
				nReader = bufio.NewReader(fZip)
			}
			default: {
				log.Fatal("Unrecognized file ", inFile)
			}
		}
````        

And yes, no `while` but infinite loops with `for`.    
Then we read the file line by line and write the line if we find a certain 
string inside it.        

````go
		for {
			if read_line, err = nReader.ReadString('\n'); err != nil {
			log.Println("Done reading file with err", err)
			break
			}
// 			if (strings.Contains(read_line, "name =") || strings.Contains(read_line, "i =")) {//&& strings.Contains(read_line, "<"){
				if strings.Contains(read_line, searchString){
				_, err = fOut.WriteString(read_line)
				}
		}
	
		// flush 
		fOut.Sync()
		fOut.Close()
	}
	
	
	log.Println()
	tGlob1 := time.Now()
	log.Println("Wall time for all ", tGlob1.Sub(tGlob0))
}
````