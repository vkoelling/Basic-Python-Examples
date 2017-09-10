# Vanessa Koelling, August 7th, 2017.

# Exercise on complementing DNA.

dna_seq = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
a_to_t = dna_seq.replace("A", "t")
c_to_g = a_to_t.replace("C", "g")
t_to_a = c_to_g.replace("T", "a")
g_to_c = t_to_a.replace("G", "C")
reverse_complement = g_to_c.upper()
print(dna_seq)
print(reverse_complement)