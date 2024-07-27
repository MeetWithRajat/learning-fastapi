from fastapi import FastAPI


app = FastAPI()


books = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'Science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'Science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'History'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'Mathematics'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'Mathematics'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'Mathematics'},
]


@app.get("/hello")
async def welcome():
    return "Hello Rajat"


@app.get("/books")
async def read_all_books():
    return {"book list": books}


@app.get("/books/mybook")
async def favorite_book():
    return {"favourite book": "Sherlock Holmes"}


@app.get("/books/{book_title}")
async def read_book(book_title: str):
    for book in books:
        if book.get('title').casefold() == book_title.casefold():
            return book
    else:
        return {"error": "Book not available"}

