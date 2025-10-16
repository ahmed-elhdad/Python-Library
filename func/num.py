from modules.library import Library
def num():
    enter =int(input("Enter number: \n"))
    if enter == 1:Library.add_book()
    if enter == 2:Library.borrow_book()
    if enter == 3:print(f"clicked {enter}")
    if enter == 4:print(f"clicked {enter}")
    if enter == 5:print(f"clicked {enter}")