import requests
import json
import socket

import os

# ip_address = os.system(' ')
# api_key = 'f8c2cb364ca729d33ceee0dc67f0b907'
# hostname = socket.gethostname()    
# ip_address = socket.gethostbyname(hostname)    

ip_address = os.system('curl icanhazip.com')
exit_code = os.WEXITSTATUS(ip_address)
send_url = 'http://api.ipstack.com/'+ip_address+'?access_key=f8c2cb364ca729d33ceee0dc67f0b907'
r = requests.get(send_url)
j = json.loads(r.text)
lat = j['latitude']
lon = j['longitude']
print(ip_address)
print('helo')
 



