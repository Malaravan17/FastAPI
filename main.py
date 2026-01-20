from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def greet():
    return "Hello Peanut"


class Detail(BaseModel):
    id: int
    name: str
    age: int
    home: str


details_db = [
    Detail(id=1, name="malar", age=19, home="harur"),
    Detail(id=2, name="rishi", age=19, home="annur"),
    Detail(id=5, name="kavin", age=19, home="dindugal"),
    Detail(id=4, name="amir", age=19, home="palani"),
]


@app.get("/info/{id}")
def get_info(id: int):
    for person in details_db:
        if person.id == id:
            return person
    return {"error": "ID not found"}


@app.post("/info")
def add_info(new_detail: Detail):
    details_db.append(new_detail)
    return new_detail

@app.put("/info")
def update_info(id:int,updated_detail:Detail):
    for i in range(len(details_db)):
        if details_db[i].id == id:
            details_db[i] = updated_detail
            return "Product updated"
        
@app.delete("/info")
def delete_info(id:int):
    for i in range(details_db):
        if details_db[i].id==id:
            del details_db[i]
            return "Product deleted"