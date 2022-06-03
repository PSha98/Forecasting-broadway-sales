# Write your code here :-)
from bs4 import BeautifulSoup
import requests
import time
import pandas as pd
import numpy as np

year_url = "https://playbill.com/seasons?year="
name = []
genre = []
nominations = []
wins = []
performances  = []
year = []
opening_date = []
previews = []
theatre = []
play = []
musical = []
revue = []
revival = []
best_musical_nom = []
best_play_nom = []
best_revival_musical_nom = []
best_revival_play_nom = []
best_musical_winner = []
best_play_winner = []
best_revival_musical_winner = []
best_revival_play_winner = []
for i in range(1985,1990):
     if i != 2020:   
        end = str(i)
        page = requests.get(year_url + end)
        
        time.sleep(3)
        soup = BeautifulSoup(page.content, 'html.parser')
        print(i)
        table = soup.find('table').tbody
        names_in_year = [a.text.strip() for a in table.find_all('a') if a.parent['class'] == ['col-1']]
        url_in_year = [a['href'] for a in table.find_all('a') if a.parent['class'] == ['col-1']]
        opening_date_in_year = [pd.to_datetime(td.text).date() for td in table.find_all('td') if td['class'] == ['col-2']]
        genre_in_year = []
        wins_in_year = []
        nominations_in_year = []
        performances_in_year = []
        previews_in_year = []
        theatre_in_year = []
        for url in url_in_year:
            time.sleep(3)
            year.append(end)
            page = requests.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')
            play.append(0)
            musical.append(0)
            revival.append(0)
            curr_genre = [h5.text for h5 in soup.find_all('h5') if (h5['class'] == ['bsp-bio-sub-text']) and (h5.parent.parent['class']!= ['hidden-xs']) and (h5.text != 'Broadway')]
            if 'Revival' in curr_genre:
                revival[-1] = 1
            if 'Musical' in curr_genre:
                musical[-1] = 1
            elif 'Revue' in curr_genre:
                musical[-1] = 1
            else:
                play[-1] = 1
            genre_in_year.append(' '.join(curr_genre))
            ul = soup.find('ul', {'class' : "bsp-bio-links bsp-bio-links-top"})
            theatre_in_year.append(ul.li.a.text)
            h3 =  soup.find('h3', text = 'Awards')
            curr_noms = 0
            curr_win_num = 0
            best_musical_nom.append(0)
            best_play_nom.append(0)
            best_revival_musical_nom.append(0)
            best_revival_play_nom.append(0)
            best_musical_winner.append(0)
            best_play_winner.append(0)
            best_revival_musical_winner.append(0)
            best_revival_play_winner.append(0)
            if h3:
                div = h3.parent
                for t in div.find_all('table'):
                    award_org  =  t.th.text
                    award_cat = [td.text for td in t.tbody.find_all('td',class_="col-1")] 
                    result = [td.text for td in t.tbody.find_all('td',class_="col-3")]
                    curr_noms += len(result)
                    curr_win_num += result.count('Winner')
                    if award_org == 'Tony Award':
                        for i in range(len(award_cat)):
                            if award_cat[i] == 'Best Musical' or award_cat[i] == 'Musical':
                                best_musical_nom[-1] = 1
                                if result[i] == 'Winner':
                                    best_musical_winner[-1] = 1
                            elif award_cat[i] == 'Best Revival of a Musical':
                                best_revival_musical_nom[-1] = 1
                                if result[i] == 'Winner':
                                    best_revival_musical_winner[-1] = 1
                            elif award_cat[i] == 'Best Play' or award_cat[i] == 'Play':
                                best_play_nom[-1] = 1
                                if result[i] == 'Winner':
                                    best_play_winner[-1] = 1
                            elif award_cat[i] == 'Best Revival of a Play':
                                best_revival_play_nom[-1] = 1
                                if result[i] == 'Winner':
                                    best_revival_play_winner[-1] = 1
                            
            nominations_in_year.append(curr_noms)
            wins_in_year.append(curr_win_num)
            spans_pre = soup.find_all('span', class_="info-circular-pre-text")
            spans  = soup.find_all('span', class_="info-circular-text")
            spans_post = soup.find_all('span', class_="info-circular-post-text")
            if spans:
                performances_in_year.append(int(spans[-1].text.replace(',','').strip()))
            if len(spans) == 5:
                previews_in_year.append(int(spans[-2].text.replace(',','').strip()))
            else:
                previews_in_year.append(0)
                                    
        name.extend(names_in_year)
        genre.extend(genre_in_year)
        nominations.extend(nominations_in_year)
        wins.extend(wins_in_year)
        performances.extend(performances_in_year)
        previews.extend(previews_in_year)
        opening_date.extend(opening_date_in_year)
        theatre.extend(theatre_in_year)
        
show_type_data = pd.DataFrame({'season': year,
                               'opening_date': opening_date,
                            'name':name,
                            'theatre':theatre,
                           'type':genre,
                            'all_nominations':nominations,
                            'all_Wins': wins,
                            'tony_best_musical_nom': best_musical_nom,
                            'tony_best_musical_winner': best_musical_winner,
                            'tony_best_revival_musical_nom': best_revival_musical_nom,
                            'tony_best_revival_musical_winner': best_revival_musical_winner,
                            'tony_best_play_nom': best_play_nom,
                            'tony_best_play_winner': best_play_winner,
                            'tony_best_revival_play_nom': best_revival_play_nom,
                            'tony_best_revival_play_winner': best_revival_play_winner,
                            'performances': performances,
                            'previews': previews,
                            'play': play,
                            'musical': musical,
                            'revival': revival
                            })
show_type_data.to_csv('show_data_new_1985_1990.csv')