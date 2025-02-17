import random

trial = 10
dc = 15
mode = 'adv'

success = 0
fail = 0
for i in range(trial):
	x = random.randint(1, 20)
	y = random.randint(1, 20)
	if mode == 'adv':
		roll = (x, y)
		if x > y: 
			roll = x
		else: 
			roll = y
	elif mode == 'disadv':
		roll = (x, y)
		if x > y: 
			roll = y
		else: 
			roll = x
	else: 
		roll = x
	
	if roll >= dc: 
		print('success')
		success += 1
	else: 
		print('fail')
		fail += 1

print('success:', success, 'fails:', fail, 'probability of success:', success / trial)
