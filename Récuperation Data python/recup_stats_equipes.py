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
                     'Major-League-Soccer': '22',
                     'Big-5-European-Leagues': 'Big5'
                    }

# Define league saison and their IDs
dict_league_saison = {'Premier-League-2017-2018': '1631',
                     'Premier-League-2018-2019': '1889',
                     'Premier-League-2019-2020': '3232',
                     'Premier-League-2020-2021': '10728',
                     'Premier-League-2021-2022': '',
                     'Ligue-1-2017-2018': '1632',
                     'Ligue-1-2018-2019': '2104',
                     'Ligue-1-2019-2020': '3243',
                     'Ligue-1-2020-2021': '10732',
                     'Ligue-1-2021-2022': '',
                     'Bundesliga-2017-2018': '1634',
                     'Bundesliga-2018-2019': '2109',
                     'Bundesliga-2019-2020': '3248',
                     'Bundesliga-2020-2021': '10737',
                     'Bundesliga-2021-2022': '',
                     'Serie-A-2017-2018': '1640',
                     'Serie-A-2018-2019': '1896',
                     'Serie-A-2019-2020': '3260',
                     'Serie-A-2020-2021': '10730',
                     'Serie-A-2021-2022': '',
                     'La-Liga-2017-2018': '1652',
                     'La-Liga-2018-2019': '1886',
                     'La-Liga-2019-2020': '3239',
                     'La-Liga-2020-2021': '10731',
                     'La-Liga-2021-2022': '',
                     'Major-League-Soccer': '22',
                     'Big-5-European-Leagues': 'Big5'
                    }

## Define list of long names for 'Big 5' European Leagues and MLS
lst_league_names_long = ['Premier-League', 'Ligue-1', 'Bundesliga', 'Serie-A', 'La-Liga', 'Major-League-Soccer']

## Define seasons to scrape
lst_seasons = ['2017-2018', '2018-2019', '2019-2020', '2020-2021', '2021-2022']

## Define list of folders
lst_folders = ['raw', 'engineered', 'reference']

## Define list of data types
lst_data_types = ['goalkeeper', 'outfield', 'team']

