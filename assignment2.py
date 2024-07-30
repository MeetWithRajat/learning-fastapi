from fastapi import FastAPI
from book_self import Book, BookRequest


app = FastAPI()


class Published(Book):
    def __init__(self, book_id: int, book_title: str, book_author: str,
                 book_description: str, book_rating: float, publish_year: int):
        super().__init__(book_id, book_title, book_author, book_description, book_rating)
        self.year = publish_year


class PublishRequest(BookRequest):
    publish_year: int

    model_config = {
        "json_schema_extra": {
            "example": {
                "book_title": "A new book title",
                "book_author": "Author name of the book",
                "book_description": "Description of the book",
                "book_rating": 4.5,
                "publish_year": 2015
            }
        }
    }


books = [
    Published(1, "Python Pro", "Rajat Roy", "Advance Python for Professional", 4.5, 2021),
    Published(2, "Java Pro", "Srinjoy Ghosh", "Advance Java for Professional", 4.5, 2022),
    Published(3, "C# Pro", "Akash Das", "Advance C# for Professional", 4.3, 2023),
    Published(4, "AWS Pro", "Rajat Roy", "Advance Amazon Web Service for Professional", 4.4, 2024),
    Published(5, "DevOps Pro", "Sheron Samir Das", "Advance DevOps for Professional", 4.7, 2015),
    Published(6, "SE Pro", "Rajat Roy", "Advance Software Engineering for Professional", 4.3, 2018),
]


@app.get("/books/filter_year")
async def filter_book_by_year(year: int):
    books_to_return = []
    for book in books:
        if book.year == year:
            books_to_return.append(book)
    return books_to_return
