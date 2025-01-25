from flask import Flask, jsonify, request
import requests
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)

# URL base da API pública do Pokémon
POKEAPI_BASE_URL = "https://pokeapi.co/api/v2/pokemon/"

@app.route('/pokemon/<name>', methods=['GET'])
def get_pokemon(name):
    


    
    import requests

def get_apod():
    """
    Obter a imagem astronômica do dia (APOD) da API da NASA e exibir no terminal.
    """
    NASA_API_URL = "https://api.nasa.gov/planetary/apod"
    API_KEY = ""  # Substitua por sua própria chave de API 

    params = {
        'api_key': API_KEY,  # Chave de API fornecida pela NASA
    }

    response = requests.get(NASA_API_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        print(f"Título: {data['title']}")
        print(f"Data: {data['date']}")
        print(f"Descrição: {data['explanation']}")
        print(f"URL da imagem: {data['url']}")
    else:
        print("Erro: Não foi possível obter os dados da NASA.")

if __name__ == '__main__':
    get_apod()
    """
    Obter informações de um Pokémon pelo nome.
    ---
    parameters:
      - name: name
        in: path
        type: string
        required: true
        description: Nome do Pokémon
    responses:
      200:
        description: Retorna as informações do Pokémon
        schema:
          id: pokemon
          properties:
            name:
              type: string
              description: Nome do Pokémon
            height:
              type: integer
              description: Altura do Pokémon
            weight:
              type: integer
              description: Peso do Pokémon
    """
    response = requests.get(f"{POKEAPI_BASE_URL}{name.lower()}")
    
    if response.status_code == 200:
        data = response.json()
        return jsonify({
            "name": data["name"],
            "height": data["height"],
            "weight": data["weight"]
        })
    else:
        return jsonify({"error": "Pokémon não encontrado."}), 404

@app.route('/pokemon/id/<int:id>', methods=['GET'])
def get_pokemon_by_id(id):
    """
    Obter informações detalhadas de um Pokémon pelo ID.
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID do Pokémon
    responses:
      200:
        description: Retorna as informações detalhadas do Pokémon
        schema:
          id: pokemon
          properties:
            name:
              type: string
              description: Nome do Pokémon
            abilities:
              type: array
              items:
                type: string
              description: Habilidades do Pokémon
            types:
              type: array
              items:
                type: string
              description: Tipos do Pokémon
    """
    response = requests.get(f"{POKEAPI_BASE_URL}{id}")
    
    if response.status_code == 200:
        data = response.json()
        return jsonify({
            "name": data["name"],
            "abilities": [ability["ability"]["name"] for ability in data["abilities"]],
            "types": [ptype["type"]["name"] for ptype in data["types"]]
        })
    else:
        return jsonify({"error": "Pokémon não encontrado."}), 404

if __name__ == '__main__':
    app.run(debug=True)
