import json

def convert_to_json(txt):
    try:
            
        if txt==''or txt is None:
            return "no text to convert"
        else:
            json_txt=json.dumps(txt)
            return json_txt
    except ValueError as e:
        print(e)