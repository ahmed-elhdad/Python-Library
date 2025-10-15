import json
from func.empty_file import empty_file
def convert_from_json(path,mode):
    try:
        with open(path,mode) as f:
            x=f.read()
            if x =='' or x is None:
                print("Empty Data to convert")
                return False
            python_txt=json.loads(x)
            return python_txt
        empty_file(path)
    except Exception as e:
        raise e