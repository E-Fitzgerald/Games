import pandas as pd
import csv

df_1 = pd.read_csv('C:\\Users\FitzL\Desktop\census.csv')
df_2 = pd.read_csv('C:\\Users\FitzL\Desktop\log.csv')
#df_2 = pd.read_csv('C:\\Users\FitzL\Desktop\olympics.csv', index_col = 0, skiprows=1)
#print(df_1.head())

#print(df_1["SUMLEV"].unique())

df_1 = df_1[df_1["SUMLEV"]==50]
#print(df_1.head())

columns_to_keep = ["STNAME","CTYNAME","BIRTHS2010","BIRTHS2011","BIRTHS2012","BIRTHS2013","BIRTHS2014","BIRTHS2015","POPESTIMATE2010","POPESTIMATE2011","POPESTIMATE2012","POPESTIMATE2013","POPESTIMATE2014","POPESTIMATE2015"]
df_1 = df_1[columns_to_keep]
#print(df_1.head())

df_1 = df_1.set_index(["STNAME","CTYNAME"])
#print(df_1.head())

#print(df_1.loc[ [("Michigan","Washtenaw County"), ("Michigan", "Wayne County")] ])

#print(df_2.head())

df_2 = df_2.set_index('time')
df_2 = df_2.sort_index()
#print(df_2.head())