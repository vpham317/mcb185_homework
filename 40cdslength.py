import gzip
import sys

with gunzip.open(sys.argv[1], 'rt') as fp:
	for line in fp:
		if line[0] != '#':
			words = line.split()
			if words[2] == 'CDS':
				beg = int(words[3])
				end = int(words[4])
				print(end - beg + 1)
				