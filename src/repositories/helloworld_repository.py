import json
from pydantic import BaseModel


class Item(BaseModel):
    hello: str
    world: str


def get_helloworld_from_json():
    with open("data/helloworld.json", "r") as file:
        return json.load(file)


def write_helloworld_into_json(item: Item):
    with open("data/helloworld.json", "r") as file:
        dict_t = json.load(file)
    dict_t[item.hello] = item.world
    json_obj = json.dumps(dict_t)
    with open("data/helloworld.json", "w") as file:
        file.write(json_obj)
