from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)

def test_given_concret_pokemon_name_when_call_api_then_comprove_if_contains():
    response = client.get("/pokemons")
    assert {
        "name": "bulbasaur",
        "types": [
            "grass",
            "poison"
            ],
        "abilities": [
            "overgrow",
            "chlorophyll"
            ]
        } in response.json() 

def test_comprove_if_json_length_is_20():
    response = client.get("/pokemons")
    assert len(response.json()) == 20

def test_response_code():
    response = client.get("/pokemons")
    assert response.status_code == 200