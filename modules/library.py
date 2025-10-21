from modules.book import Book
from func import convert_from_json
from func import check_exit
from func import empty_file
from func import write_txt
from func import find_book
json_text=convert_from_json.convert_from_json("data/books.json","r+")
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
        
    def show_books():
        print("show books")
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
                full_count=25
                if count>full_count:
                    print("The data is full ^^")
                    print("will create it with 25 number of books")
                    count=25
                new_book=Book(title,author,True,year,count)
                books.append(new_book.__dict__)
                empty_file.empty_file("data/books.json")
                write_txt.write_txt('data/books.json','r+',books)
    def borrow_book():
        title=input("Enter Book Title: \n")
        x=find_book.find_book(title,books)
        if x == 'not found':
            print('not found Book ^^')
            return
        else:
            find_book.find_book(title,books)
            empty_file('data/books.json')
            write_txt('data/books.json','w',books)
            if write_txt == True:
                print(f'you are borrowed the book called {title}')
                
    def delete_book():
        try:
            
            title = input("Enter Book title: \n").strip()
            if len(books) == 0:
                print("No books")
            else:
                book=find_book.find_book(title,books)
                if book =='not found':
                    print('not found book ^^')
                    return
                del books[book]
                print(books)
                empty_file.empty_file('data/books.json')
                if len(books)>0:
                    write_txt.write_txt('data/books.json','r+',books)
                else:
                    return
                
        except Exception as e:
            print("Error: ",e)