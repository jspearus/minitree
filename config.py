import json
import os



def get_config():
    with open('config.json', 'r') as outputfile:
            return json.load(outputfile)

def edit_config(config):
    with open('config.json', 'w', encoding='utf-8') as f:
        f.write(config)