# 3a.

i = [1,2,3,4,5]

for n in i:
	print(n)

# 3b.
j = 0
while j < len(i):
	print(i[j])
	j+=1

# 3c.

for n in range(1,len(i)+1):
	print(i[-n])

# 3d.

for n in i:
	if n < 0:
		print('negative')
	elif n == 0:
		print('zero')
	else:
		print('positive')

# 3f.

def isEven(n):
	return n % 2 == 0

# 3g.

def EvenRand():
	return 4

def testEvenRand():
	assert EvenRand()%2 == 0

# 3.h 

a = 10*[0]
b = [a]*10
print(b)