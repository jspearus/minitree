import time
from datetime import datetime
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
    
def get_next_event():
    time_format = "%H:%M"
    files = os.listdir('events/')
    next_event = {'event-time':'23:59'}
    current_datetime = datetime.now()
    current_time = current_datetime.strftime("%H:%M")
    current_time = datetime.strptime(current_time, time_format).time()
    # print(f'time: {current_time}')
    for file in files:
        with open('events/'+file, 'r') as outputfile:
            event =json.load(outputfile)
            eventTime = datetime.strptime(event['event-time'], time_format).time()
            nextTime = datetime.strptime(next_event['event-time'], time_format).time()
            if eventTime < nextTime and eventTime > current_time:
                next_event = event
    return next_event
    
def get_all_events():
    folder_path = 'events/'
    files = os.listdir(folder_path)
    events = []
    for file in files:
        events.append(file.split('.')[0])
    return events
    
def edit_event(file):
    data = json.dumps(file, indent=4)
    with open(f"events/{file['name']}.json", 'w', encoding='utf-8') as f:
        f.write(data)
    
def delete_event(name):
    file = f"events/{name}.json"
    if file:
        os.remove(file)
    
    
if __name__ == '__main__':
    # print(get_next_event())
    pass