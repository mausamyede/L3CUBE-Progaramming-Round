#!/usr/bin/python
 
import os
from os import listdir
import os.path
import filecmp

links = []				# contains path of softlinks
allfiles = []				# contains path of all files present in mounted volume
duplifiles = []				# contains path of all duplicate files

def scanvol():				# function to get every file in the mounted volume and getting softlinks seperately
	global links
	global allfiles
	for i in os.listdir(os.getcwd()):
		if os.path.isfile(i):
			allfiles.append(os.getcwd()+"/"+i)
		if os.path.islink(i):
			print i,' in directory: ',os.getcwd()
			print ''
			links.append(os.getcwd()+"/"+i)
		if os.path.isdir(i):
			os.chdir(i)
			scanvol()
	os.chdir('..')

def purge(sometype):			# function to remove all files whose paths are in the list "sometype"
	for x in range(len(sometype)):
		if os.system('test -e '+sometype[x]) == 0:
			os.system('rm '+sometype[x])
			print 'Removed: ',sometype[x]
		
vol_path = raw_input("Enter the path of the volume to be scanned: ")
os.chdir(vol_path)

print 'Following softlinks are present in the current volume: '
scanvol()

i=0
while i<len(allfiles):					# find out files that are copies of other files. Path stored in "duplifiles"
	j=i+1
	while j<len(allfiles):
		if filecmp.cmp(allfiles[i],allfiles[j]):
			flag=0
			for x in range(len(duplifiles)):
				if duplifiles[x] == allfiles[j]:
					flag=1
			if flag==0:
				duplifiles.append(allfiles[j])
		j=j+1
	i=i+1


print 'Following file copies/hardlinks are present in current volume: '
for x in range(len(duplifiles)):
	print 'Duplicate file/hardlink: ',duplifiles[x],'\n'

if len(links)!=0:
	while True:						# Choice to remove all softlinks
		choice = raw_input("Do you want to remove all softlinks links(Y/n): ")
		print choice
		if choice == "Y":
			purge(links)
			break
		if choice == "n":
			break
if len(duplifiles)!=0:
	while True:						# Choice to remove all duplicate files/hardlinks
		choice = raw_input("Do you want to remove all duplicate files(Y/n): ")
		print choice
		if choice == "Y":
			purge(duplifiles)
			break
		if choice == "n":
			break
