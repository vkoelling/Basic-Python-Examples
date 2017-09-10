# Vanessa Koelling, August 8th, 2017. This document contains some notes and code examples in Python 3 from "Python for Biologists".
# Chapter 4 notes

# creating lists and retrieving elements

# create a list called apes
apes = ["Homo sapiens", "Pan troglodytes", "Gorilla gorilla"]
# create a list called conserved_sites
conserved_sites = [24, 56, 132]
# print the first index of the list apes
print(apes[0])
# set first_site as the third (and last) element of the list conserved_sites
first_site = conserved_sites[2]
chimp_index = apes.index("Pan troglodytes")
print(chimp_index)
# chimp_index is now 1
# get the last element of the list apes
last_ape = apes[-1]
# create a list called ranks
ranks = ["kingdom", "phylum", "class", "order", "family"]
# index a subset of the list (positions 2, 3, 4 or class, order, family)
lower_ranks = ranks[2:5]
# the len function can tell you the length of a list
print("There are " + str(len(apes)) + " apes")
# append another element to the list apes
apes.append("Pan paniscus")
print("Now there are " + str(len(apes)) + " apes")
# two lists can be concatenated
monkeys = ["Papio ursinus", "Macaca mulatta"]
primates = apes + monkeys
print(primates)
print(str(len(apes)) + " apes")
print(str(len(monkeys)) + " monkeys")
print(str(len(primates)) + " primates")
# the extend method adds elements in a list onto an existing list; it takes a list as its argument
primates.extend(conserved_sites)
print(primates)
# the reverse method will reverse order the elements of a list
ranks.reverse()
print("after reversing: " + str(ranks))
# the sort method sorts strings in alphabetical order and numbers in ascending order
ranks.sort()
print("after sorting: " + str(ranks))

# writing a loop

apes = ["Homo sapiens", "Pan troglodytes", "Gorilla gorilla"]
# for each element in the list of apes, print out the element, followed by the words 'is an ape'
for ape in apes:
	name_length = len(ape)
	first_letter = ape[0]
	print(ape + " is an ape. Its name starts with " + first_letter + ".")
	print("Its name has " + str(name_length) + " letters.")
	
# iterate over a string
name = "martin"
for character in name:
	print("one character is " + character)
	
# split a string to make a list
# the method split takes the delimiter as the argument
names = "melanogaster, simulans, yakuba, ananassae"
species = names.split(",")
print(str(species))

# iterating over lines in a file
# file = open("some_input.txt")
# for line in file:
	 # do something with the line

# range is a function that generates lists of numbers that can be looped over
# with a single argument, range will count up from zero to that number, excluding the number itself
for number in range(6):
	print(number)

# with two arguments, range will count up from the first number, excluding the second number
for number in range(3, 8):
	print(number)

# with three arguments, range will count up from the first number, excluding the second number, in increments of the third number
for number in range(2, 14, 4):
	print(number)



	
	


