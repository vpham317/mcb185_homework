import sys
import mcb185
import itertools
import sequence

k = 1
kcount = {}
n = 0
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	rc = sequence.revcomp(seq)
	while n < 1:
		for i in range(len(seq) -k + 1):
			kmer = seq[i:i+k]
			if kmer not in kcount:
				kcount[kmer] = 0
			kcount[kmer] += 1
		
		for i in range(len(rc) -k +1):
			kmer = rc[i:i+k]
			if kmer not in kcount:
				kcount[kmer] = 0
			kcount[kmer] += 1
		for nts in itertools.product('ACGT', repeat = k):
			kmer = ''.join(nts)
			if kmer not in kcount:
				print(kmer)
				n += 1
	
		k += 1
		kcount={}
print(k - 1, n)

