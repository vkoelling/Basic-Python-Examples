# Vanessa Koelling, August 7th, 2017.

# Exercise on splicing out introns, part two.

dna_seq = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
dna_seq_length = len(dna_seq)
exon1 = dna_seq[0:63]
exon2 = dna_seq[90:dna_seq_length]
exon1_length = len(exon1)
exon2_length = len(exon2)
coding_sequence_percentage = (exon1_length + exon2_length)/dna_seq_length
print("The % coding sequence is " + str(coding_sequence_percentage))
