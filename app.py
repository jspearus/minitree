#!/usr/bin/env python
# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, render_template, request, jsonify
from waitress import serve
import threading
import os, time
from datetime import datetime
from datetime import timedelta
import json

import subprocess
from screen import refreshScreen
from ctrl import displayTheme, off
from theme_handler import  create_theme, get_all_themes
from events_handler import create_event, get_next_event, get_all_events
from config import get_config, edit_config
from scheduler import runUpdateDatetime


numb = 1
RST = None
connected = True
curEvent = ''
autoMode = ''
ledType = ''


# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)

        
def update_config():
    global autoMode, ledType
    config = get_config()
    autoMode = config['auto_mode']
    ledType = config['led_type']
    print(f"auto Mode: {autoMode}")


def convert2rgb(file, key):
    global ledType
    update_config()
    color = file[key]
    color = color[1:] if len(color) > 1 else ""
    colors = []
    dec_colors = []
    for i in range(0, len(color), 2):
        colors.append(color[i:i+2])
    for color in colors:
        color = int(color, 16)
        dec_colors.append(color)
    print(f'type: {ledType}')
    if ledType == 'rgb':
        color = f"{dec_colors[0]},{dec_colors[1]},{dec_colors[2]}"
    elif ledType == 'grb':
        color = f"{dec_colors[1]},{dec_colors[0]},{dec_colors[2]}"
    file[key] = color
    
# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/', methods=['GET', 'POST'])
def index():
    themes = get_all_themes()
    events = get_all_events()
    nextEvent = get_next_event()
    return render_template('index.html', themes=themes,  events=events, nextEvent=nextEvent)

@app.route('/themes', methods=['GET', 'POST'])
def themes():
    themes = get_all_themes()
    if request.method == 'POST':
        data = request.get_json()
        # todo convert color value from hex to RGB
        file = json.loads(data)
        if file['pattern'] == 'solid':
            convert2rgb(file, 'color1')
            del file['numPerGroup']
            del file['color2']
            del file['color3']
            create_theme(file)
        elif file['pattern'] == '2Color':
            convert2rgb(file, 'color1')
            convert2rgb(file, 'color2')
            del file['color3']
            create_theme(file)
        elif file['pattern'] == '3Color':
            convert2rgb(file, 'color1')
            convert2rgb(file, 'color2')
            convert2rgb(file, 'color3')
            create_theme(file)
    return render_template('themes.html', themes=themes)

@app.route('/config', methods=['GET', 'POST'])
def config():
    config = get_config()
    return render_template('config.html', config=config)

@app.route('/events', methods=['GET', 'POST'])
def events():
    if request.method == 'POST':
        data = request.get_json()
        file = json.loads(data)
        create_event(file)   
    themes = get_all_themes()
    themes.append('off')
    return render_template('event.html', themes=themes)

@app.route('/ctrl', methods=['POST'])
def ctrl():
    themes = get_all_themes()
    data = request.get_json()
    if data['cmd'] == 'clear':
        off()
        print('off')
    elif data['cmd'] in themes:
        displayTheme(data['cmd'])
        displayTheme(data['cmd'])
    return jsonify({'status': 'success'})


if __name__ == '__main__':
    refreshScreen()
    update_config()
    themes = get_all_themes()
    runUpdateDatetime()
    serve(app, host='0.0.0.0', port=8080)
    
