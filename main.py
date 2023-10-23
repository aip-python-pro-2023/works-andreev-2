import tabulate
import requests
import json

with open('data.json') as file:
    data = json.load(file)

print(data['name'])
print(data['contacts']['telegram'])

data['contacts']['vk'] = 'bakasa'

with open('result.json', 'w') as result:
    json.dump(data, result, indent=2)
