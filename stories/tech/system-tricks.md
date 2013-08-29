<!-- 
.. link: 
.. description: 
.. tags: 
.. date: 2013/08/22 12:18:45
.. title: System tricks
.. slug: system-tricks
-->

## System

Now I'm working on a Ubuntu 12.04 LTS Dell workstation (it has been 13.04 for a while)
 and a Ubuntu 13.04 Dell Laptop.    
See [here](system.html) for a list of installed packages and settings.

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

## Goodies

* visualize git history `gource ./ -o /dev/null`
* grab an image from the webcam with CLI VLC
````bash
cvlc -I dummy v4l2:///dev/video1 --video-filter scene --no-audio --scene-path 
/home/ziosi/Pictures/webcam --scene-prefix img$(date '+%y%m%d%h%m%s') 
--scene-format png vlc://quit --run-time=1
````