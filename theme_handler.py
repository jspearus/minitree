import json
import os
from config import get_config

ledType = ''

def update_config():
    global autoMode, ledType
    config = get_config()
    ledType = config['led_type']
    
def create_theme(file):
    config = get_config()
    file_path = config['FILE_PATH']
    # Serializing json
    data = json.dumps(file, indent=4)
    if os.path.exists(f"{file_path}themes"):
        ...
    else:
        os.mkdir(f"{file_path}themes")
    
    with open(f"{file_path}themes/{file['name']}.json", 'w', encoding='utf-8') as f:
        f.write(data)

def get_theme(name):
    config = get_config()
    file_path = config['FILE_PATH']
    print(f"file NAME: {name}")
    file = f"{file_path}themes/{name}.json"
    if file:
        with open(file, 'r') as outputfile:
            return json.load(outputfile)

def edit_theme(file):
    config = get_config()
    file_path = config['FILE_PATH']
    data = json.dumps(file, indent=4)
    print(f"edit file: {data}")
    with open(f"{file_path}themes/{file['name']}.json", 'w', encoding='utf-8') as f:
        f.write(data)
        
def get_all_themes():
    config = get_config()
    file_path = config['FILE_PATH']
    folder_path = f'{file_path}themes/'
    files = os.listdir(folder_path)
    themes = []
    for file in files:
        themes.append(file.split('.')[0])
    return themes
        
def delete_theme(name):
    config = get_config()
    file_path = config['FILE_PATH']
    file = f"{file_path}themes/{name}.json"
    if file:
        os.remove(file)
            
if __name__ == '__main__':
    tmp = {
        "pattern": "multicolor",
        "numOfColor":2,
        "numPerGroup":1,
        "color 1": "0,100,0",
        "color 2": "100,0,0"
    }
    tmp2 = {
        "pattern": "solid",
        "color": "0,100,0",
    }
    # create_theme(tmp2)
    # print(get_theme("tmp"))
    # print(get_config())
    pass 

