#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
import dash
from dash.dependencies import Output, Event, Input
import dash_core_components as dcc
import dash_html_components as html
import plotly
import plotly.graph_objs as go
import sqlite3
import pandas as pd
import datetime
import time

conn = sqlite3.connect('../cryptocurrency.db')
df2 = pd.read_sql("SELECT * FROM bitcoin ORDER BY last_updated DESC", conn)
#df1 = pd.read_sql("SELECT name FROM sqlite_master WHERE type='table'", conn)
#available_cryptocurrency = df1['Name']
#print (df1['name'])
available_crypto = "bitcoin"
date_value = df2['last_updated']
query = "SELECT * FROM " + available_crypto + " ORDER BY last_updated DESC"# LIMIT " + str(date_value)
df = pd.read_sql(query, conn)
#df = pd.read_sql("SELECT * FROM ? ORDER BY ? DESC LIMIT ?", conn, params=[available_crypto, 'last_updated', 4])
#df = pd.read_sql("SELECT * FROM sentiment WHERE tweet LIKE %s ORDER BY unix DESC LIMIT 1000", conn ,params=[sentiment_term,])
#print(df)
#print(df['last_updated'][::100].unique())

#X = df.index[-date_value:]
dff = df[df['last_updated'] > 1521985467]
dfff = dff[dff['last_updated'] < 1522342000]

#print(dfff)
#for date in df['last_updated'][::100].unique():
#    print(datetime.datetime.fromtimestamp(date).strftime('%m-%d %H:%M'))
    #print(int(date))
df2['date'] = pd.to_datetime(df['last_updated'], unit='s', utc=True)
#print(date): datetime.datetime.fromtimestamp(date).strftime('%m-%d %H:%M') for date in df2['last_updated'][::250].unique()
#for date in df2['date']:
#    df2['date'] = date.strftime('%m-%d')
marki = {}
for i in range(df2['date'].count()):
#    x.append(df2['date'][i].strftime('%m-%d'))
    #df2.iloc[i, 15] = df2['date'][i].strftime('%m-%d')
    if i == 0:
        marki[int(df2['last_updated'][i])] = df2['date'][i].strftime('%m-%d')
    else:
        if df2['date'][i-1].strftime('%m-%d') != df2['date'][i].strftime('%m-%d'):
            marki[int(df2['last_updated'][i])] = df2['date'][i].strftime('%m-%d')

    #df2['date'][i] = x
   #print(df2['date'][i].strftime('%m-%d'))
#print(df2['date'])
print(marki)
