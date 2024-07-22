import json
import os



def create_theme():
# Data to be written
    tmp_theme = {
        "name": "test theme",
        "pattern": "2coloralter",
        "numOfPixels":37,
        "color 1": "0,100,0",
        "color 2": "100,0,0"
    }
    
    # Serializing json
    data = json.dumps(tmp_theme, indent=4)
    print(data)
    if os.path.exists("themes"):
        ...
    else:
        os.mkdir("themes")
        
    with open('themes/tmp.json', 'w', encoding='utf-8') as f:
        f.write(data)

def get_theme(name):
    file = f"themes/{name}.json"
    if file:
        with open(file, 'r') as outputfile:
            return json.load(outputfile)
        
def get_config():
    pass

def edit_config(config):
    with open('config.json', 'w', encoding='utf-8') as f:
        f.write(config)
        
print(get_theme("tmp")) 

