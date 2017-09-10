# Vanessa Koelling, August 13th, 2017.

# Chapter 7, exercise 2: double digest

import re
file = open("/Users/vkoelling/Desktop/Python_practice_files/Python_for_Biologists_exercises_and_examples/Chapter_7/exercises/dna.txt")
dna = file.read().rstrip("\n")
sequence_length = len(dna)
AbcI_cut_sites = re.finditer(r"A[ATGC]TAAT", dna)
all_cuts = [0]
for cut in AbcI_cut_sites:
	cut_site = cut.start() + 3
	all_cuts.append(cut_site)
# R stands for adenine or guanine; W stands for adenine or thymine
AbcII_cut_sites = re.finditer(r"GC[AG][AT]TG", dna)
for cut in AbcII_cut_sites:
	cut_site = cut.start() + 4
	all_cuts.append(cut_site)
all_cuts.append(sequence_length)
all_cuts.sort()
print(all_cuts)
for i in range(0, len(all_cuts) - 1):
	fragment_size = all_cuts[i + 1] - all_cuts[i]
	print("fragment size " + str(i + 1) + " is " + str(fragment_size) + " bp in length")
