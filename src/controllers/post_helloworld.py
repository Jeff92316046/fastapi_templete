from pydantic import BaseModel

class Item(BaseModel):
    hello : str
    world : str

def post_helloworld_controller(item: Item):
    helloworld_item ={
        item.hello : item.world 
    }
    return helloworld_item