from func.convert_to_json import convert_to_json
def find_book(title,c):
    for x in c:
        if x['title'] == title:
            convert_to_json(c)
            x['count']-=1
            return True
        else:
            return 'not found'