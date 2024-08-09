import time, datetime
import os
import json


# Define a list of weekdays
weekdays = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

def create_event(file):
    # Serializing json
    data = json.dumps(file, indent=4)
    if os.path.exists("events"):
        ...
    else:
        os.mkdir("events")
    
    with open(f"events/{file['name']}.json", 'w', encoding='utf-8') as f:
        f.write(data)
    
def get_event(name):
    file = f"events/{name}.json"
    if file:
        with open(file, 'r') as outputfile:
            return json.load(outputfile)
    
def get_all_events():
    ...
    
def edit_event(file):
    data = json.dumps(file, indent=4)
    with open(f"events/{file['name']}.json", 'w', encoding='utf-8') as f:
        f.write(data)
    
def delete_event(name):
    file = f"events/{name}.json"
    if file:
        os.remove(file)
    
    
if __name__ == '__main__':
    day = datetime.datetime.now().weekday()
    print(weekdays[day])
    pass