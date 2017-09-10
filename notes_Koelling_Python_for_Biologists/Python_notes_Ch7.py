# Vanessa Koelling, August 11th, 2017. This document contains some notes and code examples in Python 3 from "Python for Biologists".
# Chapter 7 notes

# import the regular expression module, re
import re
# search is a tool of the re module, so the module name must be attached or you will get a NameError
#re.search(pattern, string)

# \n means start a new line
# \t means insert a tab character

# raw strings are used with regular expressions
# this is because some special characters clash with those in regular expressions
# to indicate a raw string, put an r in front of the string
print(r"\t\n") # string will print as written (not as a tab or newline character)

# find a restriction site within a DNA sequence
dna = "ATCGCGAATTCAC"
if re.search(r"GAATTC", dna):
	print("restriction site found!")

dna = "ATCGCGAATTCAC"
if re.search(r"GGACC", dna) or re.search(r"GGTCC", dna):
	print("restriction site found!")

# better method is to capture the variation in the motif
dna = "ATCGCGAATTCAC"
if re.search(r"GG(A|T)CC", dna): # (A|T) means either A or T
	print("restriction site found!")

# search for the motif GCNGC, where N represents any base
dna = "ATCGCGAATTCAC"
if re.search(r"GC(A|T|G|C)GC", dna):
	print("restriction site found!")

# alternatively, the same thing can be written this way
dna = "ATCGCGAATTCAC"
if re.search(r"GC[ATGC]GC", dna):
	print("restriction site found!")

# a period can also be used to denote any character
# but that would mean ANY character would match
if re.search(r"GC.GC", dna):
	print("restriction site found!")
	
# the caret is how to specify the characters you DON'T want to match
if re.search(r"GC[^XYZ]GC", dna):
	print("restriction site found!")
	
# a ? mark specifies that the character in front of it is optional (i.e., it can match either zero or one times)
# so GAT?C means that the T is optional, and GATC or GAC would be a match
# in GGG(AAA)?TTT the group of three As is optional, so GGGAAATTT or GGGTTT will match

# a + sign immediately following a character or group means that the character or group must be present but can be repeated any number of times
# example: GGGA+TTT will match GGGATTT, GGGAATTT, GGGAAATTT, but not GGGTTT.

# an * means that the character or group is optional but can also be repeated
# example: GGGA*TTT will match GGGTTT, GGGATTT, GGGAATTT, etc.

# curly brackets are used to specify a specific number of repeats
# example: GA{5}T will match GAAAAAT but not GAAAAT or GAAAAAAT

# a pair of numbers separated by a comma inside curly brackets specifies an acceptable range of repeat numbers
# example: GA{2,4}T will match GAAT, GAAAT, and GAAAAT, but not GAT or GAAAAAT

# the ^ symbol matches the start of a string
# example: ^AAA will match AAATTT but not GGGAAATTT

# the $ symbol matches the end of a string
# example: GGG$ will match AAAGGG but not AAAGGGCCC

# the \d matches digit characters [0123456789]
# this one was not in the book but was in the solution to the first exercise

# combining characters
# example: ^ATG[ATGC]{30,1000}A{15,10}$
# this matches:
# an ATG start codon at the beginning of the sequence
# followed by between 30 and 1000 bases with can be A, T, G, or C
# followed by a poly-A tail of between 5 and 10 bases at the end of the sequence

dna = "ATGACGTACGTACGACTG"
# store the match object in the variable m
m = re.search(r"GA[ATGC]{3}AC", dna)
print(m.group())

dna = "ATGACGTACGTACGACTG"
# store the match object in the variable m
m = re.search(r"GA([ATGC]{3})AC([ATGC]{2})AC", dna) # first parentheses correspond to match group 1 and the second to match group 2
print("entire match: " + m.group())
print("first bit: " + m.group(1))
print("second bit: " + m.group(2))

dna = "ATGACGTACGTACGACTG"
m = re.search(r"GA([ATGC]{3})AC([ATGC]{2})AC", dna)
# the match object also holds information about the position of the match
print("start: " + str(m.start()))
print("end: " + str(m.end()))
print("group one start: " + str(m.start(1)))
print("group one end: " + str(m.end(1)))
print("group two start: " + str(m.start(2)))
print("group two end: " + str(m.end(2)))

# splitting a string using a regular expression

# split the string wherever we see a base that isn't A, T, G, or C
dna = "ACTNGCATRGCTACGTYACGATSCGAWTCG"
runs = re.split(r"[^ATGC]", dna)
print(runs)

# finding multiple matches
dna = "ACTGCATTATATCGTACGAAATTATACGCGCG"
runs = re.findall(r"[AT]{6,100}", dna)
print(runs)
# the return value is a list of strings
# no position information is retained with the findall method

# use finditer to get a sequence of match objects
# finditer is generally preferable to findall
dna = "ACTGCATTATATCGTACGAAATTATACGCGCG"
runs = re.finditer(r"[AT]{6,100}", dna) # we're looking for an AT-rich region
for match in runs:
	run_start = match.start()
	run_end = match.end()
	print("AT rich region from " + str(run_start) + " to " + str(run_end))
