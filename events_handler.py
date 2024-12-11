import time
import threading
from datetime import datetime
import os
import json


from ctrl import displayTheme, off
from theme_handler import get_all_themes
from config import get_config, edit_config

connected = True
autoMode = ''
# Define a list of weekdays
weekdays = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
next_event = {'name':'zzzzzzz', 'event_time':'23:59'}
curEvent = ''

def create_event(file):
    # Serializing json
    config = get_config()
    file_path = config['FILE_PATH']
    data = json.dumps(file, indent=4)
    if os.path.exists(f"{file_path}events"):
        ...
    else:
        os.mkdir(f"{file_path}events")
    
    with open(f"{file_path}events/{file['name']}.json", 'w', encoding='utf-8') as f:
        f.write(data)
    
def get_next_event():
    global next_event, curEvent
    config = get_config()
    file_path = config['FILE_PATH']

    time_format = "%H:%M"
    files = os.listdir(f'{file_path}events/')
    current_datetime = datetime.now()
    current_time = current_datetime.strftime("%H:%M")
    current_time = datetime.strptime(current_time, time_format).time()
    # print(f'time: {current_time}')
    for file in files:
        with open(f'{file_path}events/'+file, 'r') as outputfile:
            event =json.load(outputfile)
            eventTime = datetime.strptime(event['event_time'], time_format).time()
            nextTime = datetime.strptime(next_event['event_time'], time_format).time()
            if event['name'] != curEvent:
                if eventTime < nextTime and eventTime > current_time:
                    print(f'UPDATED: {current_time}')
                    next_event = event
                
    return next_event
    
def get_all_events():
    config = get_config()
    file_path = config['FILE_PATH']
    folder_path = f'{file_path}events/'
    files = os.listdir(folder_path)
    events = []
    for file in files:
        with open(f'{file_path}events/'+file, 'r') as outputfile:
            event =json.load(outputfile)
            events.append(event)
    return events

def get_event_list():
    global next_event, curEvent
    config = get_config()
    file_path = config['FILE_PATH']
    folder_path = f'{file_path}events/'
    files = os.listdir(folder_path)
    events = []
    for file in files:
        events.append(file.split('.')[0])
    return events
    
def edit_event(file):
    config = get_config()
    file_path = config['FILE_PATH']
    data = json.dumps(file, indent=4)
    with open(f"{file_path}events/{file['name']}.json", 'w', encoding='utf-8') as f:
        f.write(data)
    
def delete_event(name):
    config = get_config()
    file_path = config['FILE_PATH']
    file = f"{file_path}events/{name}.json"
    if file:
        os.remove(file)
        
def update_datetime():  # runs in thread
    global connected, curEvent, autoMode
    time_format = "%H:%M"
    while connected:
        events = get_all_events()
        cur_day = datetime.now().strftime(time_format)
        global autoMode
        config = get_config()
        autoMode = config['auto_mode']
        if autoMode ==  "on":
            for event in events[:]:  # Iterate over a copy of the list
                if event["event_time"] == cur_day and event["name"] != curEvent:  # Check if the current time matches the event time
                    displayTheme(event['themeSelect'])
                    curEvent = event["name"]
                    print(f"curent event: {curEvent}")
                    if event["freq"] == "once":
                        delete_event(event["name"]) 
        time.sleep(1)

def runUpdateDatetime():
    datetime_updater = threading.Thread(target=update_datetime, args=())
    # datetime_updater.setDaemon(True)
    datetime_updater.start()
    
    
if __name__ == '__main__':
    print(f"OUTPUT: {get_next_event()}")
    # pass