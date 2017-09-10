# Vanessa Koelling, August 14th, 2017.

# Chapter 9, exercise 1: binning DNA sequences

import os

for bin_lower in range(100, 1000, 100):
	bin_upper = bin_lower + 99
	folder_name = str(bin_lower) + "-" + str(bin_upper)
	os.mkdir(folder_name)

def bin_sequence(seq, seq_number):
	seq.rstrip("\n")
	seq_length = len(seq)
	print("seq length is " + str(seq_length))
	for bin_lower in range(100, 1000, 100):
		bin_upper = bin_lower + 99
		if seq_length >= bin_lower and seq_length < bin_upper:
			folder_name = str(bin_lower) + "-" + str(bin_upper)
			path = "/Users/vkoelling/Desktop/Python_practice_files/Python_for_Biologists_exercises_and_examples/Ch9_solution_scripts_Koelling/" + folder_name
			output = open(path + "/dna" + str(seq_number) + ".txt", "w")
			output.write(seq.upper())
			output.close()

seq_number = 1
for file_name in os.listdir("/Users/vkoelling/Desktop/Python_practice_files/Python_for_Biologists_exercises_and_examples/Chapter_9/exercises/."):
	if file_name.endswith(".dna"):
		dna_input = open("/Users/vkoelling/Desktop/Python_practice_files/Python_for_Biologists_exercises_and_examples/Chapter_9/exercises/" + str(file_name))
		for seq in dna_input:
			bin_sequence(seq, seq_number)
			seq_number = seq_number + 1

