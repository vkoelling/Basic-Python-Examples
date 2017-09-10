# Vanessa Koelling, August 22nd, 2017.

# Chapter 9, exercise 2: kmer counting

# this script requires the input of command line arguments
# to initiate this script, type in at the command line: python my_ch9_e2_solution.py kmer_length cutoff_number

import sys
import os

def find_kmers(seq, kmer_length):
	seq_length = len(seq)
	kmer_length = kmer_length
	kmer_list = []
	for kmer_start in range(0, seq_length - (kmer_length - 1), 1): # you've got to ensure that there are enough nucleotides in the sequence for the specified kmer length
		kmer = seq[kmer_start:kmer_start + kmer_length]
		kmer_list.append(kmer)
	return kmer_list

kmer_length = int(sys.argv[1]) # first command line argument
cutoff_number = int(sys.argv[2]) # second command line argument

kmer_counts = {}

# we're going to cycle through all of the available DNA files and find kmers of the specified length
for file_name in os.listdir("/Users/vkoelling/Desktop/Python_practice_files/Python_for_Biologists_exercises_and_examples/Chapter_9/exercises/."):
	if file_name.endswith(".dna"):
		dna_input = open("/Users/vkoelling/Desktop/Python_practice_files/Python_for_Biologists_exercises_and_examples/Chapter_9/exercises/" + str(file_name))
		for seq in dna_input:
			dna_seq = seq.upper().rstrip("\n")
			for kmer in find_kmers(dna_seq, kmer_length):
				current_count = kmer_counts.get(kmer, 0) # the zero is the default value when the key is not present in the dictionary
				new_count = current_count + 1 # every instance of finding kmer in the list returned by find_kmers will be added to the count
				kmer_counts[kmer] = new_count # this will add the key and its value to the dictionary

for kmer, count in kmer_counts.items():
	if count > cutoff_number:
		print(kmer + ":" + str(count))