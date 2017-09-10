# Vanessa Koelling, August 11th, 2017. This document contains some notes and code examples in Python 3 from "Python for Biologists".
# Chapter 6 notes

# conditional tests

print(3 == 5)
print(3 > 5)
print(3 <= 5)
print(len("ATGC") > 5)
print("GAATTC".count("T") > 1)
print("ATGCTT".startswith("ATG"))
print("ATGCTT".endswith("TTT"))
print("ATGCTT".isupper())
print("ATGCTT".islower())
print("V" in ["V", "W", "L"])

# equals '=='
# greater than '>'
# less than '<'
# greater than or equal to '>='
# less than or equal to '<='
# not equal '!='
# is a value in a list 'in'
# are two objects the same 'is'

# if/else, and elif statements

expression_level = 125
if expression_level > 100:
	print("gene is highly expressed")
else:
	print("gene is lowly expressed")

file1 = open("one.txt", "w")
file2 = open("two.txt", "w")
file3 = open("three.txt", "w")
accs = ['ab56', 'bh84', 'hv76', 'ay93', 'ap97', 'bd72']
for accession in accs:
	if accession.startswith('a'):
		file1.write(accession + "\n")
	elif accession.startswith('b'):
		file2.write(accession + "\n")
	else:
		file3.write(accession + "\n")
			
# while loops

count = 0
while count < 10:
	print(count)
	count = count + 1
	
# building up complex conditions
# using boolean operators: and/or/not
accs = ['ab56', 'bh84', 'hv76', 'ay93', 'ap97', 'bd72']
for accession in accs:
	if accession.startswith('a') and accession.endswith('3'):
		print(accession)
		
accs = ['ab56', 'bh84', 'hv76', 'ay93', 'ap97', 'bd72']
for accession in accs:
	if accession.startswith('a') or accession.endswith('3'):
		print(accession)

accs = ['ab56', 'bh84', 'hv76', 'ay93', 'ap97', 'bd72']
for accession in accs:
	if (accession.startswith('a') or accession.startswith('b')) and accession.endswith('4'):
		print(accession)
# parentheses added around the or statement to avoid ambiguity

accs = ['ab56', 'bh84', 'hv76', 'ay93', 'ap97', 'bd72']
for accession in accs:
	if accession.startswith('a') and not accession.endswith('6'):
		print(accession)	

# writing true/false functions
def is_at_rich(dna):
	length = len(dna)
	a_count = dna.upper().count('A')
	t_count = dna.upper().count('T')
	at_content = (a_count + t_count)/length
	if at_content > 0.65:
		return True
	else:
		return False
		
print(is_at_rich("ATTATCTACTA"))
print(is_at_rich("CGGCAGCGCT"))

# alternative, more concise version
def is_at_rich(dna):
	length = len(dna)
	a_count = dna.upper().count('A')
	t_count = dna.upper().count('T')
	at_content = (a_count + t_count)/length
	return at_content > 0.65
				

