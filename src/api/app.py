
from fastapi import APIRouter
from ..controllers.get_helloworld import get_helloworld_contorller
helloworld = APIRouter(tags=["helloworld"])

@helloworld.get("/helloworld")
def get_helloworld():
    return get_helloworld_contorller()