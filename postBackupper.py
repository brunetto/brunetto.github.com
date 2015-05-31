#!/usr/bin/env python
# -*- coding: utf8 -*- 

import time, re
import httplib2
import os
import sys

from string import maketrans
from apiclient import discovery
from oauth2client import file
from oauth2client import client
from oauth2client import tools

def main(argv):
	t0 = time.time()

	storage = file.Storage('../../../../../DCode/G+API/plus-cmd-line-sample/sample.dat')
	credentials = storage.get()
	http = httplib2.Http()
	http = credentials.authorize(http) # vedere se posso fare a meno
	service = discovery.build('plus', 'v1', http=http)

	token = None
	postsNumber = 0
	iteration = 0
	
	mirrorHeader = """<!-- 
.. link: 
.. description: 
.. tags: 
.. date: 2013/09/07 16:57:13
.. title: G+ UpsideDown page mirror
.. slug: blog-mirror
-->
"""
	mirrorFooter = """<!-- Place this tag in your head or just before your close body tag. -->
<script type="text/javascript" src="https://apis.google.com/js/plusone.js"></script>
	"""
	
	backupHeader = """<!-- 
.. link: 
.. description: 
.. tags: 
.. date: 2013/09/07 16:57:13
.. title: G+ UpsideDown page backup
.. slug: blog-backup
-->
"""
	mirrorFile = open("blog-mirror.md", 'w')
	backupFile = open("blog-backup.md", 'w')
	
	mirrorFile.write(mirrorHeader)
	backupFile.write(backupHeader)
	
	dateReg = re.compile("(\d\d\d\d-\d\d-\d\d)")
	urlReg = re.compile('https://plus.google.com/111247854072185245270/posts/(\S+)')

	while True:
		iteration += 1
		print "Iteration number ", iteration
		result = service.activities().list(userId='111247854072185245270', pageToken=token, collection='public', maxResults=20).execute()
		token = result.get("nextPageToken", None)
		posts = result.get('items', [])
		postsNumber += len(posts)
		
		for postIdx in range(len(posts)):
			post = posts[postIdx]
			date = dateReg.search(post["published"]).group(1)
			url = post["url"]
			postUrl = urlReg.search(url).group(1)
			content = post["object"]["content"].replace("$", "dollars").replace("`", r"\`")
			
			mirrorFile.write('<div class="g-post" data-href="https://plus.google.com/111247854072185245270/posts/'+postUrl+'"></div>\n')
			if postIdx%2 == 0:
				mirrorFile.write("<br/> <br/>")
			
			backupFile.write('<div style="border:6px solid black;border-radius: 8px">\n')
			backupFile.write('<div style="border:6px solid white;border-radius: 8px">\n')
			backupFile.write("## [" + date + "](" + url + ")    \n")
			#backupFile.write(content.encode('utf8', 'xmlcharrefreplace')+"\n")
			backupFile.write(content.encode('utf8')+"\n")
			backupFile.write("</div>\n")
			backupFile.write("</div><br/><br/>\n")


		if token is None:
			break
	
	mirrorFile.write(mirrorFooter)
	mirrorFile.flush()
	mirrorFile.close()
	backupFile.flush()
	backupFile.close()
	
	print "Total number of posts ", postsNumber
	print "Total iterations ", iteration
	print "Done in ", time.time()-t0, " seconds."

if __name__ == '__main__':
	main(sys.argv)