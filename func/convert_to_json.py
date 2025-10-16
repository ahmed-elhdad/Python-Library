import json

def convert_to_json(txt):
    try:
            
        if txt==''or txt is None:
            return "no text to convert"
        else:
            json_txt=json.dumps(txt,indent=4)
            return json_txt
    except ValueError as e:
        print(e)