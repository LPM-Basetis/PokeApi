from fastapi import FastAPI
import json, requests

app = FastAPI()

class Pokemon:
    def __init__(self, name: str, ):
        self.name = name

response_API = requests.get('https://pokeapi.co/api/v2/pokemon/')
data = response_API.text
parse_jason = json.loads(data)
info = parse_jason['results']


@app.get("/pokemons")
def pokedex():
    pokemons = []
    for item in info:

        pokemons.append(Pokemon(item['name']))
    
    return pokemons
