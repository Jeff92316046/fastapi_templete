from pydantic import BaseModel
from ..repositories.helloworld_repository import write_helloworld_into_json


class Item(BaseModel):
    hello: str
    world: str


def post_helloworld_controller(item: Item):
    helloworld_item = {item.hello: item.world}
    write_helloworld_into_json(item)
    return helloworld_item
