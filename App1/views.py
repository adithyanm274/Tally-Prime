from django.shortcuts import render,redirect
from App1.models import crtcompony
from django.contrib import messages
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

def changecompony(request):
    return render(request, 'changecompony.html')

def createcompony(request):
    return render(request, 'createcompony.html')

def crtecompony(request):
    if request.method=='POST':
        comname=request.POST['componyname']
        mailingname=request.POST['mailingname']
        address=request.POST['address']
        state=request.POST['state']
        country=request.POST['country']
        pincode=request.POST['pincode']
        telphone=request.POST['telphone']
        mobile=request.POST['mobile']
        fax=request.POST['fax']
        email=request.POST['email']
        website=request.POST['website']
        fyearbgn=request.POST['fyearbgn']
        booksbgn=request.POST['booksbgn']
        curncysymbl=request.POST['curncysymbl']
        crncyname=request.POST['crncyname']
        # items=request.FILES['file']
        data=crtcompony(componyname=comname,
                    mailingname=mailingname,
                    address=address,
                    state=state,
                    country=country,
                    pincode=pincode,
                    telphone=telphone,
                    mobile=mobile,
                    fax=fax,
                    email=email,
                    website=website,
                    fyearbgn=fyearbgn,
                    booksbgn=booksbgn,
                    curncysymbl=curncysymbl,
                    crncyname=crncyname)
        data.save()
        messages.success(request,"Company Registered Successfully!")
        return redirect('/')

def changecompony(request):
    data=crtcompony.objects.all()
    return render(request,'changecompony.html',{'data':data})

def selectcompony(request):
    data=crtcompony.objects.all()
    return render(request,'selectcompony.html',{'data':data})
        
