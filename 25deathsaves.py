import random

trial = 100
die = 0
stable = 0
revive = 0

for i in range(trial):
	failure = 0
	success = 0
	revived = False
	while success < 3 and failure < 3 and revived == False:
		r = random.randint(1, 20)
		if r == 20: revived = True
		elif r >= 10: success += 1
		elif r == 1: failure += 2
		else: failure += 1
	if revived: revive += 1
	elif success >= 3: stable += 1
	else: die += 1
	
	
print(success, failure, revived)
print('revived:', revive, 'stabilized:', stable, 'died:', die)
print('revived:', revive / trial, 'stablized:', stable / trial, 'died:', die / trial)
print('total good cases:', (revive / trial) + (stable / trial))