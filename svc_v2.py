#!/usr/bin/python

import sys
import os
import re

versiondata = os.system('test -e versiondata.txt') 	# checking if versiondata file exists
if versiondata!=0:				     	# create versiondata file if it doesnt exists
	os.system('touch versiondata.txt')
if len(sys.argv) == 4:				# when version is commited			     
	filename = sys.argv[1]
	mainline = sys.argv[3]
	action = sys.argv[2]
	

	if action == '0':
		if os.stat("versiondata.txt").st_size != 0:
			f = open('versiondata.txt','r')
			first_line = f.readline()
			fields = first_line.split(':')
			new_version = int(fields[1])+1
			f.close()
			f = open('versiondata.txt','r+')
			linetoadd = "Version:"+str(new_version)+":append:"+mainline+"\n"
			content = f.read()
			f.seek(0, 0)
			f.write(linetoadd.rstrip('\r\n') + '\n' + content)
			f.close()
		else:
			print 'hiii'
			f = open('versiondata.txt','r+')
			linetoadd = "Version:1:append:"+mainline+"\n"
			f.write(linetoadd)
			f.close()
	if action != '0':
		f = open('versiondata.txt','r')
		first_line = f.readline()
		fields = first_line.split(':')
		new_version = int(fields[1])+1
		f.close()
		f = open('versiondata.txt','r+')
		linetoadd = "Version:"+str(new_version)+":delete:"+mainline+":"+action+"\n"
		content = f.read()
		f.seek(0, 0)
        	f.write(linetoadd.rstrip('\r\n') + '\n' + content)
		f.close()

if len(sys.argv) == 3:						# reverting to previous versions by reversing changes done in each version
	version = sys.argv[2]
	filename = sys.argv[1]
	f = open('versiondata.txt','r')
	line = f.readline()
	fields = line.split(':')
	curr_ver = int(fields[1])
	if int(curr_ver) > int(version):
		while int(curr_ver) > int(version):
			if fields[2] == "append":
				fd = open(filename,'r')
				lines = fd.readlines()
				fd.close()
				os.system('touch tempfile.txt')
				fd = open('tempfile.txt','w')
				fd.writelines([item for item in lines[:-1]])
				fd.close()
				os.system('rm '+filename)
				os.system('mv tempfile.txt '+filename)
				print 'Deleting line...'

			if fields[2] == "delete":
				deletedline = fields[3]
				line_no = fields[4]
				os.system('touch tempfile.txt')
				fd2 = open('tempfile.txt','a')
				i=0
				with open(filename,'rU') as fd1:
					for line in fd1:
						i=i+1
				x=1	
				print i
				fd1 = open(filename,'r')
				while x <= int(i)+1:
					if x == int(line_no):
						fd2.write(deletedline+"\n")
					else:
						l = fd1.readline()
						fd2.write(l)	
					x=x+1				
				fd1.close()
				fd2.close()
				os.system('rm '+filename)
				os.system('mv tempfile.txt '+filename)	
				print 'Adding line...'

			curr_ver = int(curr_ver)-1
			line = f.readline()
			fields = line.split(':')
			
			
