from django.urls import path,include
from.import views

urlpatterns = [

    path('',views.base,name='base'),
    path('home',views.homes,name='home'),
    path('group',views.groups,name='group'),
    path('ledger',views.ledgers,name='ledger'),



]