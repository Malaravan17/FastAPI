from pydantic import BaseModel


class Detail(BaseModel):
    name: str
    age: int
    home: str
