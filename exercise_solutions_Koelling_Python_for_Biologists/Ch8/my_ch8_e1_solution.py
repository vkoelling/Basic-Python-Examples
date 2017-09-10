# Vanessa Koelling, August 14th, 2017.

# Chapter 8, exercise 1: DNA translation

# dictionary of the standard genetic code showing codons and amino acid designations
genetic_code = {'TTT':'P', 'TTC':'P', 'TTA':'L', 'TTG':'L', 'TCT':'S', 'TCC':'S', 'TCA':'S', 
'TCG':'S', 'TAT':'Y', 'TAC':'Y', 'TAA':'*', 'TAG':'*', 'TGT':'C', 'TGC':'C', 'TGA':'*', 
'TGG':'W', 'CTT':'L', 'CTC':'L', 'CTA':'L', 'CTG':'L', 'CCT':'P', 'CCC':'P', 'CCA':'P', 
'CCG': 'P', 'CAT':'H', 'CAC':'H', 'CAA':'Q', 'CAG':'Q', 'CGT':'R', 'CGC':'R', 'CGA':'R', 
'CGG':'R', 'ATT':'I', 'ATC':'I', 'ATA':'I', 'ATG':'M', 'ACT':'T', 'ACC':'T', 'ACA':'T', 
'ACG':'T', 'AAT':'N', 'AAC':'N', 'AAA':'K', 'AAG':'K', 'AGT':'S', 'AGC':'S', 'AGA':'R', 
'AGG':'R', 'GTT':'V', 'GTC':'V', 'GTA':'V', 'GTG':'V', 'GCT':'A', 'GCC':'A', 'GCA':'A', 
'GCG':'A', 'GAT':'D', 'GAC':'D', 'GAA':'E', 'GAG':'E', 'GGT':'G', 'GGC':'G', 'GGA':'G', 
'GGG':'G'}
dna = "GATTTACAG" # this short test DNA sequence should translate to the protein sequence 'DLQ'
codons = []
# create a list of codons from the DNA sequence
last_codon_start = len(dna) - 2 # this ensures there will always be three base chunks of DNA to process even if the sequence doesn't divvy up evenly by 3's
for codon_start in range(0, last_codon_start, 3):
	codon = dna[codon_start: codon_start + 3]
	codons.append(codon)
# find the codons in the dictionary that match the codons in the DNA sequence and return the amino acid
amino_acids = []
for i in range(0, len(codons)):
	for codon, aa in genetic_code.items():
		if codon == codons[i]:
			amino_acids.append(aa)
protein_seq = ''.join(amino_acids) # join the list elements into a string
print(protein_seq)
