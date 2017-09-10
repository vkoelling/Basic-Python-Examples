# Vanessa Koelling, August 8th, 2017. This document contains some notes and code examples in Python 3 from "Python for Biologists".
# Chapter 3 notes
# these exercises require the dna.txt example file provided with the book

# open and print the contents of file dna.txt
my_file = open("dna.txt")
file_contents = my_file.read()
print(file_contents)

# open the file
my_file = open("dna.txt")
# read the contents
my_dna = my_file.read()
# calculate the length
dna_length = len(my_dna)
# print the output
print("sequence is " + my_dna + " and length is " + str(dna_length))

# open the file
my_file = open("dna.txt")
# read the contents
my_file_contents = my_file.read()
# remove the newline from the end of the file contents
my_dna = my_file_contents.rstrip("\n")
# calculate the length
dna_length = len(my_dna)
# print the output
print("sequence is " + my_dna + " and length is " + str(dna_length))

# alternatively, you can use more than one method on the same variable simultaneously
my_dna = my_file.read().rstrip("\n")

# create a new file and write a single line of text to it
# 'w' = write to a file (this will overwrite a file if it already exists); 'r' = read a file only; 'a' = append to an existing file
my_file = open("out.txt", "w")
my_file.write("Hello world")
# close the file
my_file.close()

# in the above examples, we were in the same working directory as dna.txt
# in most cases, you will not be and will need to specify the path to the file
my_file = open("/Users/vkoelling/Desktop/Python_practice_files/Python_for_Biologists_exercises_and_examples/Chapter_3/examples/dna.txt")
file_contents = my_file.read()
print(file_contents)

