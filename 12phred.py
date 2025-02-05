import math

def char_to_prob(x):
	p = 10 ** ((ord(x) - 33) / -10)
	return p

def prob_to_char(x):
	q = int((-10 * math.log10(x))) + 33
	if 33 <= q <= 126: return chr(q)
	

print(char_to_prob('A'))
print(prob_to_char(0.001))