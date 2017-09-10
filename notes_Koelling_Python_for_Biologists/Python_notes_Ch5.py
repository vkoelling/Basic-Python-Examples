# Vanessa Koelling, August 9th, 2017. This document contains some notes and code examples in Python 3 from "Python for Biologists".
# Chapter 5 notes

# defining a function

# create a function that calculates the AT content in a sequence of DNA
def get_at_content(dna, sig_figs=2): # takes as arguments the DNA sequence and the number of significant figures; the default sig_figs is set to 2, but the value supplied will supercede the default
	dna = dna.replace('N', '') # don't include unknown bases in the calculation
	length = len(dna)
	a_count = dna.upper().count('A')
	t_count = dna.upper().count('T')
	at_content = (a_count + t_count)/length
	return round(at_content, sig_figs) # rounds the return value to the specified number of significant figures
	
# call the get_at_content function
# at_content = get_at_content("ATGACTGGACCA")
# print(at_content)
# 
# my_at_content = get_at_content("ATGCGCGATCGATCGAATCG")
# print(str(my_at_content))
# print(get_at_content("ATGCATGCAACTGTAGC"))
# print(get_at_content("aactgtagctagctagcagcgta"))

test_dna = "ATGCATGCAACTGTAGC"
print(get_at_content(test_dna, 1))
print(get_at_content(test_dna, 2))
print(get_at_content(test_dna, 3))

# testing functions
# use assert statements to test that your code is working as expected
assert get_at_content("ATGC") == 0.5
# if you return an AssertionError, then you know there is a problem with your code

