import pandas as pd
import os
import matplotlib.pyplot as plt
from matplotlib.pyplot import pie ,axis,show
from django.contrib.staticfiles.storage import staticfiles_storage
from .forms import CustomerForm
from django.http import HttpResponse
from django.shortcuts import render 





def plotit():
    my_sheet='Sheet1'
    file=request.FILES['customer_Financial_Excel']
    df = pd.read_excel(file, sheet_name = my_sheet)
    sums = df.groupby(df["Month"])["Expenses"].sum()
    axis('equal')
    pie(sums, labels=sums.index)
    plt.savefig('/frontendworkflow/static/upload/pie.png')
    
