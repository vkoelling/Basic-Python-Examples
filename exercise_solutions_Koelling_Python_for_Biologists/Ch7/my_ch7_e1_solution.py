# Vanessa Koelling, August 13th, 2017.

# Chapter 7, exercise 1: accession names

import re
accession_names = ["xkn59438", "yhdck2", "eihd39d9", "chdsye847", "hedle3455", "xjhd53e", "45da", "de37dp"]
# match contains the number 5
for accession in accession_names:
	if re.search(r"5", accession):
		print(accession)
print("-----------------------")
# match contains the letter d or e
for accession in accession_names:
	if re.search(r"[de]", accession):
		print(accession)
print("-----------------------")
# match contains the letters d and e in that order
for accession in accession_names:
	if re.search(r"d.*e", accession):
		print(accession)
print("-----------------------")
# match contains the letters d and e in that order with a single letter between them
for accession in accession_names:
	if re.search(r"d.e", accession):
		print(accession)
print("-----------------------")
# match contains both the letters d and e in any order
for accession in accession_names:
	if re.search(r"d.*", accession) and re.search(r"e.*", accession):
		print(accession)
print("-----------------------")
# match starts with x or y
for accession in accession_names:
	if re.search(r"^[xy]", accession):
		print(accession)
print("-----------------------")
# match starts with x or y and ends with e
for accession in accession_names:
	if re.search(r"^[xy].*e$", accession):
		print(accession)
print("-----------------------")
# match contains three or more numbers in a row
for accession in accession_names:
	if re.search(r"\d{3,}", accession):
		print(accession)
print("-----------------------")
# match ends with d followed by either a, r or p
for accession in accession_names:
	if re.search(r"d[arp]$", accession):
		print(accession)
