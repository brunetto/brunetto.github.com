<!-- 
.. link: 
.. description: 
.. tags: 
.. date: 2013/08/22 12:18:45
.. title: System tricks
.. slug: system-tricks
-->

## Searching

* `grep -H '<string>' *.<ext>`
* `grep -r "<strings>" ./`
* `sudo updatedb && locate <nomefile>`

## Download

* download music from youtube
````bash
youtube-dl --extract-audio --audio-format=mp3 <youtubeLink>
````
for example:    
````python
#!/usr/bin/env python
# -*- coding: utf8 -*- 

import os, time
tt = time.time()
inFileName = "videos.dat"
inFile = open(inFileName, 'r')

print "Start video download loop"
print "Serial version, parallel is work in progress!:P"
for line in inFile:
	name, video = line.split(',')
	print "========================================"
	#print "Downloading ", name
	print "========================================"
	downloadCmd = 'youtube-dl --extract-audio --audio-format=mp3 '+ videos
	
	#downloadCmd = 'youtube-dl -o ./videos/'+name+'.flv "'+video+'"'
	#os.system(downloadCmd)
	#print "Converting to mp3..."
	#convertCommand = 'avconv -i ./videos/'+name+'.flv ./mp3/'+name+'.mp3'
	#os.system(convertCommand)
print "Done in ", time.time()-tt
````