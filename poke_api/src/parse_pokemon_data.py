import json, requests

def parse_pokemon_data(result):
    for item in result:
        item_url = item['url']
        item_api = requests.get(item_url)
        item_data = item_api.text
        parse_item = json.loads(item_data)
        name = parse_item['name']
        types = list()
        for type in parse_item['types']:
            types.append(type['type']['name'])
        print(name)
        print(types)