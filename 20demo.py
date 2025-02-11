t = 1, 2
print(t)
print(type(t))

person = 'Steve', 21, 57891.5 # Name, Age, Yearly income
print(person)

def midpoint(x1, x2, y1, y2):
	x= (x1 + x2) / 2
	y= (y1 + y2) / 2
	return x, y
	
print(midpoint(1, 2, 3, 4))
m = midpoint(1, 2, 3, 4)
mx, my = midpoint(1, 2, 3, 4)
print(mx, my)

print(m[0], m[1])


	
i = 0
while True:
	i = i +1
	print('hey', i)
	if i == 3: break
	
i = 0
while i < 3:
	i = i +1
	print('hey', i)

i = 0
while i < 10:
	print(i)	
	i = i +3
print('final value of i is', i)

for i in range(1, 10, 3):
	print(i)	
	
for i in range(0, 5):
	print(i)

for i in range(5):
	print(i)
	
basket = 'milk', 'eggs', 'bread'
for thing in basket:
	print(thing)
	
for i in range(len(basket)):
	print(basket[i])
	
for i in range(7):
	if i % 2 == 0:	print(i, 'is even')
	else:			print(i, 'is odd')


## Practice Problems

#triangular

def triangles(n):
	total = 0
	for i in range(0, n + 1): 
		total = total + i
	return total
print(triangles(6))
	
def factorial(n):
	total = 1
	for i in range(1, n + 1):
		total = total * i
	return total
print(factorial(8))


import math
def poisson(n, k):
	return n ** k * math.e ** -n / factorial(k)
print(poisson(9,9))

# Euler

def euler(n):
	i = 0
	for j in range(n):
		i = i + 1 / factorial(j)
	return i
print(euler(100))

# Prime

def prime(n):
	for i in range(2, n):
		if n % i == 0: return 'not prime'
	return 'prime'
print(prime(13))

# Estimates Pi


def nilakantha(limit):
	i = 3
	for j in range(1, limit + 1):
		n = 4 * (-1) ** (j + 1)
		d = 2 * j * (2 * j + 1) * (2 * j + 2)
		i = i + (n / d)
	return i
	
print(nilakantha(100))



	
