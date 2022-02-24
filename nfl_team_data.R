# Copyright 2021 pgdunn@bu.edu

# Preparing some information to investigate coaches and rookie QBs

# 30 Jan 2021
# Parker Dunn


# INVESTIGATING team info available via nflverse

library(nflreadr)
library(tidyverse)
library(dplyr)

teams_info <- load_teams()

# NOTE there are going to be issues with teams that have changed location
# ACTUALLY the "load_teams()" method brings information about old teams!

# Las Vegas Raiders (LV)        <-  Oakland Raiders (OAK - I think)
# Los Angeles Chargers (LAC)    <-  San Diego Chargers (SD - I think)
# Los Angeles Rams (LAR)        <-  St. Louis Rams (STL - I think)

# typeof(teams_info)

write.csv(teams_info, file='4-Code/NFL-Projects/coaches_rookie_qbs/team_info.csv')
