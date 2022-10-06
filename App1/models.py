from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.contrib.auth.models import User
from locale import currency
from unicodedata import decimal

# Create your models here.

class crtcompony(models.Model):
    componyname = models.CharField(max_length=50)
    mailingname = models.CharField (max_length=50)
    address = models.CharField (max_length=50)
    state = models.CharField (max_length=50)
    country = models.CharField (max_length=50)
    pincode = models.CharField (max_length=10)
    telphone = models.CharField(max_length=10)
    mobile = models.CharField(max_length=10)
    fax = models.CharField(max_length=10)
    email=models.EmailField()
    website=models.CharField(max_length=100)
    fyearbgn=models.DateField()
    booksbgn=models.DateField()
    curncysymbl=models.CharField(max_length=10)
    crncyname=models.CharField(max_length=10)

    def __str__(self):
        return self.name


class VoucherModels(models.Model):
    voucher_name = models.CharField(max_length=225)
    alias = models.CharField(max_length=225)
    voucher_type = models.CharField(max_length=225)
    abbreviation = models.CharField(max_length=225)
    active_this_voucher_type =  models.CharField(max_length=225)
    method_voucher_numbering = models.CharField(max_length=225)
    use_adv_conf = models.CharField(max_length=225,blank=True)
    prvnt_duplictes = models.CharField(max_length=225,default="Null",blank=True)
    use_effective_date =  models.CharField(max_length=225,default="Null")
    allow_zero_value_trns =  models.CharField(max_length=225)
    allow_naration_in_voucher =  models.CharField(max_length=225)
    make_optional =  models.CharField(max_length=225)
    provide_naration =  models.CharField(max_length=225)
    print_voucher = models.CharField(max_length=225)
  
    def __str__(self):
        return self.name

class CreateCurrency(models.Model):
    symbol =models.CharField(max_length=225)
    formal_name=models.CharField(max_length=225)
    ISO_code=models.CharField(max_length=225)
    decimal_places= models.CharField(max_length=225,default=2)
    show_in_millions =  models.CharField(max_length=225)
    suffix_to_amount=  models.CharField(max_length=225)
    space_symbol_amount = models.CharField(max_length=225)
    word_after_decimal = models.CharField(max_length=225)
    decimal_no_in_words = models.CharField(max_length=225)

    def __str__(self):
        return self.name

class CurrencyAlter(models.Model):
    cname= models.ForeignKey( CreateCurrency,on_delete=models.CASCADE,default=1)
    slno = models.CharField(max_length=225)
    currencys = models.CharField(max_length=225)
    stdrate =models.CharField(max_length=225)
    lastvrate =models.CharField(max_length=225)
    specirate =models.CharField(max_length=225)
    lastvrate2 =models.CharField(max_length=225)
    specirate2 =models.CharField(max_length=225)
    
    def __str__(self):
        return self.name

class GroupModel(models.Model):
    name =  models.CharField(max_length=225,default="Null",blank=True)
    alias =  models.CharField(max_length=225,default="Null",blank=True)
    under =models.CharField(max_length=225,default="Null",blank=True)
    nature_of_group = models.CharField(max_length=225,default="Null",blank=True)
    does_it_affect =models.CharField(max_length=225,default="Null",blank=True)
    gp_behaves_like_sub_ledger =  models.CharField(max_length=225,default="Null",blank=True)
    nett_debit_credit_bal_reporting =  models.CharField(max_length=225,default="Null",blank=True)
    used_for_calculation =  models.CharField(max_length=225,default="Null",blank=True)
    method_to_allocate_usd_purchase =  models.CharField(max_length=225,default="Null",blank=True)

    def __str__(self):
        return self.name



class LedgerModels(models.Model):
    ledger_name = models.CharField(max_length=225)
    alias = models.CharField(max_length=225)
    under = models.CharField(max_length=225)
    mail_name = models.CharField(max_length=225)
    mail_address =  models.CharField(max_length=225)
    mail_state = models.CharField(max_length=225)
    mail_country = models.CharField(max_length=225,blank=True)
    mail_pincode = models.CharField(max_length=225,default="Null",blank=True)
    bank_details =  models.CharField(max_length=225,default="Null")
    pan_no =  models.CharField(max_length=225)
    registration_type =  models.CharField(max_length=225)
    gst_in =  models.CharField(max_length=225)
    alter_gst =  models.CharField(max_length=225)
  
    def __str__(self):
        return self.name    


       