def outer_function():
	msg = "Hi!"

	def inner_function():
		print(msg)

	return inner_function()




outer_function()