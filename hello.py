import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
resp = requests.get('http://assamcollegecode.info/ASSAMCOLLEGECODE_files/iframe/provincialisedcolleges.html')
txt = resp.text


soup = BeautifulSoup(txt,'html.parser')

lists = soup.select('li > p > a')

for ol in lists:
    try:
        college_url = ol.attrs['href']
        nap = ol.text.split(' – ')
        name = nap[0].split(',')[0].strip()
        full_address = nap[0].split(',')[1].strip() + ', ' + nap[0].split(',')[2].strip()
        college_district = nap[0].split(',')[2].strip()
        pin = nap[1].strip().replace(' ','')
        with open('index.csv', 'a') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([name,full_address, college_district,pin,college_url])
    except IndexError:
        continue