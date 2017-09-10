# Vanessa Koelling, August 8th, 2017.

# Splitting genomic DNA

dna_seq_file = open("/Users/vkoelling/Desktop/Python_practice_files/Python_for_Biologists_exercises_and_examples/Chapter_3/exercises/genomic_dna.txt")
dna_seq = dna_seq_file.read()
dna_seq_length = len(dna_seq)
exon1 = dna_seq[0:63]
exon2 = dna_seq[90:dna_seq_length]
intron = dna_seq[63:90]
coding_seq = open("coding_seq.txt", "w")
coding_seq.write(exon1 + exon2)
coding_seq.close()
non_coding_seq = open("non_coding_seq.txt", "w")
non_coding_seq.write(intron)
non_coding_seq.close()

