import json

class MyIterator:

    def __init__(self, path):
        self.path = path
        self.file = open(self.path, encoding='utf-8')
        self.cities_names_list = []

        with open('countries.json') as f:
            file = json.load(f)
            for c in file:
                self.cities_names_list.append(c['name']['common'])

    def __iter__(self):
        return self

    def __next__(self):
        try:
            city = self.cities_names_list.pop(0)
        except IndexError:
            raise StopIteration

        return city

with open('result.txt', 'w') as upload:
    for city in MyIterator('countries.json'):
        try:
            upload.write(f"{city} : https://wikipedia.org/wiki/{city.replace(' ', '_')}\n")
            print(f"{city} : https://wikipedia.org/wiki/{city.replace(' ', '_')}")
        except UnicodeEncodeError:
            pass