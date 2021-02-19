from django.shortcuts import render  
from django.http import HttpResponse  
from frontendworkflow.functions import handle_uploaded_file  #functions.py
from frontendworkflow.plot import plotit
from .forms import CustomerForm#forms.py
import pandas as pd
import os
import matplotlib.pyplot as plt
from matplotlib.pyplot import axis,show,pie

  
def index(request):  
    if request.method == 'POST':  
        Customer = CustomerForm(request.POST, request.FILES)  
        if Customer.is_valid():
            #Customer.save()  
            handle_uploaded_file(request.FILES['customer_Financial_Excel'])  
            model_instance = Customer.save(commit=False)
            model_instance.save()
            return HttpResponse("File uploaded successfuly")  
    else:  
        Customer= CustomerForm()  
        return render(request,'frontendworkflow/upload.html',{'form':Customer})  


def plotview(request):
    return render(request,'frontendworkflow/renderplot.html')