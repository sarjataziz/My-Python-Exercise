users = [
		{"username": "Sarjat", "tweets": ["I love cake"]},
		{"username": "Aziz", "tweets": ["Heee..."]},
		{"username": "Rumi", "tweets": ["Yahh..."]},
		{"username": "Luffy", "tweets": ["Yahhooo..."]},
		{"username": "Naruto", "tweets": ["I will be Hokage one-day..."]},
		{"username": "Meliodas", "tweets": ["Hhhmm..."]},
		{"username": "Jaka", "tweets": []},
		{"username": "Kappa", "tweets": []},
		{"username": "Asta", "tweets": ["Ehhaaaa..."]},
		{"username": "Noelle", "tweets": []},
		{"username": "Kudu", "tweets": []}
		]
a = sorted(users, key = lambda user: user["username"])
print(a)
