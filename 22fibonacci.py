
def fibonacci(x):
	prev1 = -1
	prev2 = 1
	for i in range(x):
		total = prev1 + prev2
		prev1 = prev2
		prev2 = total
		print(total)

print(fibonacci(10))