import sys

alph = sys.argv[1]
ms = sys.argv[2]
mms = sys.argv[3]

# print header
print("   ", end="")
for nt in alph:
	print(nt, end="  ")
print()
# print matrix
for nt1 in alph:
	print(nt1, end=" ")
	for nt2 in alph:
		if nt1 == nt2: print(ms, end=" ")
		else: print(mms, end=" ")
	print()


print("   ", end="")
for i in range(len(alph)):
	print(alph[i], end="  ")
print()

for i in range(len(alph)):
	print(alph[i], end=" ")
	for j in range(len(alph)):
		if i == j: print(ms, end=" ")
		else: print(mms, end=" ")
	print()




