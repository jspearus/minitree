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
    from events_handler import get_all_events, delete_event
    config = get_config()
    events = get_all_events()
    file_path = config['FILE_PATH']
    file = f"{file_path}themes/{name}.json"
    if file:
        for event in events:
            if event['themeSelect'] == name:
                delete_event(event['name'])
        os.remove(file)
            
if __name__ == '__main__':
    # create_theme(tmp2)
    # print(get_theme("tmp"))
    # print(get_config())
    pass 

