l = [1,2,3,4,5,6,7,8,9,0,10]
even = list(filter(lambda x: x % 2 == 0, l))

print(even)

n = ["aa", "bs", "ad", "we", "eg", "at"]
a_n = list(filter(lambda y: y[0] == "a", n))
print(a_n)