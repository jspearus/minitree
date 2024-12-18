#!/usr/bin/env python
# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, render_template, request, jsonify, redirect, url_for
from waitress import serve
import threading
import os, time, subprocess
from datetime import datetime
from datetime import timedelta
import json

import subprocess
from screen import refreshScreen
from ctrl import displayTheme, off
from theme_handler import  create_theme, get_all_themes, get_theme, delete_theme, edit_theme
from events_handler import create_event, get_next_event, get_all_events, get_event, runUpdateDatetime, delete_event
from config import get_config, edit_config


numb = 1
RST = None
connected = True
curEvent = ''
autoMode = ''
ledType = ''
PORT = 7233


# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)

        
def update_config():
    global autoMode, ledType
    config = get_config()
    autoMode = config['auto_mode']
    ledType = config['led_type']
    print(f"auto Mode: {autoMode}")

@app.route('/', methods=['GET', 'POST'])
def index():
    global PORT
    config = get_config()
    device_name = config['device_name']
    themes = get_all_themes()
    events = get_all_events()
    nextEvent = get_next_event()
    cmd = "hostname -I | cut -d\' \' -f1"
    IP = IP = subprocess.check_output(cmd, shell = True ).decode('ASCII')
    refreshScreen()
    return render_template('index.html', themes=themes,  
                           events=events, nextEvent=nextEvent, 
                           IP=IP, PORT=PORT, device=device_name)
    
@app.route('/config', methods=['GET', 'POST'])
def config():
    cmd = "hostname -I | cut -d\' \' -f1"
    IP = IP = subprocess.check_output(cmd, shell = True ).decode('ASCII')
    config = get_config()
    if request.method == 'POST':
        data = request.get_json()
        file = json.loads(data)
        edit_config(file)
        refreshScreen()
    return render_template('config.html', config=config, IP=IP, PORT=PORT)

@app.route('/ctrl', methods=['POST'])
def ctrl():
    themes = get_all_themes()
    data = request.get_json()
    if data['cmd'] == 'clear':
        off()
        print('off')
    elif data['cmd'] in themes:
        displayTheme(data['cmd'])
    return jsonify({'status': 'success'})

@app.route('/system', methods=['GET', 'POST'])
def system():
    cmd = "hostname -I | cut -d\' \' -f1"
    IP = IP = subprocess.check_output(cmd, shell = True ).decode('ASCII')
    
    return render_template('system.html', IP=IP, PORT=PORT)

@app.route('/syscom/<string:command>', methods=['GET', 'POST'])
def syscom(command):
    cmd = "hostname -I | cut -d\' \' -f1"
    IP = IP = subprocess.check_output(cmd, shell = True ).decode('ASCII')
    # todo create reboot and shutdown functions
    if command == 'reboot':
        subprocess.run(["sudo", "reboot", "now"], check=True)
    elif command == 'shutdown':
        subprocess.run(["sudo", "shutdown", "now"], check=True)
    return render_template('system.html', IP=IP, PORT=PORT)

# ####################### Themes #####################
@app.route('/themes', methods=['GET', 'POST'])
def themes():
    cmd = "hostname -I | cut -d\' \' -f1"
    IP = IP = subprocess.check_output(cmd, shell = True ).decode('ASCII')
    themes = get_all_themes()
    themes.append('off')
    return render_template('themes.html', themes=themes,
                           IP=IP, PORT=PORT)

@app.route('/newtheme', methods=['GET', 'POST'])
def newtheme():
    cmd = "hostname -I | cut -d\' \' -f1"
    IP = IP = subprocess.check_output(cmd, shell = True ).decode('ASCII')
    themes = get_all_themes()
    if request.method == 'POST':
        data = request.get_json()
        file = json.loads(data)
        if file['pattern'] == 'solid':
            # convert2rgb(file, 'color1')
            del file['numPerGroup']
            del file['color2']
            del file['color3']
            create_theme(file)
        elif file['pattern'] == '2Color':
            # convert2rgb(file, 'color1')
            # convert2rgb(file, 'color2')
            del file['color3']
            create_theme(file)
        elif file['pattern'] == '3Color':
            # convert2rgb(file, 'color1')
            # convert2rgb(file, 'color2')
            # convert2rgb(file, 'color3')
            create_theme(file)
        print("lodaed")
        return redirect(url_for('themes'))
    return render_template('new_theme.html', themes=themes,
                            IP=IP, PORT=PORT)
    
