# Vanessa Koelling, August 11th, 2017.

# Chapter 6, exercise 3: at content

def get_at_content(dna):
    length = len(dna)
    a_count = dna.upper().count('A')
    t_count = dna.upper().count('T')
    at_content = (a_count + t_count) / length
    return at_content

input_file = open("/Users/vkoelling/Desktop/Python_practice_files/Python_for_Biologists_exercises_and_examples/Chapter_6/exercises/data.csv")
for row in input_file:
	new_row = row.rstrip("\n").split(",")
	species = new_row[0]
	sequence = new_row[1]
	gene_name = new_row[2]
	expression_level = int(new_row[3])
	if get_at_content(sequence) < 0.5 and expression_level > 200:
		print(gene_name)
