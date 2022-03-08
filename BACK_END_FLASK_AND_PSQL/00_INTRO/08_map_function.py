"""
numbers = input().split(" ")

new_numbers = []

for number in numbers:
	new_numbers.append(int(number))

print(new_numbers)
"""

# numbers = list(map(int, input().split()))
# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8]
# new_numbers = list(map(lambda n : n+3, numbers))
# add_3 = lambda x: x+3
# new_numbers = [ add_3(x) for x in numbers ]
# print(new_numbers)

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8]

odd = list(map(lambda m: m**2, filter(lambda n: n%2 == 0, numbers)))
# new_numbers = list(map(lambda m: m**2, odd))
print(odd)