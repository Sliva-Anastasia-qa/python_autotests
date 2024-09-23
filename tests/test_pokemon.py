import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '8c2c1a709f29edf2658d417cc0bce5a7'
HEADER = {'Content-Type': 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '10674'


def test_status_code():
    response = requests.get(url = f'https://api.pokemonbattle.ru/v2/trainers', params={'trainer_id' : TRAINER_ID})
    assert response.status_code == 200