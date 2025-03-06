from schemas.book import Book
from schemas.availability import Availability
from fastapi import Response, status, HTTPException
books: dict[int, Book] = {}
response_headers={'content-type': 'application/json'}

def createBook(book: Book):
    if book.id in books:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f'Book Id: {book.id} already exists')
    books[book.id] = book
    return Response(content=book.model_dump_json(), status_code=status.HTTP_201_CREATED,
                    headers=response_headers)

def getBook(bookId: int):
    if bookId not in books:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No Book Exists with id: {bookId}')
    return Response(content=books[bookId].model_dump_json(), status_code=status.HTTP_200_OK,
                    headers=response_headers)

def updateAvailability(bookId: int, availability: Availability):
    if bookId not in books:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No Book Exists with id: {bookId}')
    books[bookId].available = availability.available
    return Response(content=books[bookId].model_dump_json(), status_code=status.HTTP_200_OK,
                    headers=response_headers)

def deleteBook(bookId: int):
    if bookId not in books:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No Book Exists with id: {bookId}')
    books.pop(bookId)
    return Response(content='Book Deleted Successfully!', status_code=status.HTTP_200_OK,
                    headers=response_headers)