from re import T
from tkinter.tix import DirSelectDialog


numbers = [5,3,6,2,10]

def find_greatest(list):
	greatest_value = list[0]
	greatest_index = 0

	for i in range(1, len(list)):
		if list[i] > greatest_value:
			greatest_value = list[i]
			greatest_index = i
	
	return greatest_index

def find_lowest(list):
	lowest_value = list[0]
	lowest_index = 0

	for i in range(1, len(list)):
		if list[i] < lowest_value:
			lowest_value = list[i]
			lowest_index = i
	
	return lowest_index
	
def selection_sort(list, asc=True):
	new_list = []
	if asc == True:
		for i in range (len(list)):
			greater_index = find_greatest(list)
			new_list.append(list.pop(greater_index))
	if asc == False:
		for i in range (len(list)):
			lowest_index = find_lowest(list)
			new_list.append(list.pop(lowest_index))
	return new_list


# print(selection_sort(numbers, asc=True))
print(selection_sort(numbers, asc=False))
