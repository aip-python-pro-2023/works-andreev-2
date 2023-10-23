import requests

data = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu')
if data.ok:
    print('Success')
    pikachu = data.json()
    print(pikachu['name'])
    print(pikachu['height'])
    print(pikachu['weight'])
else:
    print('Failed!')

region_id = input('Enter region ID: ')
region = requests.get(f'https://pokeapi.co/api/v2/region/{region_id}/').json()

for name in region['names']:
    if name['language']['name'] == 'en':
        print('Region', name['name'])
        break

print('Locations:')
for location in region['locations']:
    print(location['name'])
