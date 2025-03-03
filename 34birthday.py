import sys
import random

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

same = 0

for i in range(trials):
	calendar = []
	for i in range(days + 1):
		calendar.append(0)
	for person in range(people):
		r = random.randint(0, days)
		calendar[r] += 1
		if 2 in calendar: 
			same += 1
			break
	
print(same)
print(same / trials)