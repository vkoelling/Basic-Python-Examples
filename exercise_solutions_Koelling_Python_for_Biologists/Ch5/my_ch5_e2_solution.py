# Vanessa Koelling, August 10th, 2017.

# Chapter 5, exercise 2: percentage of amino acid residues, part two

def get_amino_acid_residue_percentage(protein, residue=['A', 'I', 'L', 'M', 'F', 'W', 'Y', 'V'], sig_figs=2):
	protein_length = len(protein)
	total = 0
	for aa in residue:
		amino_acid = aa.upper()
		residue_count = protein.upper().count(amino_acid)
		total = total + residue_count
	residue_percentage = (total/protein_length) * 100
	return round(residue_percentage, sig_figs)
	
assert get_amino_acid_residue_percentage("MSRSLLLRFLLFLLLLPPLP", ["M"]) == 5
assert get_amino_acid_residue_percentage("MSRSLLLRFLLFLLLLPPLP", ['M', 'L']) == 55
assert get_amino_acid_residue_percentage("msrslllrfllfllllpplp", ['F', 'S', 'L']) == 70
assert get_amino_acid_residue_percentage("MSRSLLLRFLLFLLLLPPLP") == 65

test_protein = "MSRSLLLRFLLFLLLLPPLP"
print(get_amino_acid_residue_percentage(test_protein, ["M"]))