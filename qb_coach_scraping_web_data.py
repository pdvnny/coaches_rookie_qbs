# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 22:43:26 2022

@author: dvnny


DESCRIPTION

Practicing web scraping with BeautifulSoup4

Trying to pull coaching information from 

"""

from bs4 import BeautifulSoup
import requests
import pandas as pd

# https://www.pro-football-reference.com/teams/nyj/coaches.htm#coaches_year

pfr_teams_site = "https://www.pro-football-reference.com/teams/"
suffix = "/coaches.htm#coaches_year"

team = "nyj"

r = requests.get(pfr_teams_site + team + suffix)

# Previewing info about the response
# print(r.headers)
# print(r.text)

soup = BeautifulSoup(r.text, "html.parser")
# print(soup.table)

# tables = soup.find_all('div', {'table'})
tables = soup.find_all('table')

# print(soup.prettify())

coach_data = tables[1]
print(coach_data)

df = pd.read_html(str(coach_data))[0]

print(df.head())
print(df.info())
print(df.columns)

df.columns = ["year","coach","regular_season_games","wins","losses","ties","win_percentage","playoff_games","playoff_wins","playoff_losses",\
                                  "playoff_result","coordinator_offense","coordinator_defense"]

#df.rename(columns={'Year':"year",'Coach':"coach",'G':"regular_season_games",'W':"win",'L':"loss",'T':"tie",'W-L%':"win_percentage"}, inplace=True)
                   # ,"playoff_games","playoff_win","playoff_loss","playoff_result","coordinator_offense","coordinator_defense"})
# df.astype({"year":"int64"}).dtypes

print(df.info())