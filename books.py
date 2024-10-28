from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

# class Book:
#     id: int
#     title: str
#     author: str
#     description: str
#     rating: int
    
#     def __init__(self, id, title, author, description, rating):
#         self.id = id
#         self.title = title
#         self.author = author
#         self.description = description
#         self.rating = rating
    
       
# class BookRequest(BaseModel):
#     id: int
#     title: str = Field(min_length=3)
#     author: str = Field(min_length=3)
#     description: str = Field(min_length=3, max_length=100)
#     rating: int = Field(ge=1, le=5)

# BOOKS = [
#     Book(1, 'Book 1', 'Rene K.', 'First published book', 2),
#     Book(2, 'Book 2', 'Rene K.', 'Second published book', 3),
#     Book(3, 'Book 3', 'Rene K.', 'First published book', 5),
#     Book(4, 'Book 4', 'AMK', 'First published book by AMK', 1),
#     Book(5, 'Book 5', 'Leon K.', 'First published book by Leon', 5)
# ]

# @app.get("/books")
# async def get_all_books():
#     return BOOKS
