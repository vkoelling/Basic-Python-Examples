# Vanessa Koelling, August 7th, 2017.

# Exercise on splicing out introns, part one

dna_seq = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
dna_seq_length = len(dna_seq)
exon1 = dna_seq[0:63]
exon2 = dna_seq[90:dna_seq_length]
print(exon1 + exon2)

