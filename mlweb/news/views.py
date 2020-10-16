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
    News = readFronSqllite("./data/FXdata.db",selectNews)
    newsCount = len(News)
    context['pageCount'] = int(newsCount/10)
    context['news']=News[-10:]   #-10*i:10(1-i) pagination

    return render(request,'NewsPage.html',context)


def index_page(request, p1):
    context = {}
    selectNews="select articleTitle,articletime,articlecontent from fxNews"
    News = readFronSqllite("./data/FXdata.db",selectNews)
    newsCount = len(News)
    context['pageCount'] = int(newsCount/10)

    if(p1 > 1):
        context['news']=News[-10*p1:10*(1-p1)]   #-10*i:10(1-i) pagination
    else:
        context['news']=News[-10:]   #-10*i:10(1-i) pagination

    return render(request,'NewsPage.html',context)
