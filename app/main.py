from fastapi import FastAPI
from app.routers import books, auth
app = FastAPI()

app.include_router(books.router, prefix="/books")
app.include_router(auth.router, prefix="/auth")

@app.get("/")
def read_root():
    return {"Hello": "World"}
