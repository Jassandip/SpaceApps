import requests
import json
import socket
from pprint import pprint
import os

# ip_address = os.system(' ')
# api_key = 'f8c2cb364ca729d33ceee0dc67f0b907'
# hostname = socket.gethostname()    
# ip_address = socket.gethostbyname(hostname)    
# accu_api_key = KRuZpazNMoj8092MhxsNNktct3rcpuEe



# send_url = 'https://api.weather.gov/alerts?point=31.79,-100.14'  
send_url = 'http://dataservice.accuweather.com/locations/v1/cities/geoposition/search?apikey=KRuZpazNMoj8092MhxsNNktct3rcpuEe&q=31.79%2C-100.14'
# send_url = 'https://api.weather.gov/alerts?severity=severe&point=31.79,-100.14'

# send_url = 'http://dataservice.accuweather.com/currentconditions/v1/locationKey?apikey=KRuZpazNMoj8092MhxsNNktct3rcpuEe'

# 'https://api.weather.gov/gridpoints/TOP/31,80'

r = requests.get(send_url)
j = json.loads(r.text)


# pprint(j)

a = j['Key']


send_url1 = 'http://dataservice.accuweather.com/currentconditions/v1/'+ a +'?apikey=KRuZpazNMoj8092MhxsNNktct3rcpuEe'

b = requests.get(send_url1)
c = json.loads(b.text)

pprint(c)
