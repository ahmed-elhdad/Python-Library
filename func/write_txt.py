from func.convert_to_json import convert_to_json
from func.check_exit import books
from func.empty_file import empty_file
def write_txt(path,mode,txt):
    try:
            
        with open(path,mode) as f:
            json_txt=convert_to_json(txt)
            if json_txt=='' or json_txt is None:
                print("no thing to write")
            else:
                if len(books) > 1 or len(books) == 1:
                    empty_file(path)
                f.write(json_txt)
                return True
    except Exception as e:
        print ("Error: ",e)