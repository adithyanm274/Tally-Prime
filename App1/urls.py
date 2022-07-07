from django.urls import path,include
from.import views

urlpatterns = [

    path('',views.base,name='base'),
    path('home',views.homes,name='home'),
    path('group',views.groups,name='group'),
    path('ledger',views.ledgers,name='ledger'),
    path('voucher',views.voucher,name='voucher'),
    path('vouchpage',views.vouchpage,name='vouchpage'),
    path('currency',views.currency,name='currency'),
    path('currency_alter',views.currency_alter,name='currency_alter'),
    path('branch',views.branch,name='branch'),
    path('ledgerpages',views.ledgerpages,name='ledgerpages'),
    path('changecompony',views.changecompony,name='changecompony'),
    path('createcompony',views.createcompony,name='createcompony'),
    path('crtcompony',views.crtecompony,name='crtecompony'),
    path('selectcompony',views.selectcompony,name='selectcompony'),








]