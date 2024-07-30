import copy
from fastapi import FastAPI, Path, Query, HTTPException
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

    def update(self, book_title: str, book_author: str, book_description: str, book_rating: float):
        """
        Update the attributes for the book object.

        :param book_title: Title of the book
        :param book_author: Author of the book
        :param book_description: Description of the book
        :param book_rating: Rating of the book
        """
        self.title = book_title
        self.author = book_author
        self.description = book_description
        self.rating = book_rating


class BookRequest(BaseModel):
    book_title: str = Field(min_length=3, max_length=50)
    book_author: str = Field(min_length=2, max_length=25)
    book_description: str = Field(min_length=1, max_length=100)
    book_rating: float = Field(ge=0, le=5)

    model_config = {
        "json_schema_extra": {
            "example": {
                "book_title": "A new book title",
                "book_author": "Author name of the book",
                "book_description": "Description of the book",
                "book_rating": 4.5
            }
        }
    }


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


@app.get("/books/filer_book")
async def read_book_by_rating(book_rating: float = Query(ge=0, le=5)):
    books_to_return = []
    for book in books:
        if book.rating >= book_rating:
            books_to_return.append(book)
    return books_to_return


@app.get("/books/{book_id}")
async def read_book(book_id: int = Path(ge=1)):
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="book not found")


@app.post("/books/create_book")
async def create_a_book(book_request: BookRequest):
    book_id = 1 if len(books) == 0 else books[-1].id + 1
    books.append(Book(book_id, **book_request.model_dump()))
    return {"status": "successfully added the book", "book": books[-1]}


@app.put("/books/update_book")
async def update_a_book(book_request: BookRequest, book_id: int = Query(ge=1)):
    for book in books:
        if book.id == book_id:
            previously = copy.deepcopy(book)
            book.update(**book_request.model_dump())
            return {"status": "successfully updated the book", "update": {"previously": previously, "now": book}}
    raise HTTPException(status_code=404, detail="book not found")


@app.delete("/books/delete_book")
async def delete_a_book(book_id: int = Query(ge=1)):
    for index in range(len(books)):
        if books[index].id == book_id:
            previously = copy.deepcopy(books[index])
            books.pop(index)
            return {"status": "successfully deleted the book", "previously": previously}
    raise HTTPException(status_code=404, detail="book not found")
