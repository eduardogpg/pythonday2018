import requests

url = 'https://pokeapi.co/api/v2/pokemon/'

if __name__ == '__main__':

    response = requests.get(url)

    if response.ok:
        json = response.json()
        pokemons = json.get('results', [])

        for index, pokemon in enumerate(pokemons):
            name = pokemon.get('name', '')
            print("> {} - {} ".format(index, name))

        pokemon = input("\nIngresa el nombre de un pokemon : ")

        url = url + pokemon

        response = requests.get(url)
        
        if response.ok:
            json = response.json()
            abilities = json.get('abilities', [])

            print("\nHabilidades ({}):".format(pokemon))

            for ability in abilities:
                name = ability['ability']['name']
                print("* {}".format(name))
