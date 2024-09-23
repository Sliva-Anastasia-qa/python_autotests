import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '8c2c1a709f29edf2658d417cc0bce5a7'
HEADER = {'Content-Type': 'application/json', 'trainer_token' : TOKEN}

body_create = {
    "name": "asdf",
    "photo_id": 1
}

body_name = {
    "pokemon_id": "73898",
    "name": "Бублик"
}

body_pokeball = {
    "pokemon_id": "73898"
}

# response = requests.post(url = f'https://api.pokemonbattle.ru/v2/pokemons', headers = HEADER , json = body_create)
# print(response.text)

#response_create = requests.put(url = f'https://api.pokemonbattle.ru/v2/pokemons', headers = HEADER , json = body_name)
#print(response_create.text)

response = requests.post(url = f'https://api.pokemonbattle.ru/v2/trainers/add_pokeball', headers = HEADER , json = body_pokeball)
print(response.text)