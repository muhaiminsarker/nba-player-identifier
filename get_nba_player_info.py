from bs4 import BeautifulSoup
from urllib.request import urlopen
import re 
import pandas as pd
import requests

#Before we can get to identifying NBA players by image, we need to get a dataset of 
# NBA players 

#Initial Information to obtain: 
#1. Name of Player
#2. URL
#3. Height
#4. Weight
#5. Nationality
#6. Current Team

#We will mainly scour https://basketball.realgm.com/nba/players for all our data
#We will only get players from 1998-2023