# Define function for scraping a defined season and competition of FBref player data
def get_fbref_squad_stats_player(lst_league_names, lst_seasons):
    
    """
    Function to...
    """
    
    ## Define list of league names
    league_names_long = lst_league_names
    
    
    ## Define seasons to scrape
    seasons = lst_seasons
    
    
    ## Start timer
    tic = datetime.datetime.now()
    
    
    ## Print time scraping started
    print(f'Scraping started at: {tic}')
    
    ##On supprime le fichier global afin de venir faire la MAJ
    os.remove(os.path.join(data_dir_fbref +f'/raw/team/fbref_team_player_stats_for_combined_latest.csv'))
    
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
            if not os.path.exists(os.path.join(data_dir_fbref +f'/raw/team/fbref_team_player_stats_for_combined_latest.csv')):

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

                  ##### Passing stats
                  print(f'Scraping Passing stats...')
                  url_passing = f'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fcomps%2F{league_name_short}%2F{saison_name_short}%2Fpassing%2Fplayers%2F{season}-{league_name_long}&div=div_stats_squads_passing_for'
                  df_passing = pd.read_html(url_passing, header=1)[0]

                  ##### Pass Types stats
                  print(f'Scraping Pass Types stats...')
                  url_passing_types = f'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fcomps%2F{league_name_short}%2F{saison_name_short}%2Fpassing_types%2Fplayers%2F{season}-{league_name_long}&div=div_stats_squads_passing_types_for'
                  df_passing_types = pd.read_html(url_passing_types, header=1)[0]

                  ##### Goals and Shot Creation stats
                  print(f'Scraping Goals and Shot Creation stats...')
                  url_gca = f'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fcomps%2F{league_name_short}%2F{saison_name_short}%2Fgca%2Fplayers%2F{season}-{league_name_long}&div=div_stats_squads_gca_for'
                  df_gca = pd.read_html(url_gca, header=1)[0]

                  ##### Defensive Actions stats
                  print(f'Scraping Defensive Actions stats...')
                  url_defense = f'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fcomps%2F{league_name_short}%2F{saison_name_short}%2Fdefense%2Fplayers%2F{season}-{league_name_long}&div=div_stats_squads_defense_for'
                  df_defense = pd.read_html(url_defense, header=1)[0]

                  ##### Possession stats
                  print(f'Scraping Possession stats...')
                  url_possession = f'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fcomps%2F{league_name_short}%2F{saison_name_short}%2Fpossession%2Fplayers%2F{season}-{league_name_long}&div=div_stats_squads_possession_for'
                  df_possession = pd.read_html(url_possession, header=1)[0]
                  df_possession = df_possession.rename({'Att': 'Att_dribbles'}, axis=1)
                  
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

                  ##### Passing stats
                  print(f'Scraping Passing stats...')
                  url_passing = f'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fcomps%2F{league_name_short}%2Fpassing%2Fplayers%2F{season}-{league_name_long}&div=div_stats_squads_passing_for'
                  df_passing = pd.read_html(url_passing, header=1)[0]

                  ##### Pass Types stats
                  print(f'Scraping Pass Types stats...')
                  url_passing_types = f'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fcomps%2F{league_name_short}%2Fpassing_types%2Fplayers%2F{season}-{league_name_long}&div=div_stats_squads_passing_types_for'
                  df_passing_types = pd.read_html(url_passing_types, header=1)[0]

                  ##### Goals and Shot Creation stats
                  print(f'Scraping Goals and Shot Creation stats...')
                  url_gca = f'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fcomps%2F{league_name_short}%2Fgca%2Fplayers%2F{season}-{league_name_long}&div=div_stats_squads_gca_for'
                  df_gca = pd.read_html(url_gca, header=1)[0]

                  ##### Defensive Actions stats
                  print(f'Scraping Defensive Actions stats...')
                  url_defense = f'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fcomps%2F{league_name_short}%2Fdefense%2Fplayers%2F{season}-{league_name_long}&div=div_stats_squads_defense_for'
                  df_defense = pd.read_html(url_defense, header=1)[0]

                  ##### Possession stats
                  print(f'Scraping Possession stats...')
                  url_possession = f'https://widgets.sports-reference.com/wg.fcgi?css=1&site=fb&url=%2Fen%2Fcomps%2F{league_name_short}%2Fpossession%2Fplayers%2F{season}-{league_name_long}&div=div_stats_squads_possession_for'
                  df_possession = pd.read_html(url_possession, header=1)[0]
                  df_possession = df_possession.rename({'Att': 'Att_dribbles'}, axis=1)
                  
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
                lst_dfs = [df_std_stats, df_shooting, df_passing, df_passing_types, df_gca, df_defense, df_possession]

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
                df_all = df_all.rename({'Gls.1': 'Gls/90','Ast.1':'Ast/90','G-PK.1':'G-PK/90','xG.1':'xG/90','xA.1':'xA/90','npxG.1':'npxG/90','npxG+xA.1':'npxG+xA/90',
                'Cmp.1':'Cmp_short','Att.1':'Att_short','Cmp%.1':'Cmp%_short','Cmp.2':'Cmp_medium','Att.2':'Att_medium','Cmp%.2':'Cmp%_medium',
                'Cmp.3':'Cmp_long','Att.3':'Att_long','Cmp%.3':'Cmp%_long','PassLive.1':'PassLive_AMB','PassDead.1':'PassDead_AMB','Drib.1':'Drib_AMB',
                'Sh.1':'Sh_AMB','Fld.1':'Fld_AMB','Def.1':'Def_AMB','Tkl.1':'Tkl_dribble','Def 3rd.1':'Def 3rd_pression','Mid 3rd.1':'Mid 3rd_pression',
                'Att 3rd.1':'Att 3rd_pression','Prog.1':'Prog_recevant','On-Off.1':'On-Off_diff_tit_remp'}, axis=1)            
                
                df_all['Squad'] = df_all['Squad'].str.replace('vs ','')
                
                ##### Save DataFrame
                df_all.to_csv(data_dir_fbref + f'/raw/team/{league_name_long}/{season}/fbref_team_player_stats_for_{league_name_long}_{season}_latest.csv', index=None, header=True)        
                
                ##### Export a copy to the 'archive' subfolder, including the date
                df_all.to_csv(data_dir_fbref + f'/raw/team/{league_name_long}/{season}/archive/fbref_team_player_stats_for_{league_name_long}_{season}_last_updated_{today}.csv', index=None, header=True)        
                
                
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
    all_files = glob.glob(os.path.join(data_dir_fbref + f'/raw/team/*/*/fbref_team_player_stats_for_*_*_latest.csv'))
    
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
    df_fbref_player_stats_all.to_csv(data_dir_fbref + f'/raw/team/fbref_team_player_stats_for_combined_latest.csv', index=None, header=True)
    
    ### Save a copy to archive folder (dated)
    df_fbref_player_stats_all.to_csv(data_dir_fbref + f'/raw/team/archive/fbref_team_player_stats_combined_for_last_updated_{today}.csv', index=None, header=True)
    
    
    
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
                os.mkdir(os.path.join(path, 'archive'))
                for league in lst_league_names_long:
                    path = os.path.join(data_dir_fbref, folder, data_types, league)
                    if not os.path.exists(path):
                        os.mkdir(path)
                        for season in lst_seasons:
                            path = os.path.join(data_dir_fbref, folder, data_types, league, season)
                            if not os.path.exists(path):
                                os.mkdir(path)
                                os.mkdir(os.path.join(path, 'archive'))

# Display all columns of pandas DataFrames
pd.set_option('display.max_columns', None)

lst_league_names = ['Ligue-1','Bundesliga', 'Serie-A', 'La-Liga','Premier-League']     #'Big-5-European-Leagues','Premier-League', 'Ligue-1', 'Bundesliga', 'Serie-A', 'La-Liga', 'Major-League-Soccer']
lst_seasons = ['2017-2018','2018-2019','2019-2020','2020-2021','2021-2022']

df_fbref_outfield_raw = get_fbref_squad_stats_player(lst_league_names, lst_seasons)

from sqlalchemy import create_engine
import pymysql
import pandas as pd
import pandas
 
tableName   = "fbref_team_player_stats_for"
        
sqlEngine       = create_engine('mysql+pymysql://root:root@127.0.0.1/foot', pool_recycle=3600)
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

