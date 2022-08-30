from functools import wraps

def ensure_first_arg_is(arg):
	def inner(fn):
		@wraps(fn)
		def wrapper(*args, **kwargs):
			if args and args[0] != arg:
				return f"First arg needs to be {arg}"
			return fn(*args, **kwargs)
		return wrapper
	return inner


@ensure_first_arg_is("Lum")
def fav_foods(*foods):
	print(foods)

print(fav_foods("Lum", "Ice cream"))
print(fav_foods("Ice cream", "Lum"))

