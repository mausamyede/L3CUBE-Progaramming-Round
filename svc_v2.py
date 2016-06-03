#!/usr/bin/python

import sys
import os
import re

versiondata = os.system('test -e versiondata.txt') 	# checking if versiondata file exists
if versiondata!=0:				     	# create versiondata file if it doesnt exists
	os.system('touch versiondata.txt')
	f=open('versiondata.txt','a')
	f.write("Curr_ver:0\n")
	f.close()
if len(sys.argv) == 4:				# when version is commited			     
	filename = sys.argv[1]
	mainline = sys.argv[3]
	action = sys.argv[2]
	

	if action == '0':
		fin = open('versiondata.txt','r')
		first_line = fin.readline()
		fields = first_line.split(':')
		new_version = int(fields[1])+1
		fout = open('tempfile.txt','a')
		first_line = "Curr_ver:"+str(new_version)+"\n"
		fout.write(first_line)
		line = fin.readline()
		while line != "":
			fout.write(line)
			line = fin.readline()
		linetoadd = "Version:"+str(new_version)+":append:"+mainline+"\n"
		fout.write(linetoadd)
		fin.close()
		fout.close()
		os.system('rm versiondata.txt')
		os.system('mv tempfile.txt versiondata.txt')
	if action != '0':
		fin = open('versiondata.txt','r')
		first_line = fin.readline()
		fields = first_line.split(':')
		new_version = int(fields[1])+1
		fout = open('tempfile.txt','a')
		first_line = "Curr_ver:"+str(new_version)+"\n"
		fout.write(first_line)
		line = fin.readline()
		while line != "":
			fout.write(line)
			line = fin.readline()
		linetoadd = "Version:"+str(new_version)+":delete:"+mainline+":"+action+"\n"
		fout.write(linetoadd)
		fin.close()
		fout.close()
		os.system('rm versiondata.txt')
		os.system('mv tempfile.txt versiondata.txt')

if len(sys.argv) == 3:						# reverting to previous versions by reversing changes done in each version
	version = sys.argv[2]
	filename = sys.argv[1]
	f = open('versiondata.txt','r')
	line = f.readline()
	fields = line.split(':')
	curr_ver = int(fields[1])
	f.close()
	if int(curr_ver) == int(version):
		print "Already in same version!"
	if int(curr_ver) > int(version):
		for line in reversed(open("versiondata.txt").readlines()):
			fields = line.split(':')
			if fields[0] == "Curr_ver":
				break
			if int(fields[1]) <= int(curr_ver) and int(fields[1]) > int(version):
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
		fin = open('versiondata.txt','r')
		fout = open('tempfile.txt','a')
		for line in fin:
			if line.split(':')[0]=="Curr_ver":
				nline = "Curr_ver:"+str(version)+"\n"
				fout.write(nline)
			else:
				fout.write(line)
		fin.close()
		fout.close()
		os.system('rm versiondata.txt')
		os.system('mv tempfile.txt versiondata.txt')

	if int(curr_ver) < int(version):
		f = open('versiondata.txt','r')
		line = f.readline()
		line = f.readline()
		while line != "":
			fields = line.split(':')
			if int(fields[1]) > int(curr_ver) and int(fields[1]) <= int(version):
				if fields[2] == "append":
					linetoadd = fields[3]
					fd = open(filename,'a')
					fd.write(linetoadd)
					print 'Adding line...'

				if fields[2] == "delete":
					line_no = fields[4]
					fd2 = open('tempfile.txt','a')
					fd1 = open(filename,'r')
					i=0
					for line in fd1:
						i=i+1
						if i != int(line_no):
							fd2.write(line) 	
					fd1.close()
					fd2.close()
					os.system('rm '+filename)
					os.system('mv tempfile.txt '+filename)	
					print 'Deleting line...'
			line = f.readline()
		fin = open('versiondata.txt','r')
		fout = open('tempfile.txt','a')
		for line in fin:
			if line.split(':')[0]=="Curr_ver":
				nline = "Curr_ver:"+str(version)+"\n"
				fout.write(nline)
			else:
				fout.write(line)
		fin.close()
		fout.close()
		os.system('rm versiondata.txt')
		os.system('mv tempfile.txt versiondata.txt')

	
		
			
