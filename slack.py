#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import time
from slackclient import SlackClient
import yaml
import datetime
import pytz
import json


global message_string

token = "ADD-YOUR-TOKEN"# found at https://api.slack.com/web#authentication
sc = SlackClient(token)

users = sc.api_call("users.list")
users_dict = users['members']    

def nom_utilisateur(id):
    for item in users_dict:
        if item['id'] == id:
            nom_user = item['name']
            return nom_user

def conversion_date(ts):
    ma_date = datetime.datetime.fromtimestamp(ts, tz=pytz.timezone('America/Montreal')).strftime('%d-%m-%Y %H:%M:%S')
    return ma_date

def reception_message():
    global message_string
    if sc.rtm_connect():
        while True:
            contenu_recu = sc.rtm_read()
            # Verify if the list list is not empty
            if contenu_recu:
                mon_dict = contenu_recu[0]
                
                # Change this line by adding the channel id that you want to select 
                if mon_dict['type'] == "message" and mon_dict['channel'] == "YOUR-CHANNEL-ID" and mon_dict['user']!="USLACKBOT":
                    message_string = nom_utilisateur(mon_dict["user"]) + "%,%" + mon_dict['text'] + "%,%" + conversion_date(float(mon_dict['ts']))
                    return message_string 
            time.sleep(1)
    else:
        return "Erreur de connexion" 

if __name__ == "__main__":
    reception_message()
    
