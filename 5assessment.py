

#table that is amino acid and probabilities 5 by 4
#use dictionary

"""
		frequency
Ala			0.5		 Glu
Arg
Asn
Asp
Cys
"""

import sys
import mcb185

## 1 letter to 3 letter
threeletter = {'A': 'Ala', 'R': 'Arg', 'N': 'Asn', 'D': 'Asp', 'C': 'Cys', 'E': 'Glu',
 'Q': 'Gln', 'G': 'Gly', 'H': 'His', 'I': 'Ile', 'L': 'Leu', 'K': 'Lys', 'M': 'Met', 'F': 'Phe',
  'P': 'Pro', 'S': 'Ser', 'T': 'Thr', 'W': 'Trp', 'Y': 'Tyr', 'V': 'Val'}

seq = 'AAAATTTGGCDFS'
total = 0
count = {}
for defline, seq in mcb185.read_fasta(sys.argv[1]):

	for aa in seq:
		if aa not in count: count[aa] = 0
		count[aa] += 1
		total += 1
		
for aa in count:
	count[aa] /= total

print("AA  Freq        AA  Freq        AA  Freq        AA  Freq")
print("--------------------------------------------------------")
x = 1
for aa, p in count.items():
	if aa in threeletter:
		code = threeletter[aa]
	else:
		code = 'N/A'
	print(f'{code} {100*p:.2f}', end='\t')
	if x % 4 == 0: print()
	x += 1
print()







