from django.urls import path,include
from.import views


urlpatterns = [

    path('',views.base,name='base'),
    path('home',views.home,name='home'),
    path('group',views.group,name='group'),
    path('branch',views.branch,name='branch'),
    path('ledger',views.ledger,name='ledger'),
    path('voucher',views.voucher,name='voucher'),
    path('vouchpage',views.vouchpage,name='vouchpage'),
    path('currency',views.currency,name='currency'),
    path('currency_alter/<int:pk>',views.currency_alter,name='currency_alter'),


    # path('save_currency_data',views.save_currency_data,name="save_currency_data"),
    path('load_create_currency',views.load_create_currency,name='load_create_currency'),
    path('create_currency',views.create_currency,name='create_currency'),
    path('update_currency/<int:pk>',views.update_currency,name='update_currency'),
    path('load_create_vouchertyp',views.load_create_vouchertyp,name='load_create_vouchertyp'),
    path('create_voucher',views.create_voucher,name="create_voucher"),
    path('update_voucher/<int:pk>',views.update_voucher,name="update_voucher"),
    path('save_voucher/<int:pk>',views.save_voucher,name="save_voucher"),





    
]