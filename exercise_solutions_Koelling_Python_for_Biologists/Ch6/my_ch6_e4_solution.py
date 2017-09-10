# Vanessa Koelling, August 11th, 2017.

# Chapter 6, exercise 4: complex condition

input_file = open("/Users/vkoelling/Desktop/Python_practice_files/Python_for_Biologists_exercises_and_examples/Chapter_6/exercises/data.csv")
for row in input_file:
	new_row = row.rstrip("\n").split(",")
	species = new_row[0]
	sequence = new_row[1]
	gene_name = new_row[2]
	expression_level = new_row[3]
	if (gene_name.startswith('k') or gene_name.startswith('h')) and not species == "Drosophila melanogaster":
		print(gene_name)
		
