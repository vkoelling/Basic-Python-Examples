# Vanessa Koelling, August 7th, 2017. This document contains some notes and code examples in Python 3 from "Python for Biologists".

# Chapter 1 & 2 notes

# print is a function that will output whatever is in parentheses after it
# functions are followed by parentheses containing their arguments
# strings are text characters and must be enclosed in quotation marks to be properly identified; otherwise mistaken for an argument

# print a friendly greeting
print("Hello World")

# how to include a new line in the middle of a string
print("Hello\nWorld")

# store a short DNA sequence in the variable my_dna
my_dna = "ATGCGTA"
print(my_dna)
# change the value of my_dna
my_dna = "TGGTCCA"

# concatenate two strings
my_dna = "AATT" + "GGCC"
print(my_dna)
upstream = "AAA"
downstream = "GGG"
my_dna = upstream + "ATGC" + downstream
print(my_dna)

# the len function returns the length of a string; len returns an integer
dna_length = len("ATGC")
print(dna_length)

# store the DNA sequence in a variable
my_dna = "ATGCGAGT"
# calculate the length of the sequence and store it in a variable
dna_length = len(my_dna)
# print a message telling us the DNA sequence length
print("The length of the DNA sequence is " + str(dna_length)) 
# you can only concatenate two strings so the integer, dna_length, must be converted to a string

my_dna = "ATGC"
# print my_dna in lower case
print(my_dna.lower())
# lower is a method of the string type; methods can only be used on their type
# lower does not change the original variable; it returns a copy of the variable in lower case
# store a new lower case version of my_dna
my_dna_lower = my_dna.lower()
print(my_dna_lower)
# note that upper is also a method of type string

protein_seq = "vlspadktnv"
# replace valine with tyrosine
print(protein_seq.replace("v", "y"))
# we can replace more than one character
print(protein_seq.replace("vls", "ymt"))
# the original variable is not affected
print(protein_seq)

# take a slice or substring
protein_seq = "vlspadktnv"
# print positions three to five
print(protein_seq[3:5])
# positions start at zero, not one
print(protein_seq[0:6])
# if we use a stop position beyond the end, it's the same as using the end
print(protein_seq[0:60])
# a single number in the square brackets gives a single character
first_residue = protein_seq[0]
# count amino acid residues
valine_count = protein_seq.count('v')
lsp_count = protein_seq.count('lsp')
tryptophan_count = protein_seq.count('w')
# count is a method of type string; it counts the number of times a substring or pattern occurs in a string
# now print the counts
print("valines: " + str(valine_count))
print("lsp: " + str(lsp_count))
print("tryptophans: " + str(tryptophan_count))

# the find method takes a single string argument and returns the index of where the substring first appears
# this is the simple way to find the start position of a pattern of interest
print(str(protein_seq.find('p')))
print(str(protein_seq.find('kt')))
print(str(protein_seq.find('w')))
# 'w' does not exist in the string, so find returns -1


