#!/usr/bin/python


#This script only detects and removes softlinks. Other types of duplicate files wont be affected. Currently working on them too. 
 
import os
from os import listdir
import os.path

links = ["" for x in range(1000)]
count=0
def scanvol():
	global links
	global count
	for i in os.listdir(os.getcwd()):
		if os.path.islink(i):
			print i,' in directory: ',os.getcwd()
			print ''
			links[count] = os.getcwd()+"/"+i
			count=count+1
		if os.path.isdir(i):
			os.chdir(i)
			scanvol()
	os.chdir('..')

def purge():
	for x in range(count):
		os.system('rm '+links[x])
		
vol_path = raw_input("Enter the path of the volume to be scanned: ")
os.chdir(vol_path)
print 'Following links are present in the current volume: '
scanvol()

while True:
	choice = raw_input("Do you want to remove these links(Y/n): ")
	if choice == "Y":
		purge()
		break
	elif choice == "n":
		break
