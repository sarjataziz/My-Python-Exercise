class A:
	def __init__(self):
		print("Method Defined In: A")

class B(A):
	def __init__(self):
		print("Method Defined In: B")

class C(A):
	def __init__(self):
		print("Method Defined In: C")

class D(B,C):
	pass

print(D.__mro__)
print()
print(D.mro())
print()
print(help(D))


		
		
		
		