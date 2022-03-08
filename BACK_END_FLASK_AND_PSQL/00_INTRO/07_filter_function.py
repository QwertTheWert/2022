"""
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd_a = [i for i in a if i%2 != 0]

# for i in a:
# 	if (i % 2 == 1): odd_a.append(i)

print(odd_a)
"""

def isOdd(x):
	return x%2 != 0

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# odd_a = list(filter(isOdd, a))
# odd_a = list(filter(lambda x: x%2 != 0))
odd_a = [i for i in a if i%2 != 0]

print(odd_a)
