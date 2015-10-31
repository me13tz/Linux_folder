#!/home/USERNAME/anaconda3/bin/python3.4
import requests, bs4

###download the weather report from Yahoo
res = requests.get('https://weather.yahoo.com/united-states/washington/seattle-12798961/')
if res.status_code != requests.codes.ok:
    print("May want to try downloading again - there was a problem.")
    exit()
    
###create a BeautifulSoup object and search for pertinent elements, assign variables
wSoup = bs4.BeautifulSoup(res.text)
p_tags = wSoup.select('p')
today = str(p_tags[0])
tomorrow = str(p_tags[1])
span = wSoup.select('div span')
x = str(span[8])
print()

###slice and dice for clean output
print("Current temperature: "+x[34:36]+"\n")
print("From Yahoo Weather:\n"+today[16:-4]+"\n")
print(tomorrow[16:-4]+"\n") 
