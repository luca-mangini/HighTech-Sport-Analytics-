# Python â‰¥3.5 (ideally)
import platform
import sys, getopt
assert sys.version_info >= (3, 5)
import csv

# Math Operations
import numpy as np
from math import pi

# Datetime
import datetime
from datetime import date
import time

# Data Preprocessing
import pandas as pd
#import pandas_profiling as pp
import os
import re
import random
import glob
from io import BytesIO
from pathlib import Path

# Reading directories
import glob
import os

# Working with JSON
import json
from pandas.io.json import json_normalize

# Web Scraping
import requests
from bs4 import BeautifulSoup
import re

# Data Visualisation
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('seaborn-whitegrid')
import missingno as msno

# Progress Bar
from tqdm import tqdm

# Display in Jupyter
from IPython.display import Image, YouTubeVideo
from IPython.core.display import HTML

# Ignore Warnings
import warnings
warnings.filterwarnings(action="ignore", message="^internal gelsd")

# Set up initial paths to subfolders
base_dir = os.path.join('')
data_dir = os.path.join(base_dir, 'data')
data_dir_fbref = os.path.join(base_dir, 'data', 'fbref')
img_dir = os.path.join(base_dir, 'img')
fig_dir = os.path.join(base_dir, 'img', 'fig')
video_dir = os.path.join(base_dir, 'video')

## Define today's date
today = datetime.datetime.now().strftime('%d/%m/%Y').replace('/', '')

# Define league names and their IDs
dict_league_names = {'Premier-League': '9',
                     'Ligue-1': '13',
                     'Bundesliga': '20',
                     'Serie-A': '11',
                     'La-Liga': '12',
                     'Champions-League': '8',
                     'Europa-League': '19'
                    }

# Define league saison and their IDs
dict_league_saison = {'Premier-League-2017-2018': '1631',
                     'Premier-League-2018-2019': '1889',
                     'Premier-League-2019-2020': '3232',
                     'Premier-League-2020-2021': '10728',
                     'Premier-League-2021-2022': '11160',
                     'Ligue-1-2017-2018': '1632',
                     'Ligue-1-2018-2019': '2104',
                     'Ligue-1-2019-2020': '3243',
                     'Ligue-1-2020-2021': '10732',
                     'Ligue-1-2021-2022': '11183',
                     'Bundesliga-2017-2018': '1634',
                     'Bundesliga-2018-2019': '2109',
                     'Bundesliga-2019-2020': '3248',
                     'Bundesliga-2020-2021': '10737',
                     'Bundesliga-2021-2022': '11193',
                     'Serie-A-2017-2018': '1640',
                     'Serie-A-2018-2019': '1896',
                     'Serie-A-2019-2020': '3260',
                     'Serie-A-2020-2021': '10730',
                     'Serie-A-2021-2022': '11222',
                     'La-Liga-2017-2018': '1652',
                     'La-Liga-2018-2019': '1886',
                     'La-Liga-2019-2020': '3239',
                     'La-Liga-2020-2021': '10731',
                     'La-Liga-2021-2022': '11174',
                     'Champions-League-2017-2018': '1656',
                     'Champions-League-2018-2019': '2102',
                     'Champions-League-2019-2020': '2900',
                     'Champions-League-2020-2021': '10096',
                     'Champions-League-2021-2022': '11323',
                     'Europa-League-2017-2018': '1657',
                     'Europa-League-2018-2019': '2103',
                     'Europa-League-2019-2020': '2901',
                     'Europa-League-2020-2021': '10097',
                     'Europa-League-2021-2022': '11326',
                    }

## Define list of long names for 'Big 5' European Leagues and MLS
lst_league_names_long = ['Premier-League', 'Ligue-1', 'Bundesliga', 'Serie-A', 'La-Liga','Champions-League','Europa-League']

## Define seasons to scrape
lst_seasons = ['2017-2018', '2018-2019', '2019-2020', '2020-2021', '2021-2022']

## Define list of folders
lst_folders = ['raw', 'engineered', 'reference']

## Define list of data types
lst_data_types = ['goalkeeper', 'outfield', 'team','scores_fixtures']

