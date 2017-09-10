# Vanessa Koelling, August 8th, 2017.

# Writing a FASTA file

# set the sequence values
abc123 = "ATCGTACGATCGATCGATCGCTAGACGTATCG"
def456 = "actgatcgacgatcgatcgatcacgact"
hij789 = "ACTGAC-ACTGT--ACTGTA----CATGTG"
# open a new fasta file
my_fasta = open("dna_sequences.fasta", "w")
# write the headers and sequences to the file with newline characters included
my_fasta.write(">ABC123\n" + abc123 + "\n" + ">DEF456\n" + def456.upper() + "\n" + ">HIJ789\n" + hij789.replace("-", ""))
my_fasta.close()
