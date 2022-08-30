import requests
from random import choice

user_input = input("What would you like to search for? \n")
url = "https://icanhazdadjoke.com/search"
response = requests.get(
						url, 
						headers={"Accept": "application/json"},
						params={"term": user_input}
					).json()

num_jokes = response["total_jokes"]
results = response["results"]
if num_jokes > 1:
	print(f"I found {num_jokes} jokes about {user_input}. Here's one: ")
	print(choice(results)["joke"])
elif num_jokes == 1:
	print(f"I found one joke about {user_input}. Here it is: ")
	print(results[0]['joke'])
else:
	print(f"Sorry, couldn't find any joke with your term: {user_input}")


#print(response)