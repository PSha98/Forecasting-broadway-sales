# Write your code here :-)
from bs4 import BeautifulSoup
import requests
import time
import pandas as pd

year_url = "https://playbill.com/seasons?year="
name = []
genre = []
awards = []
nominations = []
wins = []
performances  = []

for i in range(1985,2019):
    end = str(i)
    page = requests.get(year_url + end)
#page = requests.get("https://playbill.com/seasons?year=2010")
    time.sleep(1)
    soup = BeautifulSoup(page.content, 'html.parser')
    print(i)
    table = soup.find('table').tbody
    names_in_year = [a.text.strip() for a in table.find_all('a') if a.parent['class'] == ['col-1']]
    url_in_year = [a['href'] for a in table.find_all('a') if a.parent['class'] == ['col-1']]
    genre_in_year = []
    awards_in_year = []
    wins_in_year = []
    nominations_in_year = []
    performances_in_year = []
    for url in url_in_year:
        time.sleep(1)
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        curr_genre = [h5.text for h5 in soup.find_all('h5') if (h5['class'] == ['bsp-bio-sub-text']) and (h5.parent.parent['class']!= ['hidden-xs']) and (h5.text != 'Broadway')]
        genre_in_year.append('+'.join(curr_genre))
        h3 =  soup.find('h3', text = 'Awards')
        curr_noms = 0
        curr_win_num = 0
        curr_awards = []
        if h3:
            div = h3.parent
            for t in div.find_all('table'):
                award_org  =  t.th.text
                award_cat = [td.text for td in t.tbody.find_all('td',class_="col-1")] 
                result = [td.text for td in t.tbody.find_all('td',class_="col-3")]
                curr_noms += len(result)
                curr_win_num += result.count('Winner')
                for i in range(len(award_cat)):
                    curr_awards.append(' + '.join([award_org, result[i], award_cat[i]]))
        nominations_in_year.append(curr_noms)
        wins_in_year.append(curr_win_num)
        awards_in_year.append(curr_awards)
        #divs  = soup.find_all('div', class_="info-circular-text")
        spans  = soup.find_all('span', class_="info-circular-text")
        if spans:
            performances_in_year.append(int(spans[-1].text.replace(',','').strip()))
        
    name.extend(names_in_year)
    genre.extend(genre_in_year)
    awards.extend(awards_in_year)
    nominations.extend(nominations_in_year)
    wins.extend(wins_in_year)
    performances.extend(performances_in_year)
show_type_data = pd.DataFrame({'Year': year,
                            'Name':name,
                           'Type':genre,
                            'Nominations':nominations,
                            'Wins': wins,
                            'Awards':awards,
                            'Performances': performances,
                           })
show_type_data.to_csv('show_data_1985_1990.csv')