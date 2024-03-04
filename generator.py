import requests


def get_numbers():
    x = 1
    while True:
        yield x
        x += 1


def get_people():
    url = 'https://swapi.dev/api/people'
    while url is not None:
        data = requests.get(url).json()
        for person in data['results']:
            yield person
        url = data['next']


# filter
# map
# enumerate
# zip

for x in filter(lambda p: p['height'] != 'unknown' and int(p['height']) >= 180, get_people()):
    print(x)

print('---')

for x in map(lambda p: p['name'], get_people()):
    print(x)
