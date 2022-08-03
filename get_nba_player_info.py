from bs4 import BeautifulSoup
from urllib.request import urlopen
import re 
import pandas as pd
import requests

#Before we can get to identifying NBA players by image, we need to get a dataset of NBA players 

#Initial Information to obtain: 
#1. Name of Player
#2. URL
#3. Height
#4. Weight
#5. Nationality
#6. Current Team

# We will mainly scour https://basketball.realgm.com/nba/players for all our data
# We will only get players from 1998-2023

# Go from 2023 all the way down to 1998
# This is to ensure that you will get the latest information about players and not 
# have to update the player throughout
years = reversed(range(1998, 2023))
baseURL = "https://basketball.realgm.com/nba/players/"

player_data = pd.DataFrame()
for i in years:
    #Uses Pandas to read the url and create a table
    table = pd.read_html(baseURL + str(i))

    #Add the player_data with the table[0] which has the DataFrame
    #containing the player data
    player_data = pd.concat([player_data, table[0]], ignore_index=True)
    break
print(player_data)

#Next Steps
#1. Be able to obtain the links for each player's profile
#2. Make it so that you don't add a players information 