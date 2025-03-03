import math
import sys

vals = []
for arg in sys.argv[1:]:
	vals.append(float(arg))

# number of values
total = 0
for val in vals:
	total += 1
print('number of values:', total)

# minimum and maximum
maxi = vals[0]
mini = vals[0]
for val in vals:
	if val < mini: mini = val
	if val > maxi: maxi = val
print('max:', maxi, 'min:', mini)

# mean and standard deviation
u = 0
for val in vals:
	u = u + val
mean = u / total
print('mean:', mean)

sd = 0 
for val in vals:
	sd = sd + (val - mean) ** 2
print('sd:', math.sqrt(sd / total))

# median
vals.sort()

pos1 = int((total / 2) - 1)
pos2 = int(total / 2)
odd = int(math.ceil((total / 2) - 1))

if total % 2 == 0:
	med = (vals[pos1] + vals[pos2]) / 2
else: med = vals[odd]
print('med:', med)
	
	
	
	
	
	
	
	
	
	
	
	
	

