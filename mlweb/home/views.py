from django.shortcuts import render
import pandas as pd

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

    

    return render(request,'Home.html', context)
