import pandas as pd
liste_Ligue_1 = [['e2d8892c/Paris-Saint-Germain-Stats',["2019-2020",'2020-2021','2021-2022']],['d298ef2c/Saint-Etienne-Stats',["2019-2020",'2020-2021','2021-2022']],
               ['fd4e0f7d/Lens-Stats',['2020-2021','2021-2022']],['132ebc33/Statistiques-Nice',['2019-2020','2020-2021','2021-2022']],
            ['69236f98/Statistiques-Angers',["2019-2020",'2020-2021','2021-2022']],['5725cc7b/Statistiques-Marseille',["2019-2020",'2020-2021','2021-2022']],
           ['fd6114db/Statistiques-Monaco',["2019-2020",'2020-2021','2021-2022']],['d2c87802/Statistiques-Lorient',['2020-2021','2021-2022']],
            ['cb188c0c/Statistiques-Lille',["2019-2020",'2020-2021','2021-2022']],['d7a486cd/Statistiques-Nantes',["2019-2020",'2020-2021','2021-2022']],
            ['d53c0b06/Statistiques-Lyon',["2019-2020",'2020-2021','2021-2022']],['b3072e00/Statistiques-Rennes',["2019-2020",'2020-2021','2021-2022']],
           ['c0d3eab4/Statistiques-Strasbourg',["2019-2020",'2020-2021','2021-2022']],['281b0e73/Statistiques-Montpellier',["2019-2020",'2020-2021','2021-2022']],
            ['7fdd64e0/Statistiques-Reims',["2019-2020",'2020-2021','2021-2022']], ['d9676424/Statistiques-Clermont-Foot',['2021-2022']],
            ['123f3efe/Statistiques-Bordeaux',["2019-2020",'2020-2021','2021-2022']],['54195385/Statistiques-Troyes',['2021-2022']],
           ['f83960ae/Statistiques-Metz',["2019-2020",'2020-2021','2021-2022']],['fb08dbb3/Statistiques-Brest',["2019-2020",'2020-2021','2021-2022']],
           ['8dfb7350/Statistiques-Dijon',["2019-2020",'2020-2021']],['1cbf5f9e/Statistiques-Nimes',["2019-2020",'2020-2021']],
           ['25622401/Statistiques-Amiens',["2019-2020"]],['3f8c4b5f/Statistiques-Toulouse',["2019-2020"]]]

liste_Serie_a = [['d48ad4ff/Statistiques-Napoli',["2019-2020",'2020-2021','2021-2022']],['dc56fe14/Statistiques-Milan',["2019-2020",'2020-2021','2021-2022']],
               ['d609edc0/Statistiques-Internazionale',["2019-2020",'2020-2021','2021-2022']],['cf74a709/Statistiques-Roma',["2019-2020",'2020-2021','2021-2022']], 
               ['421387cf/Statistiques-Fiorentina',["2019-2020",'2020-2021','2021-2022']],['1d8099f8/Statistiques-Bologna',["2019-2020",'2020-2021','2021-2022']], 
               ['e0652b02/Statistiques-Juventus',["2019-2020",'2020-2021','2021-2022']],['922493f3/Statistiques-Atalanta',["2019-2020",'2020-2021','2021-2022']], 
               ['7213da33/Statistiques-Lazio',["2019-2020",'2020-2021','2021-2022']],['a3d88bd8/Statistiques-Empoli',['2021-2022']], 
               ['105360fe/Statistiques-Torino',["2019-2020",'2020-2021','2021-2022']],['0e72edf2/Statistiques-Hellas-Verona',["2019-2020",'2020-2021','2021-2022']], 
               ['04eea015/Statistiques-Udinese',["2019-2020",'2020-2021','2021-2022']], ['e2befd26/Statistiques-Sassuolo',["2019-2020",'2020-2021','2021-2022']], 
                ['8ff9e3b3/Statistiques-Sampdoria',["2019-2020",'2020-2021','2021-2022']],['658bf2de/Statistiques-Genoa',["2019-2020",'2020-2021','2021-2022']], 
               ['af5d5982/Statistiques-Venezia',['2021-2022']],['c5577084/Statistiques-Salernitana',['2021-2022']], 
               ['68449f6d/Statistiques-Spezia',['2020-2021','2021-2022']],['c4260e09/Statistiques-Cagliari',["2019-2020",'2020-2021','2021-2022']], 
               ['4fcb34fd/Statistiques-Benevento',['2020-2021']],['3074d7b1/Statistiques-Crotone',['2020-2021']], 
               ['eab4234c/Statistiques-Parma',['2019-2020','2020-2021']],['ffcbe334/Statistiques-Lecce',['2019-2020']],
               ['4ef57aeb/Statistiques-Brescia',['2019-2020']],['1d2fe027/Statistiques-SPAL',['2019-2020']]]

