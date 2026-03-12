from fastapi import Depends, APIRouter
from database_models import DetailDB
from schemas import Detail
from database import get_db


router = APIRouter()


@router.post("/info")
def add_info(detail: Detail, db=Depends(get_db)):
    new_detail = DetailDB(
        name=detail.name,
        age=detail.age,
        home=detail.home
    )

    db.add(new_detail)
    db.commit()
    return "Details Added"


@router.get("/info")
def get_info(id: int, db=Depends(get_db)):
    person = db.query(DetailDB).filter(DetailDB.id == id).first()

    if person is None:
        return {"error": "ID not found"}

    return person


@router.put("/info")
def update_info(id: int, updated_details: Detail, db=Depends(get_db)):
    person = db.query(DetailDB).filter(DetailDB.id == id).first()

    if person is None:
        return {"error": "ID not found"}

    person.name = updated_details.name
    person.age = updated_details.age
    person.home = updated_details.home

    db.commit()

    return "Updated Details"


@router.delete("/info")
def delete_info(id: int, db=Depends(get_db)):
    person = db.query(DetailDB).filter(DetailDB.id == id).first()

    if person is None:
        return {"error": "ID not found"}

    db.delete(person)
    db.commit()

    return "Deleted Details"