from fastapi import FastAPI
from books import books


app = FastAPI()


@app.get("/books/{book_author}")
async def read_book_by_author(book_author: str):
    books_to_return = []
    for book in books:
        if book.get('author').casefold() == book_author.casefold():
            books_to_return.append(book)
    return books_to_return
