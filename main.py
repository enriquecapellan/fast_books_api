from typing import List
from fastapi import FastAPI, HTTPException
from models.book import Book, CreateBook

app = FastAPI()


books = [
    {"id": 1, "title": "The Hobbit", "author": "<NAME>"},
    {"id": 2, "title": "The Lord of the Rings", "author": "<NAME>"},
]


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/books")
def get_books() -> list[Book]:
    return books


@app.get("/books/{id}")
def get_book_by_id(id: int) -> Book:
    for book in books:
        if (book.get('id') == id):
            return book

    raise HTTPException(status_code=404, detail="Book not found")


@app.post("/books")
def create_book(book: CreateBook) -> Book:
    created_book = {
        "id": len(books) + 1,
        "title": book.name,
        "author": book.author
    }
    books.append(created_book)
    return created_book
