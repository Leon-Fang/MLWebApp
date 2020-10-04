from django.shortcuts import render
import pandas as pd
import sqlite3 as db


def readFronSqllite(db_path,exectCmd):
    conn = db.connect(db_path)  
    cursor=conn.cursor()     
    cursor.execute(exectCmd)    
    rows=cursor.fetchall()      
    return rows
   


def loadForexData(request):
    df = pd.read_csv("../static/data/GBPUSD_M15.csv",sep='\t')

    context = {}
    context['cols'] = df.columns.tolist()
    context['timestamp'] = df['Time'][:200].values.tolist()
    context['Open'] = df['Open'][:200].values.tolist()
    context['High'] = df['High'][:200].values.tolist()
    context['Low'] = df['Low'][:200].values.tolist()
    context['Close'] = df['Close'][:200].values.tolist()
    context['Volume'] = df['Volume'][:200].div(10000).values.tolist()    

    selectCalendar="select publishDate,publishTime,Country,Event,ReportPeriod,PublishData,PredictedData,PreValue,Importance,tendency from ecocalendar"
    selectNews="select articleTitle,articletime,articlecontent from fxNews"

    Calendars = readFronSqllite("../static/data/FXdata.db",selectCalendar)
    News = readFronSqllite("../static/data/FXdata.db",selectNews)

    context['canlendars']=Calendars[-30:]
    context['news']=News[-30:]

    return render(request,'Home.html', context)


