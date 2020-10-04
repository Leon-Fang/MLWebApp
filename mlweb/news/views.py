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
    context['news']=News[-10:]

    return render(request,'NewsPage.html',context)


