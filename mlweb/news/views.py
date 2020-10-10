from django.shortcuts import render,HttpResponse
import sqlite3 as db

def readFronSqllite(db_path,exectCmd):
    conn = db.connect(db_path)  
    cursor=conn.cursor()     
    cursor.execute(exectCmd)    
    rows=cursor.fetchall()      
    return rows


def index(request):
    context = {}
    selectNews="select articleTitle,articletime,articlecontent from fxNews"
    News = readFronSqllite("../static/data/FXdata.db",selectNews)
    context['newsCount']=News.__len__
    context['news']=News[-10:]   #-10*i:10(1-i) pagination

    return render(request,'NewsPage.html',context)