@app.route('/edittheme/<string:theme_name>', methods=['GET', 'POST'])
def edittheme(theme_name):
    cmd = "hostname -I | cut -d\' \' -f1"
    IP = IP = subprocess.check_output(cmd, shell = True ).decode('ASCII')
    print(f"request type: {request.method}")
    theme = get_theme(theme_name)
    
    # todo not getting past here when i try to update the theme
    if request.method == 'POST':
        print('HERE')
        pattern = request.form.get('pattern')
        numPerGroup = request.form.get('numPerGroup')
        color1 = request.form.get('color1')
        color2 = request.form.get('color2')
        color3 = request.form.get('color3')
        print(f'patern: {pattern}')
        print(f'color1: {color1}')
        if pattern == 'solid':
            # convert2rgb(color1, 'dec')
            data={
                "name": theme_name, 
                "pattern": pattern,
                "color1": color1
            }
            edit_theme(data)
            print('updated')
        elif pattern == '2Color':
            # convert2rgb(color1, 'dec')
            # convert2rgb(color2, 'dec')
            data={
                "name": theme_name, 
                "pattern": pattern,
                "numPerGroup": numPerGroup,
                "color1": color1,
                "color2": color2
            }
            edit_theme(data)
            print('updated2')
        return redirect(url_for('themes'))
        # elif pattern == '3Color':
        #     convert2rgb(file, 'color1')
        #     convert2rgb(file, 'color2')
        #     convert2rgb(file, 'color3')
        #     edit_theme(file)
        
        
    else:
        if theme['pattern'] == 'solid':
            # convert2hex(theme, 'color1')
            theme['numPerGroup'] = '1'
            theme['color2'] = '#000000'
            theme['color3'] = '#000000'
        elif theme['pattern'] == '2Color':
            # convert2hex(theme, 'color1')
            # convert2hex(theme, 'color2')
            theme['color3'] = '#000000'
        elif theme['pattern'] == '3Color':
            ...
            # convert2hex(theme, 'color1')
            # convert2hex(theme, 'color2')
            # convert2hex(theme, 'color3')
    
    # todo convert rgb values to hex before displaying them
    
    return render_template('edit_theme.html', theme=theme,
                           IP=IP, PORT=PORT)
    
@app.route('/deltheme/<string:theme_name>', methods=['GET', 'POST'])
def del_theme(theme_name):
    cmd = "hostname -I | cut -d\' \' -f1"
    IP = IP = subprocess.check_output(cmd, shell = True ).decode('ASCII')
    delete_theme(theme_name)
    themes = get_all_themes()
    themes.append('off')
    return render_template('themes.html', themes=themes,
                           IP=IP, PORT=PORT)
    
# ###################  Events ############################

@app.route('/events', methods=['GET', 'POST'])
def events():
    cmd = "hostname -I | cut -d\' \' -f1"
    IP = IP = subprocess.check_output(cmd, shell = True ).decode('ASCII')
    if request.method == 'POST':
        data = request.get_json()
        file = json.loads(data)
        create_event(file)
    events = get_all_events()
    themes = get_all_themes()
    themes.append('off')
    return render_template('event.html', themes=themes,
                          events=events, IP=IP, PORT=PORT)

@app.route('/newevent', methods=['GET', 'POST'])
def new_event():
    cmd = "hostname -I | cut -d\' \' -f1"
    IP = IP = subprocess.check_output(cmd, shell = True ).decode('ASCII')
    if request.method == 'POST':
        data = request.get_json()
        file = json.loads(data)
        create_event(file)
        return render_template('event.html', themes=themes,
                          events=events, IP=IP, PORT=PORT)
    themes = get_all_themes()
    themes.append('off')
    return render_template('new_event.html', themes=themes,
                           IP=IP, PORT=PORT)
    
@app.route('/editevent/<string:event_name>', methods=['GET', 'POST'])
def edit_event(event_name):
    cmd = "hostname -I | cut -d\' \' -f1"
    IP = IP = subprocess.check_output(cmd, shell = True ).decode('ASCII')
    event = get_event(event_name)
    themes = get_all_themes()
    themes.append('off')
    return render_template('edit_event.html', event=event, themes=themes,
                           IP=IP, PORT=PORT)

@app.route('/delevent/<string:event_name>', methods=['GET', 'POST'])
def del_event(event_name):
    cmd = "hostname -I | cut -d\' \' -f1"
    IP = IP = subprocess.check_output(cmd, shell = True ).decode('ASCII')
    delete_event(event_name)
    themes = get_all_themes()
    events = get_all_events()
    themes.append('off')
    return render_template('event.html', events=events, themes=themes,
                           IP=IP, PORT=PORT)



if __name__ == '__main__':
    refreshScreen()
    update_config()
    themes = get_all_themes()
    runUpdateDatetime()
    serve(app, host='0.0.0.0', port=PORT)
    
