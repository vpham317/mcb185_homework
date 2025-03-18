import sys
import mcb185

# GC Composition

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split()
	name = defwords[0]
	gc = 0
	for nt in seq:
		if nt == 'C' or nt == 'G': gc += 1
	print(name, gc/len(seq))
	gctotal += gc
	lentotal += len(seq)

	
"""	
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split()
	name = defwords[0]
	print(name, end=' ')
	for nt in 'ACGTN':
		print(seq.count(nt) / len(seq), end=' ')
	print()
"""