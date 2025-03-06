from fastapi import APIRouter
from schemas.book import Book
from schemas.availability import Availability
from services import book_service

router = APIRouter()

@router.post('/')
def createNewBook(book: Book):
    return book_service.createBook(book)

@router.get('/{bookId}')
def getBookById(bookId: int):
    return book_service.getBook(bookId)

@router.patch('/{bookId}')
def updateAvailability(bookId: int, availability: Availability):
    return book_service.updateAvailability(bookId, availability)

@router.delete('/{bookId}')
def deleteBookById(bookId: int):
    return book_service.deleteBook(bookId)