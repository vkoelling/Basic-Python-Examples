# Vanessa Koelling, August 9th, 2017.

# Ch. 4 exercise 2: Multiple exons from genomic DNA

# open the genomic DNA file
genomic_dna = open("/Users/vkoelling/Desktop/Python_practice_files/Python_for_Biologists_exercises_and_examples/Chapter_4/exercises/genomic_dna.txt")
# read the contents of the file into a new variable
seq = genomic_dna.read()
# open the exon positions file
exons = open("/Users/vkoelling/Desktop/Python_practice_files/Python_for_Biologists_exercises_and_examples/Chapter_4/exercises/exons.txt")
# open a new file called coding_seq
coding_seq = open("coding_seq.txt", "w")
# loop writes the exons to the new file
for exon in exons:
	exon_position = exon.split(",") # create a list out of the first set of exon positions
	exon_start = int(exon_position[0]) # index the list and convert the string to an integer
	exon_stop = int(exon_position[1])
	exon_seq = seq[exon_start:exon_stop] # get the exon sequence
	coding_seq.write(exon_seq) # write the exon sequence to a new file
coding_seq.close()
