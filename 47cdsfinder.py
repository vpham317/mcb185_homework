import mcb185
import sys
import sequence
import random
"""
min_length = int(sys.argv[2])
"""
def dna_random(length):
	return ''.join(random.choices('ACGT', k = length))

dna_random = ''.join(random.choices('ACGT', k = 4600000))

def get_protein(seq, t):
	proteins = 0
	for i in range(3):
		translation = mcb185.translate(seq[i:])
		orfs = translation.split('*')
		for orf in orfs:
			if 'M' not in orf: continue
			idx = orf.index('M')
			pro = orf[idx:]
			if len(pro) >= t: proteins +=1
	return proteins
	
print(get_protein(dna_random, 100))
"""
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split()
	name = defwords[0]
	p = 0
	for protein in get_protein(seq, min_length):
		print(f'>(name-prot-{p})')
		print(protein)
		p += 1
"""