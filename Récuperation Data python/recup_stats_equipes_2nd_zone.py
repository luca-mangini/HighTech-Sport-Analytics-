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
dict_league_names = {'Ligue-2': '60',
                    }

# Define league saison and their IDs
dict_league_saison = {
                      'Ligue-2-2017-2018': '1633',
                      'Ligue-2-2018-2019': '2105',
                      'Ligue-2-2019-2020': '3244',
                      'Ligue-2-2020-2021': '10761',
                      'Ligue-2-2021-2022': '',
                    }

## Define list of long names for 'Big 5' European Leagues and MLS
lst_league_names_long = ['Ligue-2']

## Define seasons to scrape
lst_seasons = ['2017-2018','2018-2019','2019-2020','2020-2021','2021-2022']

## Define list of folders
lst_folders = ['raw', 'engineered', 'reference']

## Define list of data types
lst_data_types = ['goalkeeper', 'outfield', 'team']

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
    os.remove(os.path.join(data_dir_fbref +f'/raw/team/fbref_team_minor_player_stats_for_combined_latest.csv'))
    
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
            if not os.path.exists(os.path.join(data_dir_fbref +f'/raw/team/fbref_team_minor_player_stats_for_combined_latest.csv')):

                ##### Scraping
                if(saison_name_short!=""):
                  ##### Print statement
                  print(f'Scraping started for player stats data for {league_name_long} league for the {season} season...')

                  ##### Standard stats
                  print(f'Scraping Standard stats...')
                  url_std_stats = f'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fcomps%2F{league_name_short}%2F{saison_name_short}%2Fstats%2Fplayers%2F{season}-{league_name_long}&div=div_stats_squads_standard_for'
                  df_std_stats = pd.read_html(url_std_stats, header=1)[0]
                  
                  ##### Shooting stats
                  print(f'Scraping Shooting stats...')
                  url_shooting = f'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fcomps%2F{league_name_short}%2F{saison_name_short}%2Fshooting%2Fplayers%2F{season}-{league_name_long}&div=div_stats_squads_shooting_for'
                  df_shooting = pd.read_html(url_shooting, header=1)[0]
                  
                  ##### Playing Time stats
                  print(f'Scraping Playing Time stats...')
                  url_playing_time = f'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fcomps%2F{league_name_short}%2F{saison_name_short}%2Fplayingtime%2Fplayers%2F{season}-{league_name_long}&div=div_stats_squads_playing_time_for'
                  df_playing_time = pd.read_html(url_playing_time, header=1)[0]

                  ##### Miscellaneous stats
                  print(f'Scraping Miscellaneous stats...')
                  url_misc = f'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fcomps%2F{league_name_short}%2F{saison_name_short}%2Fmisc%2Fplayers%2F{season}-{league_name_long}&div=div_stats_squads_misc_for'
                  df_misc = pd.read_html(url_misc, header=1)[0]

                else:
                  ##### Print statement
                  print(f'Scraping started for player stats data for {league_name_long} league for the {season} season...')

                  ##### Standard stats
                  print(f'Scraping Standard stats...')
                  url_std_stats = f'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fcomps%2F{league_name_short}%2F{saison_name_short}%2Fstats%2Fplayers%2F{season}-{league_name_long}&div=div_stats_squads_standard_for'
                  df_std_stats = pd.read_html(url_std_stats, header=1)[0]

                  ##### Shooting stats
                  print(f'Scraping Shooting stats...')
                  url_shooting = f'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fcomps%2F{league_name_short}%2Fshooting%2Fplayers%2F{season}-{league_name_long}&div=div_stats_squads_shooting_for'
                  df_shooting = pd.read_html(url_shooting, header=1)[0]
                  
                  ##### Playing Time stats
                  print(f'Scraping Playing Time stats...')
                  url_playing_time = f'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fcomps%2F{league_name_short}%2Fplayingtime%2Fplayers%2F{season}-{league_name_long}&div=div_stats_squads_playing_time_for'
                  df_playing_time = pd.read_html(url_playing_time, header=1)[0]

                  ##### Miscellaneous stats
                  print(f'Scraping Miscellaneous stats...')
                  url_misc = f'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fcomps%2F{league_name_short}%2Fmisc%2Fplayers%2F{season}-{league_name_long}&div=div_stats_squads_misc_for'
                  df_misc = pd.read_html(url_misc, header=1)[0]

                ##### Concatenate defined individual DataFrames
                ####### Define DataFrames to be concatenated side-by-side (not all of them)
                lst_dfs = [df_std_stats, df_shooting]

                ###### Concatenate DataFrames side-by-side (indicated in list above)
                df_all = pd.concat(lst_dfs, axis=1)

                ###### Drop duplicate columns
                df_all = df_all.loc[:,~df_all.columns.duplicated()]

                ###### Drop duplicate rows
                df_all = df_all.drop_duplicates()
                
                ##### Left join defined individual DataFrames
                ####### Define join conditions
                conditions_join = ['Squad', '# Pl']

                ###### Left join Playing Time data
                df_all = pd.merge(df_all, df_playing_time, left_on=conditions_join, right_on=conditions_join, how='left')

                ###### Remove duplicate columns after join (contain '_y') and remove '_x' suffix from kept columns
                df_all = df_all[df_all.columns.drop(list(df_all.filter(regex='_y')))]
                df_all.columns = df_all.columns.str.replace('_x','')
                
                ###### Drop duplicate rows
                df_all = df_all.drop_duplicates()

                ###### Left join Misc data
                df_all = pd.merge(df_all, df_misc, left_on=conditions_join, right_on=conditions_join, how='left')

                ###### Remove duplicate columns after join (contain '_y') and remove '_x' suffix from kept columns
                df_all = df_all[df_all.columns.drop(list(df_all.filter(regex='_y')))]
                df_all.columns = df_all.columns.str.replace('_x','')
                
                ###### Drop duplicate rows
                df_all = df_all.drop_duplicates()
                
                ##### Engineer DataFrames
                ###### Take first two digits of age - fixes current season issue with extra values
                df_all['Age'] = df_all['Age'].astype(str).str[:2]
                
                ###### Create columns for league code and season
                df_all['League Name'] = league_name_long
                df_all['League ID'] = league_name_short
                df_all['Season'] = season              

                ###### Drop duplicates
                df_all = df_all.drop_duplicates()

                # Remove accents
                df_all['Squad'] = (df_all['Squad'].str.encode('latin-1', errors='ignore').str.decode('UTF-8',errors='ignore'))
                
                #Update of name columns 
                df_all = df_all.rename({'Gls.1': 'Gls/90','Ast.1':'Ast/90','G-PK.1':'G-PK/90'}, axis=1)            
                df_all['Squad'] = df_all['Squad'].str.replace('vs ','')
                
                ##### Save DataFrame
                df_all.to_csv(data_dir_fbref + f'/raw/team/{league_name_long}/{season}/fbref_team_minor_player_stats_for_{league_name_long}_{season}_latest.csv', index=None, header=True)        
                
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
    all_files = glob.glob(os.path.join(data_dir_fbref + f'/raw/team/*/*/fbref_team_minor_player_stats_for_*_*_latest.csv'))
    
    ### Create an empty list of Players URLs
    lst_player_stats_all = []

    ### Loop through list of files and read into temporary DataFrames
    for filename in all_files:
        df_temp = pd.read_csv(filename, index_col=None, header=0)
        lst_player_stats_all.append(df_temp)

    ### Concatenate the files into a single DataFrame
    df_fbref_player_stats_all = pd.concat(lst_player_stats_all, axis=0, ignore_index=True)
    
    ### Sort DataFrame
    df_fbref_player_stats_all = df_fbref_player_stats_all.sort_values(['Squad', '# Pl'], ascending=[True, True])

    ## Export DataFrame
    ###
    df_fbref_player_stats_all.to_csv(data_dir_fbref + f'/raw/team/fbref_team_minor_player_stats_for_combined_latest.csv', index=None, header=True)

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

lst_league_names = ['Ligue-2']     #'Big-5-European-Leagues','Premier-League', 'Ligue-1', 'Bundesliga', 'Serie-A', 'La-Liga', 'Major-League-Soccer']
lst_seasons = ['2021-2022']


df_fbref_outfield_raw = get_fbref_squad_stats_player(lst_league_names, lst_seasons)

from sqlalchemy import create_engine
import pymysql
import pandas as pd
import pandas
 
tableName   = "fbref_team_minor_player_stats_for"
        
sqlEngine       = create_engine('mysql+pymysql://lmangini:root@127.0.0.1/foot', pool_recycle=3600)
dbConnection    = sqlEngine.connect()

try:
    frame = df_fbref_outfield_raw.to_sql(tableName, dbConnection, if_exists='replace');
except ValueError as vx:
    print(vx)
except Exception as ex:   
    print(ex)
else:
    print("Table %s created successfully."%tableName);   
finally:
    dbConnection.close()

