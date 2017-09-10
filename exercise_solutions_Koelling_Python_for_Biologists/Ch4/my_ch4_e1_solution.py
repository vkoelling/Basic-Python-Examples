# Vanessa Koelling, August 9th, 2017.

# Ch. 4 exercise 1: Processing DNA in a file

dna_seq_file = open("/Users/vkoelling/Desktop/Python_practice_files/Python_for_Biologists_exercises_and_examples/Chapter_4/exercises/input.txt")
# dna_seq_file contains newline characters at the end of each line
trimmed_dna_seq_file = open("trimmed.txt", "w")
for seq in dna_seq_file:
	dna_seq_lenth = len(seq)
	new_seq = seq[14:dna_seq_lenth]
	trimmed_dna_seq_file.write(new_seq)
	new_seq_length = len(new_seq) - 1 # subtract 1 here or the newline character is counted as part of the sequence length
	print(new_seq_length)
trimmed_dna_seq_file.close()

