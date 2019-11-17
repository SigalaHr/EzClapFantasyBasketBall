from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome()

########################################################################################################################
# # This gets the players names
# players = []
# driver.get("https://www.fantasypros.com/nba/stats/avg-overall.php")
#
# # Confirms that the title has the word "Python" in it
# # assert "Python" in driver.title
#
# content = driver.page_source
# soup = BeautifulSoup(content)
#
# for a in soup.findAll('td', attrs={'class': 'player-label'}):
#     name = a.find('a', attrs={'class': 'player-name'})
#     players.append(name.text)
#
# df = pd.DataFrame({'Players Name': players})
# df.to_csv('products.csv', index=False, encoding='utf-8')

########################################################################################################################
# This gets the teams playing for the week
year = 2019
month = 11
day = 18

dic = {}


print(year)
print(month)
print(day)
driver.get("https://www.espn.com/nba/schedule/_/date/" + str(year) + str(month) + str(day))

content = driver.page_source
soup = BeautifulSoup(content)

for a in soup.findAll('a', attrs={'class': 'team-name'}):
    teamAbr = a.find('abbr')
    teamFullName = teamAbr['title']
    namePlusAbr = teamAbr['title'] + ":" + teamAbr.text

    if namePlusAbr in dic:
        dic[namePlusAbr] = dic.get(namePlusAbr) + 1
    else:
        dic[namePlusAbr] = 1

print(sorted(dic.items(), key=lambda kv: (kv[1], kv[0]), reverse=True))
teamName = []
teamAbbreviation = []
gamesThisWeek = []

for key, value in sorted(dic.items(), key=lambda kv: (kv[1], kv[0]), reverse=True):
    nameAndAbr = key.split(':')
    teamName.append(nameAndAbr[0])
    teamAbbreviation.append(nameAndAbr[1])
    gamesThisWeek.append(value)


df = pd.DataFrame({'Team Name': teamName, 'Team Abbreviation': teamAbbreviation, 'Games This Week': gamesThisWeek})
df.to_csv('products.csv', index=False, encoding='utf-8')
