# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 22:43:26 2022

@author: dvnny


DESCRIPTION

Practicing web scraping with BeautifulSoup4

Trying to pull coaching information from Pro-Football-Reference (PFR) since I wasn't able to find
another convenient table with coaching information.

Here is a sample of pulling a table from PFR with coaching information about the New York Jets.

I will reproduce similar work in order to extract information about every NFL teams coaches in another script.

"""

from bs4 import BeautifulSoup
import requests
import pandas as pd

# sample of NYJ site -> https://www.pro-football-reference.com/teams/nyj/coaches.htm#coaches_year

pfr_teams_site = "https://www.pro-football-reference.com/teams/"
suffix = "/coaches.htm#coaches_year"

team = "nyj"

r = requests.get(pfr_teams_site + team + suffix)

# Previewing info about the response
# print(r.headers)
# print(r.text)

soup = BeautifulSoup(r.text, "html.parser")
# print(soup.table)

tables = soup.find_all('table')

# print(soup.prettify())

coach_data = tables[1]
# print(coach_data)   <-- preview of the raw HTM table; very messy to print though

df = pd.read_html(str(coach_data))[0]

print(df.head(), "\n")
print(df.info(), "\n")
print(df.columns, "\n")

df.columns = ["year","coach","regular_season_games","wins","losses","ties","win_percentage","playoff_games","playoff_wins",
                                "playoff_losses", "playoff_result","coordinator_offense","coordinator_defense"]


print(df.info())