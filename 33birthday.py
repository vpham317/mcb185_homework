import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

same = 0

for i in range(trials):
	bdays = []
	for person in range(people):
		r = random.randint(0, days)
		if r in bdays: 
			print('same birthday')
			same += 1
			break
		else: bdays.append(r)

print(same / trials)

			
			


	