from fastapi import APIRouter
from models.book import Book, CreateBook
from fastapi import HTTPException


router = APIRouter(tags=['Books'])

books = [
    {"id": 1, "name": "The Hobbit", "author": "<NAME>"},
    {"id": 2, "name": "The Lord of the Rings", "author": "<NAME>"},
]


@router.get("/")
def get_books() -> list[Book]:
    return books


@router.get("/{id}")
def get_book_by_id(id: int) -> Book:
    for book in books:
        if (book.get('id') == id):
            return book

    raise HTTPException(status_code=404, detail="Book not found")


@router.post("/")
def create_book(book: CreateBook) -> Book:
    created_book = {
        "id": len(books) + 1,
        "name": book.name,
        "author": book.author
    }
    books.append(created_book)
    return created_book


@router.delete("/{id}")
def delete_book(id: int) -> None:
    for book in books:
        if (book.get('id') == id):
            books.remove(book)
            return

    raise HTTPException(status_code=404, detail="Book not found")


@router.put("/{id}")
def update_book(id: int, book: CreateBook) -> Book:
    for book in books:
        if (book.get('id') == id):
            book['name'] = book.name
            book['author'] = book.author
            return book

    raise HTTPException(status_code=404, detail="Book not found")
