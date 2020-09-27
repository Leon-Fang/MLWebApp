from django.shortcuts import render,HttpResponse
import pandas as pd

def index(request):
    df = pd.read_csv("D:\github\MLWebApp\static\data\GBPUSD_M1.csv",sep='\t')
    context = {}
    context['headers'] = df.columns.tolist()
    context['timestamp'] = df['Time'][:10].values.tolist()
    context['Open'] = df['Open'][:10].values.tolist()
    context['High'] = df['High'][:10].values.tolist()
    context['Low'] = df['Low'][:10].values.tolist()
    context['Close'] = df['Close'][:10].values.tolist()
    context['Volume'] = df['Volume'][:10].values.tolist()
    return render(request,'AnalysisPage.html', context)