liste_Liga = [['53a2f082/Statistiques-Real-Madrid',["2019-2020",'2020-2021','2021-2022']],['db3b9613/Statistiques-Atletico-Madrid',["2019-2020",'2020-2021','2021-2022']],
               ['e31d1cd9/Statistiques-Real-Sociedad',["2019-2020",'2020-2021','2021-2022']],['ad2be733/Statistiques-Sevilla',["2019-2020",'2020-2021','2021-2022']], 
               ['03c57e2b/Statistiques-Osasuna',["2019-2020",'2020-2021','2021-2022']],['98e8af82/Statistiques-Rayo-Vallecano',['2021-2022']], 
               ['2b390eca/Statistiques-Athletic-Club',["2019-2020",'2020-2021','2021-2022']],['dcc91a7b/Statistiques-Valencia',["2019-2020",'2020-2021','2021-2022']], 
               ['206d90db/Statistiques-Barcelona',["2019-2020",'2020-2021','2021-2022']],['fc536746/Statistiques-Real-Betis',['2021-2022']], 
               ['2a8183b3/Statistiques-Villarreal',["2019-2020",'2020-2021','2021-2022']],['2aa12281/Statistiques-Mallorca',["2019-2020",'2021-2022']], 
               ['a8661628/Statistiques-Espanyol',["2019-2020",'2021-2022']], ['6c8b07df/Statistiques-Elche',['2020-2021','2021-2022']], 
               ['ee7c297c/Statistiques-Cadiz',['2020-2021','2021-2022']],['f25da7fb/Statistiques-Celta-Vigo',["2019-2020",'2020-2021','2021-2022']], 
               ['a0435291/Statistiques-Granada',["2019-2020",'2020-2021','2021-2022']],['9800b6a1/Statistiques-Levante',["2019-2020",'2020-2021','2021-2022']], 
               ['8d6fd021/Statistiques-Alaves',["2019-2020",'2020-2021','2021-2022']],['7848bd64/Statistiques-Getafe',["2019-2020",'2020-2021','2021-2022']], 
               ['c6c493e6/Statistiques-Huesca',['2020-2021']],['17859612/Statistiques-Valladolid',["2019-2020",'2020-2021']],
               ['bea5c710/Statistiques-Eibar',["2019-2020",'2020-2021']]]
               
liste_Bundesliga = [['054efa67/Statistiques-Bayern-Munich',["2019-2020",'2020-2021','2021-2022']],['c7a9f859/Statistiques-Bayer-Leverkusen',["2019-2020",'2020-2021','2021-2022']],
               ['add600ae/Statistiques-Dortmund',["2019-2020",'2020-2021','2021-2022']],['a486e511/Statistiques-Freiburg',["2019-2020",'2020-2021','2021-2022']], 
               ['4eaa11d7/Statistiques-Wolfsburg',["2019-2020",'2020-2021','2021-2022']],['bc357bf7/Statistiques-Koln',["2019-2020",'2020-2021','2021-2022']], 
               ['7a41008f/Statistiques-Union-Berlin',["2019-2020",'2020-2021','2021-2022']],['acbb6a5b/Statistiques-RB-Leipzig',["2019-2020",'2020-2021','2021-2022']], 
               ['a224b06a/Statistiques-Mainz-05',["2019-2020",'2020-2021','2021-2022']],['32f3ee20/Statistiques-Monchengladbach',["2019-2020",'2020-2021','2021-2022']], 
               ['033ea6b8/Statistiques-Hoffenheim',["2019-2020",'2020-2021','2021-2022']],['598bc722/Statistiques-Stuttgart',['2020-2021','2021-2022']], 
               ['f0ac8ee6/Statistiques-Eintracht-Frankfurt',["2019-2020",'2020-2021','2021-2022']],['2818f8bc/Statistiques-Hertha-BSC',["2019-2020",'2020-2021','2021-2022']], 
               ['0cdc4311/Statistiques-Augsburg',["2019-2020",'2020-2021','2021-2022']],['247c4b67/Statistiques-Arminia',['2020-2021','2021-2022']], 
               ['b42c6323/Statistiques-Bochum',['2021-2022']],['12192a4c/Statistiques-Greuther-Furth',['2021-2022']], 
               ['62add3bf/Statistiques-Werder-Bremen',["2019-2020",'2020-2021']],['c539e393/Statistiques-Schalke-04',["2019-2020",'2020-2021']], 
               ['b1278397/Statistiques-Dusseldorf',["2019-2020"]],['d9f93f02/Statistiques-Paderborn-07',["2019-2020"]]]

