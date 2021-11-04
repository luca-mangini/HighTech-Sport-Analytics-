import pandas
df = pandas.read_csv('calendrier.csv',sep=";")
del df["Unnamed: 0"]
df.to_csv('calendrier.csv', sep=';', encoding='utf-8',index=False)