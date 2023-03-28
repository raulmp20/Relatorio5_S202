from database import Database
from model import BookModel

db = Database(database="relatorio5", collection="books")
db.resetDatabase()

book_model = BookModel(db)
id_book = book_model.create_book("Percy Jackson", "Rick Riordan", 2005, 45.90)
livro = book_model.read_book_by_id(id_book)

book_model.update_book(id_book, "Harry Potter", "J.K. Rowling", 1997, 19.90)
livro = book_model.read_book_by_id(id_book)

book_model.delete_book(id_book)
livro = book_model.read_book_by_id(id_book)

