import requests

def get_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)

    # HTTPリクエストが成功時は200
    if response.status_code == 200:
        data = response.json()
        print(f"ポケモン名: {data['name'].capitalize()}")
        print(f"ID: {data['id']}")
        print("タイプ:", ", ".join([t['type']['name'] for t in data['types']]))
        print("高さ:", data['height'])
        print("重さ:", data['weight'])
        print("能力値:", ", ".join([a['ability']['name'] for a in data['abilities']]))
    else:
        print("ポケモンが見つかりませんでした。")

print("-------------------")
# ピカチュウのデータを取得
get_pokemon_data("pikachu")
print("-------------------")
# ゲンガーのデータを取得
get_pokemon_data("gengar")
print("-------------------")
