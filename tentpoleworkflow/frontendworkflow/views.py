from django.shortcuts import render  
from django.http import HttpResponse  
#from myapp.functions import handle_uploaded_file  #functions.py
from .forms import CustomerForm#forms.py
  
def index(request):  
    if request.method == 'POST':  
        customer = CustomerForm(request.POST, request.FILES)  
        if customer.is_valid():  
            #handle_uploaded_file(request.FILES['file'])  
            model_instance = customer.save(commit=False)
            model_instance.save()
            return HttpResponse("File uploaded successfuly")  
    else:  
        customer= CustomerForm()  
        return render(request,'frontendworkflow/upload.html',{'form':customer})  