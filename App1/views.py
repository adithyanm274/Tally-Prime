from django.shortcuts import render

# Create your views here.

def base(request):
    return render(request, 'base.html')

def groups(request):
    return render(request,'group.html')  

def ledgers(request):
    return render(request,'ledger.html')    

def homes(request):
    return render(request,'home.html')       

    
