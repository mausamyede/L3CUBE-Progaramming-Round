#!/usr/bin/python

import sys
import os
import re

metadata = os.system('test -e metadata.txt') 	# checking if metadata file exists
if metadata!=0:				     	# create metadata file if it doesnt exists along with a versions folder
	os.system('touch metadata.txt')
	os.system('mkdir versions')	     	# versions is a directory that stores the backup of all commited versions

if len(sys.argv) == 2:				# when version is commited			     
	filefound=0
	filename = sys.argv[1]
	
	os.system('touch tempfile.txt')
	with open('tempfile.txt','wt') as outputfile:					# updating metadata to latest version information
		with open('metadata.txt','r') as inputfile:
			for line in inputfile:
				if re.search(filename,line):
					filefound=1
					latest_version = int(line.split(':')[1])
					new_version = latest_version+1
					newstr = filename+" :"+str(new_version)+":\n"
					outputfile.write(newstr)
					command = 'cp '+filename+' ./versions/'+filename+str(new_version)
					os.system(command)
				else:
					outputfile.write(line)

	inputfile.close()
	outputfile.close()
	os.system('rm metadata.txt')
	os.system('mv tempfile.txt metadata.txt')

	
	if filefound==0:
		f=open('metadata.txt','a')
		f.write(filename+" :1"+":\n")
		command = 'cp '+filename+' ./versions/'+filename+str(1)
		os.system(command)
		f.close()

if len(sys.argv) == 3:									# displaying contents of previous versions
	version = sys.argv[2]
	filename = sys.argv[1]
	command = 'cat ./versions/'+filename+version
	os.system(command)
