def decorator_function(original_function):

	def wrapper_function():
		print("wrapper executed this before {} function".format(original_function.__name__))
		return original_function()

	return wrapper_function

@decorator_function
def display():
	print("display function ran well.")

# decorator_function(display)

display()