# Define function for scraping a defined season and competition of FBref player data
def get_fbref_squad_stats_player(lst_league_names, lst_seasons):
    
    ## Define list of league names
    league_names_long = lst_league_names
    
    ## Define seasons to scrape
    seasons = lst_seasons
    
    ## Start timer
    tic = datetime.datetime.now()
    
    ## Print time scraping started
    print(f'Scraping started at: {tic}')
    
    ##On supprime le fichier global afin de venir faire la MAJ
    os.remove(os.path.join(data_dir_fbref +f'/raw/scores_fixtures/fbref_scores_fixtures_latest.csv'))
    
    ## Scrape information for each player
    for season in seasons:

        ### Print message
        print(f'Scraping started for the {season} season...')

        ### Loop through leagues
        for league_name_long in league_names_long:
            #### Determine league short name from the league names dictionary
            league_name_short = [v for k,v in dict_league_names.items() if k == league_name_long][0]
            saison_name_short = [v for k,v in dict_league_saison.items() if k == league_name_long+"-"+str(season)][0]
            
            #### Save Player URL List (if not already saved)
            if not os.path.exists(os.path.join(data_dir_fbref +f'/raw/scores_fixtures/fbref_scores_fixtures_combined_latest.csv')):

                ##### Scraping
                if(saison_name_short!=""):
                  ##### Print statement
                  print(f'Scraping started for player stats data for {league_name_long} league for the {season} season...')

                  ##### Standard stats
                  print(f'Scraping Standard stats...')
                  url_std_scores_fixtures = f'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fcomps%2F{league_name_short}%2F{saison_name_short}%2Fschedule%2F{season}-{league_name_long}-Scores-and-Fixtures&div=div_sched_{saison_name_short}_1'
                  df_std_scores_fixtures = pd.read_html(url_std_scores_fixtures, header=0)[0]
                else:
                  ##### Print statement
                  print(f'Scraping started for player stats data for {league_name_long} league for the {season} season...')

                  ##### Standard stats
                  print(f'Scraping Standard stats...')
                  url_std_scores_fixtures = f'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fcomps%2F{league_name_short}%2F{saison_name_short}%2Fschedule%2F{season}-{league_name_long}-Scores-and-Fixtures&div=div_sched_{saison_name_short}_1'
                  df_std_scores_fixtures = pd.read_html(url_std_scores_fixtures, header=0)[0]

                ###### Drop duplicate rows
                df_std_scores_fixtures = df_std_scores_fixtures.drop_duplicates()
                               
                ###### Create columns for league code and season
                df_std_scores_fixtures['League Name'] = league_name_long
                df_std_scores_fixtures['League ID'] = league_name_short
                df_std_scores_fixtures['Season'] = season              
                del df_std_scores_fixtures['Notes']
                del df_std_scores_fixtures['Match Report']

                # Remove accents
                df_std_scores_fixtures['Home'] = (df_std_scores_fixtures['Home'].str.encode('latin-1', errors='ignore').str.decode('UTF-8',errors='ignore'))
                df_std_scores_fixtures['Away'] = (df_std_scores_fixtures['Away'].str.encode('latin-1', errors='ignore').str.decode('UTF-8',errors='ignore'))
                df_std_scores_fixtures['Referee'] = (df_std_scores_fixtures['Referee'].str.encode('latin-1', errors='ignore').str.decode('UTF-8',errors='ignore'))
                df_std_scores_fixtures['Venue'] = (df_std_scores_fixtures['Venue'].str.encode('latin-1', errors='ignore').str.decode('UTF-8',errors='ignore'))
                
                ##### Save DataFrame
                df_std_scores_fixtures.to_csv(data_dir_fbref + f'/raw/scores_fixtures/{league_name_long}/{season}/fbref_scores_fixtures_{league_name_long}_{season}_latest.csv', index=None, header=True)        
                
                ##### Print statement for league and season
                print(f'All player stats data for the {league_name_long} league for {season} season scraped and saved.')
             
            
            #### Load player stats data (if already saved)
            else:
                ##### Print statement
                print(f'Player stats data for the {league_name_long} league for the {season} season already saved as a CSV file.')         
           
    ## End timer
    toc = datetime.datetime.now()
    
    ## Print time scraping ended
    print(f'Scraping ended at: {toc}')

    ## Calculate time take
    total_time = (toc-tic).total_seconds()
    print(f'Time taken to scrape the player stats data for {len(league_names_long)} leagues for {len(seasons)} seasons is: {total_time/60:0.2f} minutes.')

    ## Unify individual CSV files as a single DataFrame
    ### Show files in directory
    all_files = glob.glob(os.path.join(data_dir_fbref + f'/raw/scores_fixtures/*/*/fbref_scores_fixtures_*_*_latest.csv'))
    ### Create an empty list of Players URLs
    lst_player_stats_all = []

    ### Loop through list of files and read into temporary DataFrames
    for filename in all_files:
        df_temp = pd.read_csv(filename, index_col=None, header=0)
        lst_player_stats_all.append(df_temp)

    ### Concatenate the files into a single DataFrame
    df_fbref_player_stats_all = pd.concat(lst_player_stats_all, axis=0, ignore_index=True)
    
    ### Sort DataFrame
    df_fbref_player_stats_all = df_fbref_player_stats_all.sort_values(['Date'], ascending=[True])

    ## Export DataFrame
    df_fbref_player_stats_all.to_csv(data_dir_fbref + f'/raw/scores_fixtures/fbref_scores_fixtures_latest.csv', index=None, header=True)
    
    ## Return final list of Player URLs
    return(df_fbref_player_stats_all)

