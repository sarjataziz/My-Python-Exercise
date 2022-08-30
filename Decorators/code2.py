from functools import wraps

def log_function_data(fn):
	''' HHHHHH'''
	@wraps(fn)
	def wrapper(*args, **kwargs):
		print(f"you are avout to call {fn.__name__}")
		print(f"Here's the documentation: {fn.__doc__}")
		return fn(*args, **kwargs)
	return wrapper

@log_function_data
def add(x,y):
	'''aaaa'''
	return x + y 

print(add.__doc__)
print(add.__name__)