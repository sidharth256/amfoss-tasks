import requests
from bs4 import BeautifulSoup
from datetime import datetime
import csv

url = "https://www.espncricinfo.com/live-cricket-score"
get_url = requests.get(url).text

soup = BeautifulSoup(get_url, 'lxml')
main = soup.find_all('div', class_ = 'ds-flex ds-flex-col ds-mt-2 ds-mb-2')
time = datetime.now()
current_time = time.strftime("%Y-%m-%d")
csv_time = time.strftime("%Y-%m-%d %H:%M:%S")
status = soup.find('p', 'ds-text-tight-s ds-font-regular ds-truncate ds-text-typo')

if len(main)>=1:
    over_1 = ""
    over_2 = ""
    score_1 = ""
    score_2 = ""
    match1 = main[0]
    teams1 = match1.find_all('p')
    overs1 = match1.find_all('span')
    scores1 = match1.find_all('strong')

    if len(teams1)>=2:
        team_1 = teams1[0].text.strip()   
        team_2 = teams1[1].text.strip()

        if len(overs1)>=1:
            over_1 = overs1[0].text.strip()           
        if len(overs1)>=2:
            over_2 = overs1[1].text.strip()

        if len(scores1)>=1:
            score_1 = scores1[0].text.strip()
        if len(scores1)>=2:
            score_2 = scores1[1].text.strip()

elif len(main)>=2:
    over_1 = ""
    over_2 = ""
    score_1 = ""
    score_2 = ""
    match2 = main[1]
    teams2 = match2.find_all('p')
    overs2 = match2.find_all('span')
    scores2 = match2.find_all('strong')

    if len(teams2)>=2:
        team_1 = teams2[0].text.strip()    
        team_2 = teams2[1].text.strip()

        if len(overs2)>=1:
            over_1 = overs2[0].text.strip()   
        if len(overs2)>=2:
            over_2 = overs2[1].text.strip()

        if len(scores2)>=1:
            score_1 = scores2[0].text.strip()
        if len(scores2)>=2:
            score_2 = scores2[1].text.strip()


if status:
    live_status = status.text.strip('.') 

if over_1 and over_2:
    match_data = [team_1, over_1, score_1, team_2, over_2, score_2, live_status, csv_time]

elif over_1 and score_2:
    match_data = [team_1, over_1, score_1, team_2, over_2, score_2, live_status, csv_time]

elif over_2 and score_1:
    match_data = [team_1, over_1, score_1, team_2, over_2, score_2, live_status, csv_time]

elif over_1:
    match_data = [team_1, over_1, score_1, team_2, over_2, score_2, live_status, csv_time]

else:
    match_data = [team_1, team_2, live_status, csv_time]
def add_data():
    with open('livescores.csv', 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        c = csv_writer.writerow(match_data)
    return c

def score(team_1, over_1, score_1, team_2, over_2, score_2, live_status, current_time):
    data = (f'{team_1} {over_1}{score_1}\n{team_2} {over_2}{score_2}\n{live_status}\n{current_time}')
    return data

def no_live():
    if 'live' not in main:
        result = "No live matches available"
    return result