# Make the data directory structure
for folder in lst_folders:
    path = os.path.join(data_dir_fbref, folder)
    if not os.path.exists(path):
        os.mkdir(path)
        for data_types in lst_data_types:
            path = os.path.join(data_dir_fbref, folder, data_types)
            if not os.path.exists(path):
                os.mkdir(path)
                for league in lst_league_names_long:
                    path = os.path.join(data_dir_fbref, folder, data_types, league)
                    if not os.path.exists(path):
                        os.mkdir(path)
                        for season in lst_seasons:
                            path = os.path.join(data_dir_fbref, folder, data_types, league, season)
                            if not os.path.exists(path):
                                os.mkdir(path)

# Display all columns of pandas DataFrames
pd.set_option('display.max_columns', None)

lst_league_names = ['Premier-League', 'Ligue-1', 'Bundesliga', 'Serie-A', 'La-Liga','Champions-League','Europa-League']     #'Big-5-European-Leagues','Premier-League', 'Ligue-1', 'Bundesliga', 'Serie-A', 'La-Liga', 'Major-League-Soccer']
lst_seasons = ['2021-2022']

df_std_scores_fixtures = get_fbref_squad_stats_player(lst_league_names, lst_seasons)

df_std_scores_fixtures_cup = df_std_scores_fixtures.loc[(df_std_scores_fixtures['League Name'] == 'Champions-League') | (df_std_scores_fixtures['League Name'] == 'Europa-League')]
df_std_scores_fixtures_no_cup = df_std_scores_fixtures.loc[(df_std_scores_fixtures['League Name'] != 'Champions-League') & (df_std_scores_fixtures['League Name'] != 'Europa-League')]
df_std_scores_fixtures_cup['Away'] = df_std_scores_fixtures_cup['Away'].str[3:]
df_std_scores_fixtures_cup['Home'] = df_std_scores_fixtures_cup['Home'].str[:-3]
frames = [df_std_scores_fixtures_cup, df_std_scores_fixtures_no_cup]
df_std_scores_fixtures = pd.concat(frames)

from sqlalchemy import create_engine
import pymysql
import pandas as pd
import pandas
 
tableName   = "fbref_scores_fixtures"
        
sqlEngine       = create_engine('mysql+pymysql://lmangini:root@127.0.0.1/foot', pool_recycle=3600)
dbConnection    = sqlEngine.connect()

try:
    frame = df_std_scores_fixtures.to_sql(tableName, dbConnection, if_exists='replace');
except ValueError as vx:
    print(vx)
except Exception as ex:   
    print(ex)
else:
    print("Table %s created successfully."%tableName);   
finally:
    dbConnection.close()

