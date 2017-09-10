# Vanessa Koelling, August 11th, 2017.

# Chapter 6, exercise 1: several species

input_file = open("/Users/vkoelling/Desktop/Python_practice_files/Python_for_Biologists_exercises_and_examples/Chapter_6/exercises/data.csv")
for row in input_file:
	new_row = row.rstrip("\n").split(",")
	if new_row[0] == "Drosophila melanogaster" or new_row[0] == "Drosophila simulans":
		print(new_row[0] + " gene name is: " + new_row[2])
	
	

	