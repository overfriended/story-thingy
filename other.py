import json

def _jsonToList(file):
    with open(file) as jsonfile:
        return json.load(jsonfile)

def get_list(name):
    return _jsonToList("stories.json")[name]
