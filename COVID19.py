import requests
from pandas.io.json import json_normalize
URL = "https://api.covid19india.org/data.json"
data = requests.get(url=URL).json()
covid19_df = json_normalize(data['statewise'])

#SUMMARIES OF DATA

df_morph = covid19_df[["state","statecode","active","confirmed","deaths"]].drop_duplicates()
df_morph

#Data file Converting json to excel

import csv, json
import pandas as pd
import numpy  as np
import matplotlib.pyplot as pt
import requests
file=pd.read_excel('D:\\covidexcel.xlsx')
file.fillna("undefined", inplace = True)
json_file = open('D:\\raw_data.json','w')
url = requests.get('https://api.covid19india.org/raw_data.json')
json_file.write(str(url.text))
json_file.close()
#to load json file into variable
data = json.load(open('D:\\raw_data.json'))
#writing into cvs file
output = csv.writer(open('D:\\covidcsv.csv','w'))
output.writerow(data['raw_data'][0].keys())
for row in data['raw_data']:
    output.writerow(row.values())
#converting cvs file to excel
read_file = pd.read_csv (r'D:\\covidcsv.csv',encoding="cp1252")
read_file.to_excel (r'D:\\covidexcel.xlsx', index = None, header=True)

#Line graph of gender represented

f=0
m=0
ud=0
for i in file['gender']:
    if(i=='M'):m=m+1
    elif(i=='F'):f=f+1
    else:ud=ud+1
print("-----> male :",m)
print("-----> female :",f)
print("-----> undefined :",ud)

gender=["Male","Female","Undefined"]
value=[m,f,ud]
pt.title("Gender Represented")
pt.xlabel("Gender")
pt.ylabel("Total number of people")
pt.plot(gender,value,color='red')
pt.grid(True)
pt.show()

#Pie Chart for Death,Deltadeaths,Recoverd & TotalRecovered

active=covid19_df['active'][0]
confirmed=covid19_df['confirmed'][0]
deltaconfirmed=covid19_df['deltaconfirmed'][0]
deaths=covid19_df['deaths'][0]
deltadeaths=covid19_df['deltadeaths'][0]
recovered=covid19_df['recovered'][0]
deltarecovered=covid19_df['deltarecovered'][0]
labels=['Death','Deltadeaths','Recoverd','TotalRecovered']
sizes=[deaths,deltadeaths,recovered,deltarecovered]
explode=[0.2,0.3,0,0]
colors = ['orange','red','lightblue','pink']
pt.figure(figsize = (10, 7))
pt.pie(sizes,labels=labels,colors=colors,shadow='true',autopct='%1.1f%%',explode=explode,startangle=90)

#State affected by percentage

import matplotlib.colors as pltc
import matplotlib.pyplot as plt
from random import sample
import requests
from pandas.io.json import json_normalize
URL = "https://api.covid19india.org/data.json"
data = requests.get(url=URL).json()
covid19_df = json_normalize(data['statewise'])
T='This graph is showing which States of india is affected by what percentage'
explode = (0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.1,0.10,0.11,0.12,0.13,0.14,0.15)
labels=covid19_df['state'][covid19_df["state"]!='Total']

all_colors = [ k for k,v in pltc.cnames.items() ]
    

for val in range(2):
    colors = sample(all_colors, len(labels))
fig = plt.figure(figsize=(28,27))
fig.patch.set_facecolor('xkcd:mint green')
size=covid19_df['confirmed'][covid19_df["state"]!='Total']
plt.pie(size,explode=explode, labels=labels, colors=colors,autopct='%1.1f%%',shadow=True,startangle=43)
plt.legend(labels, loc="best",shadow=True)
plt.axis('equal')
plt.title(T,bbox={'facecolor':'0.6', 'pad':10})
plt.show()
covid19_df.tail()

#Line Plot - Deaths and Recovered Statewise

import matplotlib.pyplot as plt 
import requests
from pandas.io.json import json_normalize
URL = "https://api.covid19india.org/data.json"
data = requests.get(url=URL).json()
covid19_df = json_normalize(data['statewise']) 
covid19_dfnew=covid19_df.drop(covid19_df.index[[0]])
plt.figure(figsize = (12, 7))
statecode=covid19_dfnew['statecode']
recovered=covid19_dfnew['recovered']
deaths=covid19_dfnew['deaths']
plt.plot(statecode, recovered, label='covid-19')
plt.plot(statecode, deaths, label='covid-19')
import itertools 
for (a,b) in zip(covid19_dfnew['statecode'], covid19_dfnew['state']):
    print(a , ' = ' , b)
    
#How this virus spread day by day start from day one to till date

import requests
import matplotlib.pyplot as plt
from random import sample
import matplotlib.colors as pltc
all_colors = [k for k,v in pltc.cnames.items()]
from pandas.io.json import json_normalize
URL = "https://api.covid19india.org/data.json"
data = requests.get(url=URL).json()
covid19_df = json_normalize(data['cases_time_series'])
T='By using this graph i am trying to show how this virus spread day by day start from day one to till date'
labels=covid19_df.index
for val in range(2):
 colors = sample(all_colors, len(labels))
fig = plt.figure(figsize=(28,27))
fig.patch.set_facecolor('xkcd:mint green')
plt.pie(covid19_df['dailyconfirmed'], labels=labels, colors=colors,autopct='%1.1f%%',shadow=True,startangle=120)
plt.legend(labels, loc="best",shadow=True)
plt.axis('equal')
plt.title(T,bbox={'facecolor':'0.8', 'pad':5})
plt.show()
covid19_df.tail()
