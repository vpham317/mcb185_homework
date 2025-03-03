import sys
import math

probs = []
for arg in sys.argv[1:]:
	f = float(arg)
	if f >= 1 or f <= 0: sys.exit('error: must be probability')
	probs.append(float(arg))
	
total = 0
for prob in probs: total += prob
if not math.isclose(total, 1.0):
	sys.exit('error: probs must equal 1.0')
		
h = 0 
for p in probs:
	h -= p * math.log2(p)

print(f'{h:.4f}')

