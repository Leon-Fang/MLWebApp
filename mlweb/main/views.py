from django.shortcuts import render,HttpResponse
import pandas as pd

def index(request):
    df = pd.read_csv("../static/data/GBPUSD_M1.csv",sep='\t')
    context = {}
    context['cols'] = df.columns.tolist()
    context['timestamp'] = df['Time'][:1000].values.tolist()
    context['Open'] = df['Open'][:1000].values.tolist()
    context['High'] = df['High'][:1000].values.tolist()
    context['Low'] = df['Low'][:1000].values.tolist()
    context['Close'] = df['Close'][:1000].values.tolist()
    context['Volume'] = df['Volume'][:1000].div(100).values.tolist()    

    return render(request,'AnalysisPage.html', context)
