books=[]

def check_exit_book(title,count):
    for x in books:
        if x['title']==title:
            print("exit")
            x['count']+=count
            print(books)
            return True