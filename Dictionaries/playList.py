playList = {
	"Tile": "Patagonia bus",
	"Author": "Colt Steele",
	"Songs": [
		{"Tile": "Know me", "Artist": ["Blue"], "Duration": 2.5},
		{"Tile": "Meno", "Artist": ["Barry", "Djcd"], "Duration": 7.5},
		{"Tile": "Hello", "Artist": ["Garf"], "Duration": 4.5}

	]
}

total_lenght = 0
for song in playList["Songs"]:
	total_lenght += song["Duration"]
print(total_lenght)