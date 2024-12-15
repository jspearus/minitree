import json
import os
from config import get_config

ledType = ''

def update_config():
    global autoMode, ledType
    config = get_config()
    ledType = config['led_type']
    print(f"auto Mode: {autoMode}")
    
def convert2hex(file, key):
    global ledType
    update_config()
    color = file[key]
    color = color[1:] if len(color) > 1 else ""
    print(f'decvalue: {color}')
    colors = []
    hex_colors = []
    for i in range(0, len(color), 2):
        colors.append(color[i:i+2])
    for color in colors:
        hexcolor = hex(color)
        hex_colors.append(hexcolor)
    print(f'type: {ledType}')
    if ledType == 'rgb':
        color = f"#{hex_colors[0]}{hex_colors[1]}{hex_colors[2]}"
    elif ledType == 'grb':
        color = f"#{hex_colors[1]}{hex_colors[0]}{hex_colors[2]}"
    print(f'hexvalue: {color}')
    file[key] = color
    
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
    file = f"{file_path}themes/{name}.json"
    if file:
        with open(file, 'r') as outputfile:
            return json.load(outputfile)
        
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

