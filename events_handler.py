import time
import threading
from datetime import datetime
import os
import json

from ctrl import displayTheme, off
from theme_handler import  create_theme, get_all_themes
from config import get_config, edit_config

connected = True
autoMode = ''
# Define a list of weekdays
weekdays = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
next_event = {'name':'zzzzzzz', 'event-time':'23:59'}
curEvent = ''

def create_event(file):
    # Serializing json
    data = json.dumps(file, indent=4)
    if os.path.exists("/home/jeff/minitree/events"):
        ...
    else:
        os.mkdir("/home/jeff/minitree/events")
    
    with open(f"/home/jeff/minitree/events/{file['name']}.json", 'w', encoding='utf-8') as f:
        f.write(data)
    
def get_next_event():
    global next_event, curEvent

    time_format = "%H:%M"
    files = os.listdir('/home/jeff/minitree/events/')
    current_datetime = datetime.now()
    current_time = current_datetime.strftime("%H:%M")
    current_time = datetime.strptime(current_time, time_format).time()
    # print(f'time: {current_time}')
    for file in files:
        with open('/home/jeff/minitree/events/'+file, 'r') as outputfile:
            event =json.load(outputfile)
            eventTime = datetime.strptime(event['event-time'], time_format).time()
            nextTime = datetime.strptime(next_event['event-time'], time_format).time()
            print(f"eventtime: {eventTime}, nextTime: {nextTime}, curentTime: {current_time}")
            # todo need to find curent event
            print(f"eventname: {event['name']}")
            print(f"curEvent: {curEvent}")
            if event['name'] != curEvent:
                if eventTime < nextTime and eventTime > current_time:
                    print(f'UPDATED: {current_time}')
                    next_event = event
                
    return next_event
    
def get_all_events():
    folder_path = '/home/jeff/minitree/events/'
    files = os.listdir(folder_path)
    events = []
    for file in files:
        events.append(file.split('.')[0])
    return events
    
def edit_event(file):
    data = json.dumps(file, indent=4)
    with open(f"/home/jeff/minitree/events/{file['name']}.json", 'w', encoding='utf-8') as f:
        f.write(data)
    
def delete_event(name):
    file = f"/home/jeff/minitree/events/{name}.json"
    if file:
        os.remove(file)
        
def update_datetime():  # runs in thread
    time_format = "%H:%M"
    global connected, curEvent, autoMode
    event = get_next_event()
    while connected:
        cur_day = datetime.now()
        global autoMode
    config = get_config()
    autoMode = config['auto_mode']
    # print(f"Current Day: {cur_day.day}")
    # print(f"Current Month: {cur_day.month}")
    # print(f"Current time: {cur_day.hour}:{cur_day.minute}:{cur_day.second}")
    if autoMode ==  "on":
        eventTime = datetime.strptime(event['event-time'], time_format).time()
        # print(f"curtTime: {cur_day.time()}")
        # print(f"eventTime: {eventTime}")
        if eventTime <= cur_day.time():
            
            themes = get_all_themes()
            print("going")
            print(f"event: {event['name']}") 
        
            if event['name'] != curEvent:
                if event['themeSelect'] in themes or event['themeSelect'] == 'off':
                    print("go")
                    curEvent = event['name']
                    print(f"current event: {curEvent}")
                    displayTheme(event['themeSelect'])
                    displayTheme(event['themeSelect'])
            event = get_next_event()
            print(f"new event: {event['name']}") 
        else:
            event = get_next_event()
            # print(f"new event: {event['name']}") 
            # eventTime = datetime.strptime(event['event-time'], time_format).time()
            # print(f"new event: {event}")
            # print(f"eventTime: {eventTime}")
    time.sleep(1)

def runUpdateDatetime():
    datetime_updater = threading.Thread(target=update_datetime, args=())
    # datetime_updater.setDaemon(True)
    datetime_updater.start()
    
    
if __name__ == '__main__':
    print(f"OUTPUT: {get_next_event()}")
    # pass