# 10demo.py by Victor

import math

print('hello, again')	# greeting

print(1.5e-2)
print(1 + 1)
print(pow(2, 3))
print(math.ceil(5.6))
print(math.factorial(9))
print(0.1 * 3)

a = 3	# side of triangle
b = 4	# side of triangle
c = math.sqrt(a**2 + b**2)
print(c)

print(type(a), type(b), type(c), sep=', ', end='!\n')

def pythagoras(a, b):
	c = math.sqrt(a**2 +b**2)
	return c
hyp = pythagoras(3, 4)
print(hyp)

def pythagoras(a, b):
	return math.sqrt(a**2 + b**2)
print(pythagoras(3, 4))



# Practice

def circle_area(r):
	return math.pi * r**2
print(circle_area(3))

def rectangle_area(w, h):
	return w * h

def triangle_area(w, h):
	return (w * h) / 2
print(triangle_area(2, 2))

def ftoc(f):			#Fahrenheit to Celsius
	return (f - 32) * (5/9)
print(ftoc(50))

def mphtokph(m):		#MPH to KPH
	return m * 1.60934
print(mphtokph(60))

def arithmean(a, b, c):		#Arithmetic Mean of 3 numbers
	return (a + b + c)/3
print(arithmean(1, 2, 3))

def geomean(a, b, c):		#Geometric Mean of 3 numbers
	return (a + b + c)**(1 / 3)
print(geomean(1, 2, 3))

def harmonicmean(a, b, c):	#Harmonic Mean of 3 numbers
	return 3 / ((1/a) + (1/b) + (1/c))
print(harmonicmean(1, 2, 3))

s = 'hello world'
print(s, type(s))

a = 2
b = 2
if a ==b:
	print('a equals b')
	print(a, b)

def is_even(x):
	if x % 2 == 0: return True
	return False

print(is_even(2))
print(is_even(3))

c = a == b
print(c)
print(type(c))

if a < b: print('a < b')
elif a > b: print('a > b')
else: print('a==b')

a = 2
b = 3
if a < b or a > b: print('all things being equal, a and b are not')
if a < b and a > b: print('you are living in a strange world')
if not False: print(True)

a = 0.3
b = 0.1 * 3
if a < b: print('a < b')
elif a > b: print('a > b')
else: print ('a == b')

print(abs(a-b))
if abs(a-b) < 1e-9: print('close enough')

if math.isclose(a, b): print('close enough')

s1 = 'A'
s2 = 'B'
s3 = 'a'
if s1 < s2: print('A < B')
if s2 < s3: print('B < a')

def silly(m, x, b):
	y = m * x + b
	return y
print(silly(2, 3, 4))

# More Practice

def is_integer(x):
	if math.ceil(x) - x == 0: return 'is integer'
	else: return 'not integer'
print(is_integer(9.89))


def molweight(nucleotide):
	if nucleotide == 'A': return 135.15
	elif nucleotide == 'G': return 151.13
	elif nucleotide == 'T': return 126.11
	elif nucleotide == 'C': return 111.1
	 
print(molweight('A'))
print(molweight('B'))

def complement(nucleotide):
	if nucleotide == 'A': return 'T'
	elif nucleotide == 'T': return 'A'
	elif nucleotide == 'C': return 'G'
	elif nucleotide == 'G': return 'C'
	
print(complement('G'))
print(complement('B'))
