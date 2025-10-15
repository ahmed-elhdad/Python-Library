import json

def convert_from_json(path,mode):
    try:
        with open(path,mode) as f:
            x=f.read()
            if x =='' or x is None:
                print("Empty Data to convert")
                return False
            python_txt=json.loads()
            return python_txt
    except Exception as e:
        raise e
    
        