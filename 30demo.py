"""
s = 'hello world'
print(s)

s1 = 'hey "dude"'
s2 = "don't tell me what to do"
print(s1, s2)

print('hey "dude" don\'t tell me what to do"')
polyA = 'a' * 100
print(polyA)
hi = 'hello' + 'world'
print(hi)
print(len(s))

#method syntax

print(s.upper())
print(s)
print(s.replace('o', ''))
print(s.replace('o', '').replace('r', 'i'))

# f string
import math

print(f'{math.pi}')
print(f'{math.pi:.3f}')
print(f'{1e6 * math.pi:e}')
print(f'{"hello world":.>20}')
print(f'{20:<10} {10}')

print('{} {:.3f}'.format('str.format', math.pi))

# Indexes

seq = 'GAATTCC'
print(seq[0], seq[1])
print(seq[-1])

for nt in seq:
	print(nt, end="")
print()

s = 'ABCDEFGHIJ'
print(s[0:5])
print(s[0:8:2])

print(s[0:5], s[:5])
print(s[5:len(s)], s[5:])

print(s, s[::], s[::1], s[::-1])


dna = 'ATGCTGTAA'
for i in range(0, len(dna), 3):
	codon = dna[i:i+3]
	print(i, codon)

# Tuples

tax = ('Homo', 'sapiens', 9606)
print(tax)
print(tax[0])
print(tax[::-1])


nts = 'ACGT'
for i in range(len(nts)):
	print(i, nts[i])

for i, nt in enumerate(nts):
	print(i, nt)

names = ('adenine', 'cytosine', 'guanine', 'thymine')
for i in range(len(names)):
	print(nts[i], names[i])
	
for nt, name in zip(nts, names):
	print(nt, name)
	
for i, (nt, name) in enumerate(zip(nts, names)):
	print(i, nt, name)


nts = ['A', 'T', 'C']
print(nts)
nts[2] = 'G'
print(nts)
nts.append('C')
print(nts)

last  = nts.pop()
print(last)

nts.sort()
print(nts)
nts.sort(reverse=True)
print(nts)

nucleotides = nts
nucleotides.append('C')
nucleotides.sort()
print(nts, nucleotides)


items = list()
print(items)
items.append('eggs')
print(items)

stuff = []
stuff.append(3)
print(stuff)

alph = 'ABCEDFGHIJKLMNOPQRSVW'
print(alph)
aas = list(alph)
print(aas)

text = 'good day          to you'
words = text.split()
print(words)

line = '1.41,2.72,3.14'
print(line.split('\t'))

s = '-'.join(aas)
print(s)
s = ''.join(aas)
print(s)

if 'A' in alph: print('yay')
if 'a' in alph: print('no')

print('index G?', alph.index('G'))

print('find G?', alph.find('G'))
print('find Z?', alph.find('Z'))

# Practice
vals = [5, 6, 2, 8, 1]


def minimum(vals):
	vals.sort()
	return vals[0]
print(minimum(vals))



def othermin(vals):
	mini = vals[0]
	for val in vals[1:]:
		if val < mini: mini = val
	return mini
print(othermin(vals))	

def minmax(vals):
	mini = vals[0]
	maxi = vals[0]
	for val in vals[1:]:
		if val < mini: mini = val
		if val > maxi: maxi = val
	return mini, maxi
print(minmax(vals))


def mean(vals):
	total = 0
	for val in vals:
		total = total + val
	return total / len(vals)
print(mean(vals))


import math
def entropy(probs):
	total = 0
	for prob in probs:
		total = prob * math.log2(prob)
	return - 1 * total
print(entropy([0.1, 0.2, 0.5]))

p = [0.4, 0.3, 0.4]
q = [0.5, 0.6, 0.2]
def kullback(p, q):
	total = 0
	for p1, q1 in zip(p, q):
		total = total + p1 * math.log(p1 / q1)
	return total
print(kullback(p, q))
	
"""
"""
# Command Line

import sys
print(sys.argv[1])

i = int('42')
x = float('0.61803')
print(i * x)
"""

list = ['A', 'G', 'C', 'T']
for i in range(0, len(list)):
	for j in range(0, len(list)):
		print(i, j)

			














# use f = float(arg) to turn "numbers" into numbers