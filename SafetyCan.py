#!/usr/bin/env python3

from flask import Flask,render_template,request,session,Blueprint
import requests
import json
from pprint import pprint
import pandas as pd
import os
import math
from collections import Counter


x = 'https://freegeoip.app/json/' 
r = requests.get(x) #makes api call and reutrns ip address and coordinates
x = json.loads(r.text)
longitude = str(x['longitude'])
latitude = str(x['latitude'])


url = 'https://api.weather.gov/alerts?active=1&severity=severe&point='+latitude+','+longitude
call = requests.get(url)
coordinate_info = json.loads(call.text)


try:
    print(coordinate_info['features'][0]['properties']['event'])
except IndexError:
    print("N/A")

check_list = {'AR': 'Severe Storm(s)', 'ND': 'Flood', 'PA': 'Hurricane', 'WI': 'Severe Storm(s)', 'NJ': 'Severe Storm(s)', 'KY': 'Severe Storm(s)', 'CA': 'Fire', 'TN': 'Severe Storm(s)', 'PR': 'Hurricane', 'LA': 'Hurricane', 'AK': 'Severe Storm(s)', 'WA': 'Fire', 'VA': 'Hurricane', 'MD': 'Hurricane', 'GA': 'Severe Storm(s)', 'IA': 'Severe Storm(s)', 'SD': 'Severe Storm(s)', 'WV': 'Severe Storm(s)', 'NH': 'Severe Storm(s)', 'NE': 'Severe Storm(s)', 'OK': 'Fire', 'VT': 'Severe Storm(s)', 'MS': 'Severe Storm(s)', 'ME': 'Severe Storm(s)', 'RI': 'Severe Storm(s)', 'IL': 'Severe Storm(s)', 'NM': 'Fire', 'MN': 'Severe Storm(s)', 'SC': 'Hurricane', 'DE': 'Hurricane', 'AL': 'Severe Storm(s)', 'FL': 'Hurricane', 'AZ': 'Fire', 'NC': 'Hurricane', 'CO': 'Fire', 'ID': 'Flood', 'NY': 'Severe Storm(s)', 'OH': 'Severe Storm(s)', 'CT': 'Severe Storm(s)', 'WY': 'Flood', 'MA': 'Severe Storm(s)', 'MI': 'Severe Storm(s)', 'OR': 'Severe Storm(s)', 'KS': 'Severe Storm(s)', 'MO': 'Severe Storm(s)', 'DC': 'Hurricane', 'GU': 'Typhoon', 'TX': 'Fire', 'NV': 'Fire', 'HI': 'Severe Storm(s)', 'AS': 'Hurricane', 'UT': 'Fire', 'IN': 'Severe Storm(s)', 'MP': 'Typhoon', 'MT': 'Fire', 'VI': 'Hurricane'}








url_past = 'https://www.fema.gov/api/open/v1/FemaWebDisasterDeclarations'
call = requests.get(url_past)
past_disasters = json.loads(call.text)


incidents = []
for i in range(len(past_disasters['FemaWebDisasterDeclarations'])):
    incidents.append(past_disasters['FemaWebDisasterDeclarations'][i]['incidentType'])
    

states = []
for i in range(len(past_disasters['FemaWebDisasterDeclarations'])):
    states.append(past_disasters['FemaWebDisasterDeclarations'][i]['stateCode'])


dates = []
for i in range(1000):
    abc = past_disasters['FemaWebDisasterDeclarations'][i]['incidentBeginDate']
    cde = abc[:10]
    dates.append(cde)


final = []
for i in range(len(dates)):
    final.append([states[i],incidents[i],dates[i]])
df = pd.DataFrame(final)
df.index +=1
df.columns = ['State','Incident','Date']     #includes commonwealth territories


df1 = df.loc[lambda df: df['State'] == 'NY']


df1 = df1.sort_values(by=['Incident'], ascending=False)


x = list(df1['Incident'])
print(Counter(x).most_common())
check_list = {'AR': 'Severe Storm(s)', 'ND': 'Flood', 'PA': 'Hurricane', 'WI': 'Severe Storm(s)', 'NJ': 'Severe Storm(s)', 'KY': 'Severe Storm(s)', 'CA': 'Fire', 'TN': 'Severe Storm(s)', 'PR': 'Hurricane', 'LA': 'Hurricane', 'AK': 'Severe Storm(s)', 'WA': 'Fire', 'VA': 'Hurricane', 'MD': 'Hurricane', 'GA': 'Severe Storm(s)', 'IA': 'Severe Storm(s)', 'SD': 'Severe Storm(s)', 'WV': 'Severe Storm(s)', 'NH': 'Severe Storm(s)', 'NE': 'Severe Storm(s)', 'OK': 'Fire', 'VT': 'Severe Storm(s)', 'MS': 'Severe Storm(s)', 'ME': 'Severe Storm(s)', 'RI': 'Severe Storm(s)', 'IL': 'Severe Storm(s)', 'NM': 'Fire', 'MN': 'Severe Storm(s)', 'SC': 'Hurricane', 'DE': 'Hurricane', 'AL': 'Severe Storm(s)', 'FL': 'Hurricane', 'AZ': 'Fire', 'NC': 'Hurricane', 'CO': 'Fire', 'ID': 'Flood', 'NY': 'Severe Storm(s)', 'OH': 'Severe Storm(s)', 'CT': 'Severe Storm(s)', 'WY': 'Flood', 'MA': 'Severe Storm(s)', 'MI': 'Severe Storm(s)', 'OR': 'Severe Storm(s)', 'KS': 'Severe Storm(s)', 'MO': 'Severe Storm(s)', 'DC': 'Hurricane', 'GU': 'Typhoon', 'TX': 'Fire', 'NV': 'Fire', 'HI': 'Severe Storm(s)', 'AS': 'Hurricane', 'UT': 'Fire', 'IN': 'Severe Storm(s)', 'MP': 'Typhoon', 'MT': 'Fire', 'VI': 'Hurricane'}


    
    

