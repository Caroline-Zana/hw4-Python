def my_steps(n):
    if n <= 1:
        return 1   
    else:
	return my_steps(n - 1) + mysteps(n - 2)
