import sys
import sequence
import mcb185

seq = 'AAAAAAAAAAGGGGGGGGGGTTTTTTTTTT'
w = 10
s = seq[:w]
g_count = s.count('G')
c_count = s.count('C')

for i in range(1, len(seq) - w + 1):
	if seq[i-1] == 'G': g_count -=1
	elif seq[i-1] == 'C': c_count -=1
	if seq[i + w - 1] == 'G': g_count +=1
	elif seq[i + w - 1] == 'C': c_count +=1
	s = seq[i:i + w]
	print(i, sequence.gc_comp(s), sequence.gc_skew(s))