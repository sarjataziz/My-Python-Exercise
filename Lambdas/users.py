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

list_of_inactive = list(map(lambda user: user["username"].upper(),
						filter(lambda u: not u["tweets"], users)))

print("The list of inactive users today : " ,list_of_inactive)

list_of_active = list(map(lambda user: user["username"].upper(),
						filter(lambda u: u["tweets"], users)))

print("The list of active users today : " ,list_of_active)

