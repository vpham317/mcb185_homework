import math

def char_to_prob(x):
	return ord(x)

def prob_to_char(x):
	if math.ceil(x) - x == 0: return chr(x)

print(char_to_prob('A'))
print(prob_to_char(0.001))