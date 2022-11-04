from fastapi import FastAPI
import json, requests
from poke_api.src.fill_pokedex import fill_pokedex


from poke_api.src.pokemon import Pokemon

app = FastAPI()

URL = 'https://pokeapi.co/api/v2/pokemon/'
pokemons = list()


response_API = requests.get(URL)
data = response_API.text
parse_json = json.loads(data)
info = parse_json['results']
pokemons = fill_pokedex(info)


@app.get("/pokemons")
def pokedex():
     
    return pokemons
