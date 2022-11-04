import requests, json
from poke_api.src.pokemon import Pokemon

def fill_pokedex(result):
    pokemons = list()
    for item in result:
        item_url = item['url']
        item_api = requests.get(item_url)
        item_data = item_api.text
        parse_item = json.loads(item_data)
        name = parse_item['name']
        types = list()
        abilities = list()
        for type in parse_item['types']:
            types.append(type['type']['name'])
        
        for ability in parse_item['abilities']:
            abilities.append(ability['ability']['name'])
        
        pokemons.append(Pokemon(name, types, abilities))
    return pokemons