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

teams_pfr = [team.lower() for team in teams]

teams_pfr[0] = "crd"
teams_pfr[2] = "rav"
teams_pfr[11] = "gnb"
teams_pfr[12] = "htx"
teams_pfr[13] = "clt"
teams_pfr[15] = "kan"
teams_pfr[16] = "rai"
teams_pfr[17] = "sdg"
teams_pfr[18] = "ram"
teams_pfr[19] = "was"  # SWAP: "lv" -> WAS - Washington Football Team
teams_pfr[22] = "nwe"
teams_pfr[23] = "nor"
teams_pfr[26] = "tam"  # SWAP: "oak" -> TB - Tampa Bay
teams_pfr[29] = "oti"  # SWAP: "sd" -> TEN - Tennessee
teams_pfr[31] = "sfo"

teams_pfr_32 = teams_pfr[0:32]

# Modify teams to match order of teams_pfr - although there are many changes above, the teams represented stay the same
# Any time there was not a full swap, e.g., "lv" -> "was", there is no need to correct the original teams list

teams[19] = "WAS"
teams[26] = "TB"
teams[29] = "TEN"

for i,team in enumerate(teams_pfr_32):
    r = requests.get(pfr_teams_site + team + suffix)
    soup = BeautifulSoup(r.text, "html.parser")
    tables = soup.find_all('table')
    coach_data = tables[1]
    df = pd.read_html(str(coach_data))[0]
    df.columns = ["year","coach","regular_season_games","wins","losses","ties","win_percentage","playoff_games","playoff_wins","playoff_losses",\
                                      "playoff_result","coordinator_offense","coordinator_defense"]
    #print(df.iloc[0])
    
    with open("coach_data/"+teams[i]+".csv",'w') as f:
      df.to_csv(f,na_rep="N/A",header=True)