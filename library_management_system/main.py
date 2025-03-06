from fastapi import FastAPI
from routes import book
import uvicorn


app = FastAPI(title='Library Management System')
app.include_router(book.router, prefix='/api/v1/books', tags=['books'])

if __name__ == '__main__':
    print('Api is exposing on /api/v1/books')
    uvicorn.run(app, port=8000)
