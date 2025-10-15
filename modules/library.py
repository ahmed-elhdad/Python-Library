from modules.book import Book
from func.check_exit import books
from func import check_exit
from func.write_txt import write_txt
from func.convert_from_json import convert_from_json
from func.empty_file import empty_file
json_text=convert_from_json("data/books.json","r+")
if type(json_text)==bool:
    print("Empty file from lib")
    
else:
    print("Empty file from lib")
    books = json_text
    
class Library:
    def __init__(self,title,author,available,count,year):
        self.title=title
        self.author=author
        self.available=available
        self.count=count
        self.year=year
    def add_book():
        title=input('Enter title: \n')
        author=input('Enter author: \n')
        year=int(input('Enter year: \n'))
        count=int(input('Enter count: \n'))
        book_status=check_exit.check_exit_book(title,count)
        if title == '' or author=='':
            print('Empty Data')
            return 0
        else:
            print(book_status)
            if book_status == True:
                check_exit.check_exit_book(title,count)
                print('exited book')
                return 
            else:
                new_book=Book(title,author,True,year,count)
                books.append(new_book.__dict__)
                empty_file("data/books.json")
                write_txt('data/books.json','r+',books)
