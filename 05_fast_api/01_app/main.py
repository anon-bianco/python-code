from fastapi import FastAPI, HTTPException
from model import Item

app = FastAPI()

@app.get("/")
def root():
  return {"Hello": "World"}

items = []

# Add item to list and also return all items
@app.post("/items")
def create_items(item: Item):
  items.append(item)
  return items

# Pull an item based on index
@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int) -> Item:
  if item_id < len(items):
    item = items[item_id]
  else:
    raise HTTPException(status_code=404, detail=f"Item {item_id} not found")  
  return item