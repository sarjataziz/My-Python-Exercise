nums = [1,2,3,4,5,6,7,8,9,0]
double = list(map(lambda x: x*2, nums))

 #''' for x in double:
 #   print(x) '''

names = [
    {"first": "Rusty", "last": "Boom"},
    {"first": "Raa", "last": "Phha"}
]

first_names = list(map(lambda x: x["first"], names))

print(first_names)