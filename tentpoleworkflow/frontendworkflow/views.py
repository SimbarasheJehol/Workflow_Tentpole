from django.shortcuts import render  
from django.http import HttpResponse  
from frontendworkflow.functions import handle_uploaded_file  #functions.py
from frontendworkflow.plot import plotit
from .forms import CustomerForm#forms.py
import pandas as pd
import os
import matplotlib.pyplot as plt
from matplotlib.pyplot import axis,show,pie
import io
from PIL import Image
from io import StringIO
import base64

  
def index(request):  
    if request.method == 'POST':  
        Customer = CustomerForm(request.POST, request.FILES)  
        if Customer.is_valid():
            #Customer.save()  
            handle_uploaded_file(request.FILES['customer_Financial_Excel'])  
            model_instance = Customer.save(commit=False)
            model_instance.save()
            my_sheet='Sheet1'
            file=request.FILES['customer_Financial_Excel']
            df = pd.read_excel(file, sheet_name = my_sheet)
            rs = df.groupby(df["Month"])["Expenses"].sum()
            categories = list(rs.index)
            values = list(rs.values)
            table_content = df.to_html(index=None)
            table_content = table_content.replace("<thead>","<thead class='thead-dark'>")
            table_content = table_content.replace('class="dataframe"',"class='table table-striped'")
            table_content = table_content.replace('border="1"',"")
            context = {"categories": categories, 'values': values, 'table_data':table_content}
            return render(request,'frontendworkflow/renderplot.html',context=context)  
    else:  
        Customer= CustomerForm()  
        return render(request,'frontendworkflow/upload.html',{'form':Customer})  


