import json
import os



def create_theme(file):
    # Serializing json
    data = json.dumps(file, indent=4)
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
    with open('config.json', 'r') as outputfile:
            return json.load(outputfile)

def edit_config(config):
    with open('config.json', 'w', encoding='utf-8') as f:
        f.write(config)
        
        
if __name__ == '__main__':
    tmp = {
        "name": "test theme",
        "pattern": "2coloralter",
        "numPerGroup":1,
        "color 1": "0,100,0",
        "color 2": "100,0,0"
    }
    # create_theme(tmp)
    # print(get_theme("tmp"))
    # print(get_config())
    pass 

