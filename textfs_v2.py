import os
import fileinput

## Fully functional now

print 'Welcome to textFS'
print '1. create <filename> - Create a new file.'
print '2. delete <filename> - Delete file'
print '3. echo <filename> - Print contents of file'
print '4. ls - List all files'
print '5. cp <srcfile> <destfile> - Copy contents from external file (src) to internal file (dest)'
print '6. quit - exit textFS'

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
	if args[0] == "quit":				#exit interface
		break
	if args[0] == "create":				#Create a file
		if len(args) != 2 or args[1]=="":
			print 'Usage: create <filename>'
			continue
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
				fout.write(filename+":"+str(tot_lines+1+5)+":"+str(num_lines)+"\n")
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
		if len(args) != 1:
			print 'Usage: ls'
			continue
		if num_file==0:
			print 'No files present'
			continue
		f = open('textfs.txt','r')
		for x in range(num_file):
			line = f.readline()
			filename = line.split(':')[0]
			print filename

	if args[0] == "echo":				#Print contents of the file
		if len(args) != 2 or args[1]=="":
			print 'Usage: echo <filename>'
			continue
		filename = args[1]
		f = open('textfs.txt','r')
		flag=0
		for x in range(num_file):
			line = f.readline()
			if filename == line.split(':')[0]:
				start_line = int(line.split(':')[1])
				nos_line = int(line.split(':')[2])
				flag=1
				break
		if flag==0:
			print 'File not found!'
			continue
		f.seek(0,0)
		for x in range(start_line-1):
			line = f.readline()
		for x in range(nos_line):
			line = f.readline()
			print line
		f.close()

	if args[0] == "delete":				#Deleting file in textfs
		if len(args) != 2 or args[1]=="":
			print 'Usage: delete <filename>'
			continue
		filename = args[1]
		fin = open('textfs.txt','r')
		flag=0
		for x in range(num_file):
			line = fin.readline()
			if filename == line.split(':')[0]:
				start_line = int(line.split(':')[1])
				nos_line = int(line.split(':')[2])
				flag=1
				break
		if flag==0:
			print 'File not found!'
			continue
		fin.seek(0,0)

		os.system('touch tempfile.txt')
		fout = open('tempfile.txt','a')
		flag=0
		for x in range(5):
			line = fin.readline()
			if line.split(':')[0] == filename:
				flag=1
			if line.split(':')[0] != filename and flag==0:
				fout.write(line)
			if line.split(':')[0] != filename and flag==1:
				if line != "\n":
					n_line = line.split(':')[0]+':'+str(int(line.split(':')[1])-nos_line)+':'+line.split(':')[2]
					fout.write(n_line)
				else:
					fout.write(line)
		fout.write("\n")
		for x in range(start_line-6):
			line = fin.readline()
			fout.write(line)
		for x in range(nos_line):
			line = fin.readline()
		while line != "":
			line = fin.readline()
			fout.write(line)

		fin.close()
		fout.close()
		os.system('rm textfs.txt')
		os.system('mv tempfile.txt textfs.txt')
		num_file=num_file-1
		tot_lines = tot_lines - nos_line

	if args[0] == "cp":					# copy external file to internal file
		if len(args) != 3 or args[1]=="" or args[2]=="":
			print 'Usage: create <src> <dest>'
			continue
		src = args[1]
		dest = args[2]
		fdest = open('textfs.txt','r')
		flag=0
		for x in range(num_file):
			line = fdest.readline()
			if dest == line.split(':')[0]:
				start_line = int(line.split(':')[1])
				nos_line = int(line.split(':')[2])
				flag=1
				break
		if flag==0:
			print 'File not found!'	
			continue
		srccount=0
		fsrc = open(src,'r')
		for line in fsrc:
			srccount = srccount+1
		fsrc.close()
		os.system('touch tempfile.txt')
		ftemp = open('tempfile.txt','a')
		fdest.seek(0,0)
		flag=0
		for x in range(5):
			line = fdest.readline()
			if line.split(':')[0] == dest:
				flag=1
				n_line = line.split(':')[0]+':'+line.split(':')[1]+':'+str(srccount)+'\n'
				ftemp.write(n_line)
			if line.split(':')[0] != dest and flag==0:
				ftemp.write(line)
			if line.split(':')[0] != dest and flag==1:
				if line != "\n":
					n_line = line.split(':')[0]+':'+str(int(line.split(':')[1])-nos_line+srccount)+':'+line.split(':')[2]
					ftemp.write(n_line)
				else:
					ftemp.write(line)
		
		for x in range(start_line-6):
			line = fdest.readline()
			ftemp.write(line)
		for x in range(nos_line):
			line = fdest.readline()
		fsrc = open(src,'r')
		for x in range(srccount):
			line = fsrc.readline()
			ftemp.write(line)
		fsrc.close()
		line = fdest.readline()
		while line != "":
			ftemp.write(line)
			line = fdest.readline()

		fdest.close()
		ftemp.close()
		os.system('rm textfs.txt')
		os.system('mv tempfile.txt textfs.txt')
		tot_lines = tot_lines - nos_line+srccount
		
			
		

	
		

	
