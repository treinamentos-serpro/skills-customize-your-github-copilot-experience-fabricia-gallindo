from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="Books API")


class BookInput(BaseModel):
    title: str
    author: str


class Book(BookInput):
    id: int


books: dict[int, Book] = {
    1: Book(id=1, title="The Hobbit", author="J. R. R. Tolkien"),
    2: Book(id=2, title="Frankenstein", author="Mary Shelley"),
}


@app.get("/books", response_model=list[Book])
def list_books() -> list[Book]:
    return list(books.values())


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int) -> Book:
    book = books.get(book_id)
    if book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found",
        )
    return book


@app.post(
    "/books",
    response_model=Book,
    status_code=status.HTTP_201_CREATED,
)
def create_book(book_input: BookInput) -> Book:
    book_id = max(books, default=0) + 1
    book = Book(id=book_id, **book_input.model_dump())
    books[book_id] = book
    return book


@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book_input: BookInput) -> Book:
    if book_id not in books:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found",
        )
    book = Book(id=book_id, **book_input.model_dump())
    books[book_id] = book
    return book


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int) -> None:
    if book_id not in books:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found",
        )
    del books[book_id]
