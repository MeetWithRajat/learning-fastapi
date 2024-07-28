from fastapi import FastAPI
from pydantic import Field, BaseModel


app = FastAPI()


class Book:
    def __init__(self, book_id: int, book_title: str, book_author: str, book_description: str, book_rating: float):
        """
        Constructs all the necessary attributes for the book object.

        :param book_id: Unique identifier for the book
        :param book_title: Title of the book
        :param book_author: Author of the book
        :param book_description: Description of the book
        :param book_rating: Rating of the book
        """
        self.id = book_id
        self.title = book_title
        self.author = book_author
        self.description = book_description
        self.rating = book_rating

    def __repr__(self):
        """
        Returns a string representation of the book object.
        """
        return (f"Book(id={self.id}, title={self.title!r}, author={self.author!r}, "
                f"description={self.description!r}, rating={self.rating})")

    def __str__(self):
        """
        Returns a readable string representation of the book object.
        """
        return f"'{self.title}' by {self.author} (Rating: {self.rating})"


books = [
    Book(1, "Python Pro", "Rajat Roy", "Advance Python for Professional", 4.5),
    Book(2, "Java Pro", "Srinjoy Ghosh", "Advance Java for Professional", 4.5),
    Book(3, "C# Pro", "Akash Das", "Advance C# for Professional", 4.3),
    Book(4, "AWS Pro", "Rajat Roy", "Advance Amazon Web Service for Professional", 4.4),
    Book(5, "DevOps Pro", "Sheron Samir Das", "Advance DevOps for Professional", 4.7),
    Book(6, "SE Pro", "Rajat Roy", "Advance Software Engineering for Professional", 4.3),
]


@app.get("/books")
async def read_all_books():
    return books


@app.post("/create_book")
async def create_a_book(book=Body()):
    books.append(book)
    return "Book added successfully"
