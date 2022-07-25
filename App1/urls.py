from django.urls import path,include
from.import views


urlpatterns = [

    path('',views.base,name='base'),
    path('home',views.home,name='home'),
    path('branch',views.branch,name='branch'),
#----change Company------#
    path('changecompony',views.changecompony,name='changecompony'),
    path('createcompony',views.createcompony,name='createcompony'),
    path('crtcompony',views.crtecompony,name='crtecompony'),
    path('selectcompony',views.selectcompony,name='selectcompony'),



#-----Create Currency-------#
    path('currency',views.currency,name='currency'),
    path('currency_alter/<int:pk>',views.currency_alter,name='currency_alter'),
    path('save_currency_data',views.save_currency_data,name="save_currency_data"),
    path('load_create_currency',views.load_create_currency,name='load_create_currency'),
    path('create_currency',views.create_currency,name='create_currency'),
    path('update_currency/<int:pk>',views.update_currency,name='update_currency'),

#-----Create Voucher--------#   
    path('voucher',views.voucher,name='voucher'),
    # path('vouchpage',views.vouchpage,name='vouchpage'),
    path('load_create_vouchertyp',views.load_create_vouchertyp,name='load_create_vouchertyp'),
    path('create_voucher',views.create_voucher,name="create_voucher"),
    path('update_voucher/<int:pk>',views.update_voucher,name="update_voucher"),
    path('save_voucher/<int:pk>',views.save_voucher,name="save_voucher"),

#-----Create Group----------#
    path('group',views.group,name='group'),
    path('branch',views.branch,name='branch'),
    path('load_create_group1',views.load_create_group1,name='load_create_group1'),
    path('load_create_groups',views.load_create_groups,name="load_create_groups"),
    path('create_group',views.create_group,name="create_group"),
    path('update_grp/<int:pk>',views.update_grp,name="update_grp"),

#-----Create Ledger---------#   
    path('ledger',views.ledger,name='ledger'),
    path('ledgerpage',views.ledgerpage,name='ledgerpage'),
    path('load_create_ledgertype',views.load_create_ledgertyp,name='load_create_ledgertyp'),
    path('create_ledger',views.create_ledger,name="create_ledger"),
    path('update_ledger/<int:pk>',views.update_ledger,name="update_ledger"),
    path('save_ledger/<int:pk>',views.save_ledger,name="save_ledger"),





]