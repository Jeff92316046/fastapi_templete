import json
def get_helloworld_from_json():
    with open('data/helloworld.json','r') as file:
        return json.load(file)
