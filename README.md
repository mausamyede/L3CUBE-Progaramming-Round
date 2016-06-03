# L3CUBE-Programming-Round
Assignments given by L3CUBE as a part of programming round.

*******************************************************************************************************************************
Assignment no. 1:
Write a code to verify that Birthday paradox is really valid.

Associated code file: bdayparadox.py

Instructions of exuction:
$python bdayparadox.py - on linux terminal

Additional comments: This program performs the experiment to verify bithday paradox n number of times. The consistent values obtained for probablity for any value of "n" proves that the birthday paradox is indeed valid. 

*******************************************************************************************************************************
Assignment no. 2:
Create a simple version control program "svc" which performs version control for a text file.

#Version 1
Associated code file: svc.py

Instruction of execution:
$python svc.py <filename> - to commit changes in a file 
$python svc.py <filename> <version no.> - to display the content of <version no.>th version of the file.

Additional comments: This program is not complete yet. svc.py is the main version control program. Constraints on file operation has not been implemented yet. There exists some confusion within problem statement that needs to be cleared before proceeding. However, this program in its current form works for a text file will all sorts of changes allowed in the file.

#Version 2
Associated code files: fileopes_v2.py, svc_v2.py

Instruction of excution:
Keep both the files in same directory.
$python fileops_v2.py 

Additional comments: This program is another approach for performing version control. This program gives an interface where user can create a file, append a line to it, delete any line from it, commit changes done in it, and also revert the file back to any previous version. File operation constraints are met. Currently, file cannot revert to back to future version after being reverted to past version.

*******************************************************************************************************************************
Assignment no. 3
Write a program to list duplicate files from hard drive.

#Version 1
Associated code file: symlink.py

Instruction of execution:
$python symlink.py

Additional comments: This is just a module of the intended program. This will list all the softlinks present in the volume (hard drive) and provide users with the option to delete them all. Dupicate files may be of more types. Currently working on those.

#Version 2
Associated code file: listdupli.py

Instruction of execution:
$python listdupli.py

Additional comments: This program is capable of listing softlinks, and all files with same content(duplicate) which includes hardlinks. The user can choose to delete the duplicate files and/or softlinks. Only one among the copies of a file will remain after deletion. All softlinks will be deleted.

*******************************************************************************************************************************
Assignment no. 4
Design a simple filesystem called TextFS

#Version 1
Associated code file: textfs.py

Instruction of execution:
$python textfs.py

Additional comments: Not complete yet. This program emulates a command interface for a filesystem where user can create files, list them, and print file contents. The file storage and access is text based which is personally designed. User cannot delete files or copy external file content to internal files in this version.

#Version 2
Associated code file: textfs_v2.py

Instruction of execution:
$python textfs_v2.py

Additional comments: This version supports creating, deleting, listing and printing contents of file. It also supports copying data from external files to internal file.
