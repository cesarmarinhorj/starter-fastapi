from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
from faker import Faker

app = FastAPI()
# data
fake = Faker()
items = [{'id': i+1, 'name': fake.name(), 'email': fake.email(), 'job': fake.job()} for i in range(10)]

class Item(BaseModel):
    id: int
    name: str
    email: str
    job: str


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return FileResponse('favicon.ico')


@app.get("/item/{id}")
async def read_item(id: int):
    item = items[id-1]
    return item


@app.get("/items/")
async def list_items():
    return items


@app.post("/items/")
async def create_item(item: Item):
    return item
