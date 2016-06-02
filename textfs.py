import os
import fileinput

### Currently supports only file creation, listing, and printing file contents. Working on remaining features.

print 'Welcome to textFS'
print '1. create <filename> - Create a new file.'
print '2. delete <filename> - Delete file'
print '3. echo <filename> - Print contents of file'
print '4. ls - List all files'
print '5. cp <srcfile> <destfile> - Copy contents from external file (src) to internal file (dest)'

if os.system('test -e textfs.txt') != 0:	#checking existance of textfs.txt. Create one if it doesnt exist.
	os.system('touch textfs.txt')
	f = open('textfs.txt','a')
	for x in range(5):
		f.write("\n")
	f.close()
num_file = 0
f = open('textfs.txt','r')
for x in range(5):
	line = f.readline()
	if line != "\n":
		num_file=num_file+1
f.close()
print num_file
tot_lines = 0
while True:
	comm = raw_input(">>")
	args = comm.split(' ')
	if args[0] == "create":				#Create a file
		if num_file == 5:			#Max files allowed in file system are 5
			print 'Max file limit reached!'
			continue
		filename = args[1]
		content = []
		print 'Enter contents of file:'
		nxt_line = raw_input()
		while nxt_line!="end":
			content.append(nxt_line)
			nxt_line = raw_input()
		num_lines = len(content)
		fin = open('textfs.txt','r+')
		fout = open('tempfile.txt','a')
		flag=0
		for line in fin:
			if line == "\n" and flag==0:
				fout.write(str(num_file)+":"+filename+":"+str(tot_lines+1+5)+":"+str(num_lines)+"\n")
				num_file=num_file+1
				print num_file
				flag=1
			else:
				fout.write(line)	
		fin.close()
		fout.close()
		os.system('rm textfs.txt')
		os.system('mv tempfile.txt textfs.txt')
		tot_lines = tot_lines+num_lines
		
		f = open('textfs.txt','r+')
		for x in range(5):
			l = f.readline()
		for x in range(tot_lines):
			l = f.readline()
		for x in range(num_lines):
			f.write(content[x]+"\n")
		f.close()
	
	if args[0] == "ls":				#List all files
		if num_file==0:
			print 'No files present'
			continue
		f = open('textfs.txt','r')
		for x in range(num_file):
			line = f.readline()
			filename = line.split(':')[1]
			print filename

	if args[0] == "echo":				#Print contents of the file
		filename = args[1]
		f = open('textfs.txt','r')
		flag=0
		for x in range(num_file):
			line = f.readline()
			if filename == line.split(':')[1]:
				start_line = int(line.split(':')[2])
				nos_line = int(line.split(':')[3])
				flag=1
				break
		if flag==0:
			print 'File not found!'

		f.seek(0,0)
		for x in range(start_line-1):
			line = f.readline()
		for x in range(nos_line):
			line = f.readline()
			print line
		f.close()

	
		

	
