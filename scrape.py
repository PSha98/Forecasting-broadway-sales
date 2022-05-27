# Write your code here :-)
from bs4 import BeautifulSoup
import requests
import time
import pandas as pd

year_url = "https://playbill.com/seasons?year=2010"
page = requests.get(year_url)

soup = BeautifulSoup(page.content, 'html.parser')
table = soup.find('table').tbody


        
play_name = [a.text.strip() for a in table.find_all('a') if a.parent['class'] == ['col-1']]
play_url = [a['href'] for a in table.find_all('a') if a.parent['class'] == ['col-1']]
play_type = []
for url in play_url:
    time.sleep(3)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    curr_play_type = [h5.text for h5 in soup.find_all('h5') if (h5['class'] == ['bsp-bio-sub-text']) and (h5.parent.parent['class']!= ['hidden-xs']) and (h5.text != 'Broadway')]
    play_type.append(curr_play_type)
show_type_data = pd.DataFrame({'Name':play_name,
                               'Type':play_type,
                               })