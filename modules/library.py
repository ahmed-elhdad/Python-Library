from modules.book import Book
from func.check_exit import books
from func import check_exit
from func.write_txt import write_txt
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
        year=input('Enter year: \n')
        count=input('Enter count: \n')
        book_status=check_exit.check_exit_book(title,count)
        if title == '' or author=='':
            print('Empty Data')
            return 0
            # Will add the func to handle the books exits
        else:
            if book_status == True:
                print(count)
            else:
                new_book=Book(title,author,year,count)
                books.append(new_book.__dict__)
                write_txt("data/books.json","r+",books)