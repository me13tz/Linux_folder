#!/home/USERNAME/anaconda3/bin/python3.4
import requests, bs4

res = requests.get('https://weather.yahoo.com/united-states/washington/seattle-12798961/')
if res.status_code != requests.codes.ok:
    print("May want to try downloading again - there was a problem.")
    exit()

wSoup = bs4.BeautifulSoup(res.text)
p_tags = wSoup.select('p')
today = str(p_tags[0])
tomorrow = str(p_tags[1])

print("Today's forecast from Yahoo Weather is:\n"+today[16:-4])
print("Tomorrow's forecast from Yahoo Weather is:\n"+tomorrow[16:-4])
