#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 02:15:35 2022

@author: gautam
"""

from bs4 import BeautifulSoup
import requests
import time
import pandas as pd
import numpy as np

year_url = "https://playbill.com/seasons?year="
names = []
dates = []
year = []

for i in range(1985,2022):
     if i != 2020:   
        end = str(i)
        page = requests.get(year_url + end)
        
        time.sleep(3)
        soup = BeautifulSoup(page.content, 'html.parser')
        print(i)
        table = soup.find('table').tbody
        names.extend([a.text.strip() for a in table.find_all('a') if a.parent['class'] == ['col-1']])
        year.extend([int(end) for _ in range(len(names))])
        dates.extend([pd.to_datetime(a.text.strip()).date() for a in table.find_all('a') if a.parent['class'] == ['col-2']])
show_date_data = pd.DataFrame({'Year': year,
                            'Name':names,
                           'Opening Date':dates
                           })
show_date_data.to_csv('show_date_data.csv')