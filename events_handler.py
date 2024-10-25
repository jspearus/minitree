import time
from datetime import datetime
import os
import json


# Define a list of weekdays
weekdays = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
next_event = {'name':'zzzzzzz', 'event-time':'23:59'}

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
    global next_event
    time_format = "%H:%M"
    files = os.listdir('events/')
    current_datetime = datetime.now()
    current_time = current_datetime.strftime("%H:%M")
    current_time = datetime.strptime(current_time, time_format).time()
    # print(f'time: {current_time}')
    for file in files:
        with open('events/'+file, 'r') as outputfile:
            event =json.load(outputfile)
            eventTime = datetime.strptime(event['event-time'], time_format).time()
            nextTime = datetime.strptime(next_event['event-time'], time_format).time()
            # todo need to find curent event
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
    
    
if __name__ == '__main__':
    # print(get_next_event())
    pass