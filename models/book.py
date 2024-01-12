from pydantic import BaseModel


class Book(BaseModel):
    id: int
    name: str
    author: str

class CreateBook(BaseModel):
    name: str
    author: str

