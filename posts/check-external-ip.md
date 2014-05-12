<!-- 
.. link: 
.. description: 
.. tags: go, golang, Python, netword, ip
.. date: 2013/09/03 16:59:56
.. title: Check external ip
.. slug: check-external-ip
-->

This is the first attempt to check the external ip of a linux box. 
This means, for example, the public ip address of our modem if we are connected
to the home Wi-Fi.    
I will try to do this in Python and Go. Of course these are raw attempts.
    
<!--TEASER_END-->
    
### Python

````python
#!/usr/bin/env python
import re, os, time

# In internet they say that
# ^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$
# is better but I find this useful

print "Check external ip"
print "This script need curl and the Python modules re, os and time"

# Compile regex
reg = re.compile('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')

# Query until stop, hoping the site won't stop us
while True:
	# Ask the site for ip
	string = os.popen("curl -s 'http://checkip.dyndns.org'").read()
	res = reg.search(string)
	if res == None:
		print "Error, ip not found, continue, ..."
	else:
		print ip
		ip = res.group(0)
		# Recreate the ip file and write the ip
		ipFile = open("ip.dat", 'w')
		ipFile.write(ip)
		ipFile.flush()
		ipFile.close()
	# Wait
	time.sleep(5)
````
    
         
### Go

````go
package main

import (
	//"io/ioutil"
    "os"
    "log"
    "fmt"
    "time"
    "os/exec"
    "regexp"
)

// check the errors
func check(e error) {
    if e != nil {
        panic(e)
    }
}

func main() {

	// set ip download command
	
	command := "/usr/bin/curl"
	args := "http://checkip.dyndns.org"
	
	// compile regexp
	var digitsRegexp = regexp.MustCompile(`\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}`)
	
	// infinite loop to update the ip
    for ;;{
		// download ip string
		out, err := exec.Command(command, args).Output()
		if err != nil {
			log.Fatal(err)
		}
		
		// out is a binary buffer, convert into string
		ipString := string(out)
		
		// search for ip
		ipRes := digitsRegexp.FindString(ipString)
		fmt.Println(ipRes)
		
		// convert string to byte (found a better method)
		//ipByte := []byte(ipRes)
		//ioutil.WriteFile("ip.dat", ipByte, 0644)
		
		// create a file, it implements the Writer interface
		f, err := os.Create("ip.dat")
		
		// check for errors
		check(err)
		
		// close file before exit in case of problems
		defer f.Close()
		
		// write the string, discard (_) the number of bytes written
		_, err = f.WriteString(ipRes)
		// flush 
		f.Sync()
		f.Close()
		// wait
		time.Sleep(5 * time.Second)
    }
}

````



