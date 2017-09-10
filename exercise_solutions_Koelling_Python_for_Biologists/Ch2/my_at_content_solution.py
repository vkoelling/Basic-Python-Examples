# Vanessa Koelling, August 7th, 2017.

# Exercise to calculate AT content.

dna_seq = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
dna_seq_length = len(dna_seq)
adenine_count = dna_seq.count('A')
thymine_count = dna_seq.count('T')
at_count = adenine_count + thymine_count
at_content = at_count/dna_seq_length
print("AT content is: " + str(at_content))