import threading
import os, time
from datetime import datetime
from datetime import timedelta
import json

from ctrl import displayTheme, off
from theme_handler import  create_theme, get_all_themes
from events_handler import create_event, get_next_event, get_all_events
from config import get_config, edit_config

connected = True
curEvent = ''
autoMode = ''

def update_datetime():  # runs in thread
    time_format = "%H:%M"
    global connected, curEvent, autoMode
    event = get_next_event()
    while connected:
        cur_day = datetime.now()
        update_config()
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
        
def update_config():
    global autoMode
    config = get_config()
    autoMode = config['auto_mode']
        
def runUpdateDatetime():
    datetime_updater = threading.Thread(target=update_datetime, args=())
    # datetime_updater.setDaemon(True)
    datetime_updater.start()