liste_Premier_League = [['cff3d9bb/Statistiques-Chelsea',["2019-2020",'2020-2021','2021-2022']],['822bd0ba/Statistiques-Liverpool',["2019-2020",'2020-2021','2021-2022']],
               ['b8fd03ef/Statistiques-Manchester-City',["2019-2020",'2020-2021','2021-2022']],['19538871/Statistiques-Manchester-United',["2019-2020",'2020-2021','2021-2022']], 
               ['d3fd31cc/Statistiques-Everton',["2019-2020",'2020-2021','2021-2022']],['d07537b9/Statistiques-Brighton-and-Hove-Albion',["2019-2020",'2020-2021','2021-2022']], 
               ['cd051869/Statistiques-Brentford',['2021-2022']],['361ca564/Statistiques-Tottenham-Hotspur',["2019-2020",'2020-2021','2021-2022']], 
               ['7c21e445/Statistiques-West-Ham-United',["2019-2020",'2020-2021','2021-2022']],['8602292d/Statistiques-Aston-Villa',["2019-2020",'2020-2021','2021-2022']], 
               ['18bb7c10/Statistiques-Arsenal',["2019-2020",'2020-2021','2021-2022']],['8cec06e1/Statistiques-Wolverhampton-Wanderers',["2019-2020",'2020-2021','2021-2022']], 
               ['a2d435b3/Statistiques-Leicester-City',["2019-2020",'2020-2021','2021-2022']],['47c64c55/Statistiques-Crystal-Palace',["2019-2020",'2020-2021','2021-2022']], 
               ['2abfe087/Statistiques-Watford',["2019-2020",'2021-2022']],['5bfb9659/Statistiques-Leeds-United',['2020-2021','2021-2022']], 
               ['33c895d4/Statistiques-Southampton',["2019-2020",'2020-2021','2021-2022']],['943e8050/Statistiques-Burnley',["2019-2020",'2020-2021','2021-2022']], 
               ['b2b47a98/Statistiques-Newcastle-United',["2019-2020",'2020-2021','2021-2022']],['1c781004/Statistiques-Norwich-City',["2019-2020",'2021-2022']], 
               ['fd962109/Statistiques-Fulham',['2020-2021']],['60c6b05f/Statistiques-West-Bromwich-Albion',['2020-2021']], 
               ['1df6b87e/Statistiques-Sheffield-United',["2019-2020",'2020-2021']],['4ba7cbea/Statistiques-Bournemouth',["2019-2020"]]]


df_calendrier = pd.DataFrame()
#Fonction de récup et création du df calendrier
def creation_df_calendrier(nom_ligue,liste):
  df_cal = pd.DataFrame()
  for i in liste:
    print(i)
    for j in i[1]:
      dfnew=pd.read_html('https://fbref.com/en/squads/'+str(i[0][:9])+str(j)+'/'+str(i[0][9:]),header=0)[1]
      #On ajoute le nom du club, sa saion et sa ligue afin de permettre un filtre plus facile à posteriori
      dfnew['nom_club']=str(i[0][9:])
      dfnew['saison']=str(j)
      dfnew['ligue']=str(nom_ligue)
      df_cal=df_cal.append(dfnew,ignore_index=True)
  print(df_cal)
  #On supprime les deux colonnes qui ne nous serviront a rien
  del(df_cal['Match Report'])
  del(df_cal['Notes'])
  return df_cal

#On fait les appels pour les différentes ligues que nous voulons
df_calendrier = df_calendrier.append(creation_df_calendrier("Liga",liste_Liga),ignore_index=True)
df_calendrier = df_calendrier.append(creation_df_calendrier("Ligue1",liste_Ligue_1),ignore_index=True)
df_calendrier = df_calendrier.append(creation_df_calendrier("Première League",liste_Premier_League),ignore_index=True)
df_calendrier = df_calendrier.append(creation_df_calendrier("Bundesliga",liste_Bundesliga),ignore_index=True)
df_calendrier = df_calendrier.append(creation_df_calendrier("SerieA",liste_Serie_a),ignore_index=True)

df_calendrier['nom_club'] = df_calendrier['nom_club'].str.replace('Statistiques-','')

df_calendrier.to_csv('../CSV/calendrier.csv', sep=';', encoding='utf-8',index=False)

from sqlalchemy import create_engine
import pymysql
import pandas as pd
import pandas
 
tableName   = "fbref_calendrier"
        
sqlEngine       = create_engine('mysql+pymysql://root:root@127.0.0.1/foot', pool_recycle=3600)
dbConnection    = sqlEngine.connect()

try:
    frame = df_calendrier.to_sql(tableName, dbConnection, if_exists='replace');
except ValueError as vx:
    print(vx)
except Exception as ex:   
    print(ex)
else:
    print("Table %s created successfully."%tableName);   
finally:
    dbConnection.close()