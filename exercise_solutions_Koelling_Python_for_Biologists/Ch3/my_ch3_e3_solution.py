# Vanessa Koelling, August 8th, 2017.

# Writing a FASTA file

# set the sequence values
abc123 = "ATCGTACGATCGATCGATCGCTAGACGTATCG"
def456 = "actgatcgacgatcgatcgatcacgact"
hij789 = "ACTGAC-ACTGT--ACTGTA----CATGTG"
# open a new fasta file for each sequence
my_fasta1 = open("ABC123.fasta", "w")
my_fasta2 = open("DEF456.fasta", "w")
my_fasta3 = open("HIJ789.fasta", "w")
# write the headers and sequences to each file with newline characters included
my_fasta1.write(">ABC123\n" + abc123)
my_fasta2.write(">DEF456\n" + def456.upper())
my_fasta3.write(">HIJ789\n" + hij789.replace("-", ""))
my_fasta1.close()
my_fasta2.close()
my_fasta3.close()
