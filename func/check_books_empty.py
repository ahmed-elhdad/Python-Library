from func.check_exit import books
from func.convert_from_json import convert_from_json


def books_empty():
    if books ==[] or books is None:
        convert_from_json("../data/books.json","r+")
        print(books)