import os
from modules.library import Library
def num():
    enter =int(input("Enter number: \n"))
    if enter == 1: Library.show_books()
    if enter == 2:Library.add_book()
    if enter == 3:Library.borrow_book()
    if enter == 4:Library.delete_book()
    if enter == 5: os._exit()