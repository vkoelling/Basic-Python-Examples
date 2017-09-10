# Vanessa Koelling, August 7th, 2017.

# Exercise on splicing out introns, part three.

dna_seq = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
dna_seq_length = len(dna_seq)
exon1 = dna_seq[0:63]
exon2 = dna_seq[90:dna_seq_length]
intron = dna_seq[63:90]
print(exon1 + intron.lower() + exon2)
