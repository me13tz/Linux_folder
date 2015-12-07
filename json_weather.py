#!/home/cassius/anaconda3/bin/python3.4

import requests, sys, json, re

d=0
h=0
T=0
w=0

##Compute location from command line argument:
if len(sys.argv) < 2:
    print()
    print("Please enter a city on the command line.")
    print()
    sys.exit()
location = ' '.join(sys.argv[1:])
apikey = 'YOUR_API_KEY_HERE'

###Use with city id (from list of city id's from openweather.org):
#url = 'http://api.openweathermap.org/data/2.5/forecast/city?id=524901&APPID=YOUR_API_KEY_HERE'

###Use with command line arugment city search:
url = 'http://api.openweathermap.org/data/2.5/forecast/city?q={}&APPID=YOUR_API_KEY_HERE'.format(location)

###convert degrees Kelvin to Farenheit
def k_to_f(T):
    tmp_k = wData[T]['main']['temp']
    tmp_f = tmp_k*(9/5)-459.67
    tmp_f = round(tmp_f,1)
    t = 'Current temperature: '+str(tmp_f)+' F'
    return t
###get humidity and convert to string output
def humidity(h):
    hum = wData[h]['main']['humidity']
    humidity = 'Humidity '+str(hum)+'%'
    return humidity
###convert from meters/sec to mph
def windspeed(w):
    wind = wData[w]['wind']['speed']
    wind = round(wind*2.23694,1)
    windspeed = 'Winds at '+str(wind)+'mph'
    return windspeed

response = requests.get(url)
wData = json.loads(response.text)
wData = wData['list']
print()

###get current description
def w_desc(d):
    x = wData[d]['weather'][0]['main'], '-' ,wData[d]['weather'][0]['description']
    x = re.sub("[(,')]", '', str(x))
    return x

def w_format(hour):
    global h, d, T, w
    d = int(hour)
    T = int(hour)
    h = int(hour)
    w = int(hour)
    print(w_desc(d))
    print(k_to_f(T))
    print(humidity(h))
    print(windspeed(w))
    print()
###The API has 3-hour chunks of information. So zero is current weather, 8 
###is 3x8 hours or 24 hours away, and 16 is 3x16 hours or 48 hours away:
print('The current weather in {}:'.format(location))
w_format(0)
print('Tomorrow:')
w_format(8)
print('Day After Tomorrow:')
w_format(16)
