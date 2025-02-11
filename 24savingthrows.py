import random

# without advantage and disadvantage
# DC = 'DC5' , 'DC10', or 'DC15'

def saving(DC):
	x = random.randint(1, 20)
	y = random.randint(1, 20)
	if DC == 'DC15': 
		if x >= 15: print(x, 'success')
		elif x < 15: print(x, 'fail')
	if DC == 'DC5':
		if x >= 5: print(x, 'success')
		elif  x < 15: print(x, 'fail')
	if DC == 'DC10':
		if x >= 10: print(x, 'success')
		elif x < 10: print(x, 'fail')
	

# with advantage and disadvantage
# R = 'adv', or 'disadv'

trials = 100
def savingR(DC, R):
	success = 0
	fail = 0
	for k in range(trials):
		x = random.randint(1, 20)
		print(x)
		y = random.randint(1, 20)
		print(y)
		if R == 'adv':
			if x > y: i = x
			if y > x: i = y
			if DC == 'DC15': 
				if i >= 15: 
					print(i, 'success')
					success += 1
				elif i < 15: 
					print(i, 'fail')
					fail += 1
			if DC == 'DC5':
				if i >= 5: 
					print(i, 'success')
					success += 1
				elif  i < 15: 
					print(i, 'fail')
					fail += 1
			if DC == 'DC10':
				if i >= 10: 
					print(i, 'success')
					success += 1
				elif i < 10: 
					print(i, 'fail')
					fail += 1
		if R == 'disadv':
			if x > y: i = y
			if y > x: i = x
			if DC == 'DC15': 
				if i >= 15: print(i, 'success')
				elif i < 15: print(i, 'fail')
			if DC == 'DC5':
				if i >= 5: print(i, 'success')
				elif  i < 15: print(i, 'fail')
			if DC == 'DC10':
				if i >= 10: print(i, 'success')
				elif i < 10: print(i, 'fail')
	print(success)
	print(fail)
print(savingR('DC15', 'adv'))
