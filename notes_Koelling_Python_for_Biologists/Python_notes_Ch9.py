# Vanessa Koelling, August 14th, 2017. This document contains some notes and code examples in Python 3 from "Python for Biologists".
# Chapter 9 notes

import os # short for operating systems
import shutil # short for SHell UTILities
# these modules take care of differences between operating systems and provide useful functions for file manipulation

# rename an existing file
os.rename("old.txt", "new.txt")
# if the file is not in your working directory, you will need to give the path to the file

# move a file to a different folder
os.rename("/home/martin/biology/old.txt", "/home/martin/python/old.txt")
# you can also rename and move at the same time
os.rename("/home/martin/biology/old.txt", "/home/martin/python/new.txt")
# you can also rename folders
os.rename("/home/martin/biology/old_folder", "/home/martin/biology/new_folder")
# create a new folder (i.e., a directory)
os.mkdir("/home/martin/python")
# make multiple directories simultaneously
os.mkdirs("/a/long/path/with/lots/of/folders")

# copy a single file
shutil.copy("/home/martin/original.txt", "/home/martin/copy.txt")
# copy a folder
shutil.copytree("/home/martin/original_folder", "/home/martin/copy_folder")

# test whether or not a file or folder exists
if os.path.exists("/home/martin/email.txt"):
	print("You have mail!")
	
# delete a single file
os.remove("/home/martin/unwanted_file.txt")
# delete an EMPTY folder
os.rmdir("/home/martin/empty")
# delete a folder and all the files in it
shutil.rmtree("/home/martin/full")

# return a list of all of the files and folders in the current working directory
for file_name in os.listdir("."):
	print("one file name is " + file_name)
# list the contents of a different folder
for file_name in os.listdir("/home/martin"):
	print("one file name is " + file_name)

# run an external program
import subprocess
subprocess.call("/bin/date")
# this prints the output of the Linux date program

# to supply command-line options to the external program, set them in the string and set the optional shell argument to True
subprocess.call("/bin/date +%B", shell=True)
# this only prints the month from the Linux date program

# run an external program and then store the output in a variable
current_month = subprocess.check_output("/bin/date +%B", shell=True)
# note you will probably need to strip newline characters from the output

# interactive user input

# the input function takes a single string argument, which is the prompt to be displayed to the user, and returns the value typed in as a string
accession = input("Enter the accession name")
# do something with the accession variable
# if the string needs to be used as something else, e.g. a number, it will have to be converted
# the string will also end with a newline character (use rstrip to remove)

# command line arguments
# example: myprogram one two three; myprogram is the script you want to execute; one, two, three, are the command line arguments
import sys # the sys module must be imported to use command line arguments
print(sys.argv) # sys.argv is a special list: ['myprogram', 'one', 'two', 'three'] of the program name and the command line arguments
# the first command line argument is at index 1, second at index 2, etc. because the program name is always index 0
# note that the command line arguments are stored as strings, so if they need to be used as another data type, you will need to convert it
