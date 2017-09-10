# Vanessa Koelling, August 14th, 2017. This document contains some notes and code examples in Python 3 from "Python for Biologists".
# Chapter 8 notes

# dictionaries: storing paired data

# paired data is referred to as key-value pairs
# examples:
# key	value
# trinucleotide	count
# name	protein sequence
# name	restriction enzyme motif
# codon	amino acid residue
# name	email address
# sample	coordinates
# word	definition

# we call the means to store this type of data a dictionary, after the real-world example that already does this with words and their definitions!

# a dictionary is designated by curly brackets
# dictionary of restriction enzymes and their recognition sites
enzymes = {'EcoRI':r'GAATTC', 'AvaII':r'GG(A|T)CC', 'BisI':r'GC[ATGC]GC'}
print(enzymes['BisI'])

# the only data types that can be used as keys are strings and numbers
# file objects cannot be used as keys
# keys must be unique; multiple values cannot be stored for the same key

# create empty dictionary and add elements to it
enzymes = {}
enzymes['EcoRI'] = r'GAATTC'
enzymes['AvaII'] = r'GG(A|T)CC'
enzymes['BisI'] = r'GC[ATGC]GC'
print(enzymes)

# remove the EcoRI enzyme from the dict enzymes using the pop method
enzymes.pop('EcoRI')
print(enzymes)

# create a dictionary of trinucleotide counts
dna = "AATGATCGATCGTACGCTGA"
counts = {}
for base1 in ['A', 'T', 'G', 'C']:
	for base2 in ['A', 'T', 'G', 'C']:
		for base3 in ['A', 'T', 'G', 'C']:
			trinucleotide = base1 + base2 + base3
			count = dna.count(trinucleotide)
			if count > 0:
				counts[trinucleotide] = count # this adds the trinucleotide (key) and its count (value) to the dictionary

print(counts)
print(counts['TGA'])
# print(counts['AAA']) will return a KeyError because trinucleotides with counts of zero have been excluded from the dictionary
# one way to fix this:
if 'AAA' in counts:
	print(counts['AAA'])
# a second way to fix this:
print("count for TGA is " + str(counts.get('TGA', 0)))
print("count for AAA is " + str(counts.get('AAA', 0)))
print("count for GTA is " + str(counts.get('GTA', 0)))
print("count for TTT is " + str(counts.get('TTT', 0)))
# the get method takes an optional second argument, which is the default value to be returned if the key isn't present in the dictionary

# iterating over a dictionary
# one example
for base1 in ['A', 'T', 'G', 'C']:
	for base2 in ['A', 'T', 'G', 'C']:
		for base3 in ['A', 'T', 'G', 'C']:
			trinucleotide = base1 + base2 + base3
			if counts.get(trinucleotide, 0) == 2:
				print(trinucleotide)

# a second example
# iterating over keys
# the keys method returns a list of all of the keys in the dictionary
for trinucleotide in counts.keys():
	if counts.get(trinucleotide) == 2:
		print(trinucleotide)

# note that the output from each method is listed in a different order even though we are asking for the same keys in each example
# dictionaries are inherently unordered
# to control the order in which keys are printed, use the sorted function to sort the list before processing it
for trinucleotide in sorted(counts.keys()):
	if counts.get(trinucleotide) == 2:
		print(trinucleotide)

# iterating over items
# instead of this:
#for key in my_dict.keys():
#	value = my_dict.get(key)
	# do something with key and value

# do this:
#for key, value in my_dict.items():
	# do something with key and value
# the items method returns a list of pairs of values

for trinucleotide, count in counts.items():
	if count == 2:
		print(trinucleotide)
# this is the best way to iterate over items in a dictionary because it makes the intent of the code very clear

# dictionaries allow us to rapidly look up the value associated with a key, but not the reverse