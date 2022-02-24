# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 00:11:31 2022

@author: dvnny

DESCRIPTION

Setting up a script that will scrape the web for coaching information from every team
SOURCE: https://www.pro-football-reference.com

I will accumulate this data

"""
#%%
# IMPORTS
from bs4 import BeautifulSoup
import requests
import pandas as pd

#%%

pfr_teams_site = "https://www.pro-football-reference.com/teams/"
suffix = "/coaches.htm#coaches_year"

teams = list(pd.read_csv("team_info.csv")["team_abbr"])
teams = [team.lower() for team in teams]
teams[0] = "crd"
teams[2] = "rav"
teams[11] = "gnb"
teams[12] = "htx"
teams[13] = "clt"
teams[15] = "kan"
teams[16] = "rai"
teams[17] = "sdg"
teams[18] = "ram"
teams[19] = "was"  # SWAP: "lv" -> WAS - Washington Football Team
teams[22] = "nwe"
teams[23] = "nor"
teams[26] = "tam"  # SWAP: "oak" -> TB - Tampa Bay
teams[29] = "oti"  # SWAP: "sd" -> TEN - Tennessee
teams[31] = "sfo"

teams = teams[0:32]

for team in teams:
    r = requests.get(pfr_teams_site + team + suffix)
    soup = BeautifulSoup(r.text, "html.parser")
    tables = soup.find_all('table')
    coach_data = tables[1]
    df = pd.read_html(str(coach_data))[0]
    df.columns = ["year","coach","regular_season_games","wins","losses","ties","win_percentage","playoff_games","playoff_wins","playoff_losses",\
                                      "playoff_result","coordinator_offense","coordinator_defense"]
    print(df.iloc[0])