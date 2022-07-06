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


def voucher(request):
    return render(request,'voucher.html')

def vouchpage(request):
    return render(request,'vouchpage.html')  

def branch(request):
    return render(request,'branch.html')

def ledgerpages(request):
    return render(request,'ledgerpage.html')


def currency(request):
    # obj=CreateCurrency.objects.all()
    # context={'cur':obj,}
    return render(request, 'currency.html')         

def currency_alter(request):
    return render(request, 'currency_alter.html')

# def currency_alter(request):
#     cur=CreateCurrency.objects.get(id=pk)
#     return render(request,'currency_alter.html')
#     return render(request,'currency_alter.html',{'i':cur})


    
