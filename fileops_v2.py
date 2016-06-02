#!/usr/bin/python

import os

print '1. new - Create a new file.'
print '2. append - Append a new line to the file.'
print '3. del - Delete a line from the file.'
print '4. disp - Display the file contents.'
print '5. commit - commit the file as a new version.'
print '6. revert - revert the file back to older version.'
print '7. quit - end the session.'
linesinfile=0
append=0
delete=0
mainline=""
filename=""
while True:
	print 'Enter command:'
	comm = raw_input("")
	if comm == "new":
		filename = raw_input("Enter filename:")
		os.system('touch '+filename)
		print filename,' created!'
	if comm == "append":
		if linesinfile == 20:
			print "No more appending allowed!"
			continue
		#f = raw_input("Enter filename:")
		line = raw_input("Enter line to append:")
		if len(line)>10:
			print "No more that 10 chars per line allowed!"
			break
		fd = open(filename,'a')
		fd.write(line+'\n')
		print 'Line appended in file ',filename
		fd.close()
		append=1
		delete=0
		mainline=line
		linesinfile=linesinfile+1
	if comm == "del":
		if linesinfile == 0:
			print "Cant delete anymore!"
			continue
		#f = raw_input("Enter filename:")
		line_no = raw_input("Enter line no. to delete:")
		fd = open(filename,'r')
		lines = fd.readlines()
		fd.close()
		fd = open(filename,'w')
		i=0
		for line in lines:
			i=i+1
			if i != int(line_no):
				fd.write(line)	
			else:
				mainline=line		
		fd.close()
		delete=1
		append=0
		linesinfile=linesinfile-1
	if comm == "disp":
		#f = raw_input("Enter filename:")
		os.system('cat '+filename)
	
	if comm == "commit":
		#f = raw_input("Enter filename:")
		if append==1:
			os.system('python svc_v2.py '+filename+' 0 '+mainline)
		if delete==1:
			os.system('python svc_v2.py '+filename+' '+line_no+' '+mainline)
			
		print 'File commited!'
	
	if comm == "revert":
		#f = raw_input("Enter filename:")
		ver = raw_input("Enter file version:")
		os.system('python svc_v2.py '+filename+' '+ver)
		 
	if comm == "quit":
		break
