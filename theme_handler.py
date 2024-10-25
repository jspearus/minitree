import json
import os



def create_theme(file):
    # Serializing json
    data = json.dumps(file, indent=4)
    if os.path.exists("/home/jeff/minitree/themes"):
        ...
    else:
        os.mkdir("/home/jeff/minitree/themes")
    
    with open(f"/home/jeff/minitree/themes/{file['name']}.json", 'w', encoding='utf-8') as f:
        f.write(data)

def get_theme(name):
    file = f"/home/jeff/minitree/themes/{name}.json"
    if file:
        with open(file, 'r') as outputfile:
            return json.load(outputfile)
def get_all_themes():
    folder_path = '/home/jeff/minitree/themes/'
    files = os.listdir(folder_path)
    themes = []
    for file in files:
        themes.append(file.split('.')[0])
    return themes
        
def delete_theme(name):
    file = f"/home/jeff/minitree/themes/{name}.json"
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

