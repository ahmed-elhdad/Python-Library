from func.convert_to_json import convert_to_json
def find_book(title,c):
    try:
        
        if len(c) == 0:
            return 'not found'
        for x in range(len(c[:len(c)])):
            if c[x]['title'] == title:
                convert_to_json(c)
                c[x]['count']-=1
                return int(x)
            else:
                return 'not found'
    except Exception as e:
        print("Error: ",e)