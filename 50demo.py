
"""
s = {'A', 'C', 'G'}
print(s)
s.add('T')
print(s)

d = {'dog': 'woof', 'cat': 'meow'}
print(d)
print(d['cat'])

d['pig'] = 'oink'
print(d)

d['cat'] = 'mew'
print(d)

del d['cat']
print(d)

if 'dog' in d:
	print(d['dog'])

#Iteration

for key in d:
	print(f'{key} says {d[key]}')

for k, v in d.items(): print(k, 'says', v)

kdtable = {
    'I':  4.5, 'V':  4.2, 'L':  3.8, 'F':  2.8, 'C':  2.5, 'M': 1.9, 'A': 1.8,
    'G': -0.4, 'T': -0.7, 'S': -0.8, 'W': -0.9, 'Y': -1.3, 'P':-1.6, 'H': -3.2,
    'E': -3.5, 'Q': -3.5, 'D': -3.5, 'N': -3.5, 'K': -3.9, 'R': -4.5
}

def kd_dict(seq):
	kd = 0 
	for aa in seq: kd += kdtable[aa]
	return kd/len(seq)
"""
"""
seq = 'AAAAAAAAACCCCCCCGGGT'
count = {}
for nt in seq:
	if nt not in count: count[nt] = 0
	count[nt] += 1	
print(count)
"""

import itertools
for nts in itertools.product('ACGT', repeat = 2):
	print(nts)
	
print('first', 'second', sep='\t', end='\n')
print('first', 'second', end='\n', sep='\t')









