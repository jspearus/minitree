import json
import os



def get_config():
    if os.path.exists("/home/mini/minitree/themes"):
        with open('/home/jeff/minitree/config.json', 'r') as outputfile:
                return json.load(outputfile)
    elif os.path.exists("/home/jeff/minitree/themes"):
        with open('/home/jeff/minitree/config.json', 'r') as outputfile:
                return json.load(outputfile)

def edit_config(config):
    config = get_config()
    file_path = config['FILE_PATH']
    with open(f'{file_path}config.json', 'w', encoding='utf-8') as f:
        f.write(config)
