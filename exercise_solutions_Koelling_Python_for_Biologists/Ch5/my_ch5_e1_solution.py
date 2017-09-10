# Vanessa Koelling, August 10th, 2017.

# Chapter 5, exercise 1: percentage of amino acid residues, part one

def get_amino_acid_residue_percentage(protein, residue, sig_figs=2):
	residue = residue.upper()
	protein_length = len(protein)
	residue_count = protein.upper().count(residue)
	residue_percentage = (residue_count/protein_length) * 100
	return round(residue_percentage, sig_figs)
	
assert get_amino_acid_residue_percentage("MSRSLLLRFLLFLLLLPPLP", "M") == 5
assert get_amino_acid_residue_percentage("MSRSLLLRFLLFLLLLPPLP", "r") == 10
assert get_amino_acid_residue_percentage("msrslllrfllfllllpplp", "L") == 50
assert get_amino_acid_residue_percentage("MSRSLLLRFLLFLLLLPPLP", "Y") == 0

test_protein = "MSRSLLLRFLLFLLLLPPLP"
print(get_amino_acid_residue_percentage(test_protein, "M"))
