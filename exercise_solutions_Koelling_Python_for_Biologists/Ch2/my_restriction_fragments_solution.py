# Vanessa Koelling, August 7th, 2017.

# Exercise on restriction fragment lengths.

dna_seq = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
dna_seq_length = len(dna_seq)
recognition_site_position = dna_seq.find('GAATTC')
fragment1_length = len(dna_seq[0:recognition_site_position])
fragment2_length = len(dna_seq[(recognition_site_position + 1):dna_seq_length])
print(fragment1_length)
print(fragment2_length)
