import json
import os
file_path = ''


def get_config():
    global file_path
    if os.path.exists("/home/mini/minitree/themes"):
        with open('/home/mini/minitree/config.json', 'r') as outputfile:
            file_path= '/home/mini/minitree/'
            return json.load(outputfile)
    elif os.path.exists("/home/jeff/minitree/themes"):
        with open('/home/jeff/minitree/config.json', 'r') as outputfile:
            file_path= '/home/jeff/minitree/'
            return json.load(outputfile)

def edit_config(config):
    global file_path
    try:
        # Step 1: Read the JSON file
        with open(f'{file_path}config.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        # Step 2: Update the fields
        for key, value in config.items():
            data[key] = value
        
        # Step 3: Write the updated data back to the file  
        with open(f'{file_path}config.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
            
    except FileNotFoundError:
        print(f"Error: {file_path} does not exist.")
    except json.JSONDecodeError:
        print(f"Error: {file_path} is not a valid JSON file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        