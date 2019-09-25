from django.db import models
from django.contrib import admin
from decimal import Decimal



class Xiaomi(models.Model):
    titlegb = models.CharField(max_length=512, default='')
    url_img_gb = models.URLField(max_length=2000, default='')
    namegb = models.CharField(max_length=50, default='', blank=True)
    pricegb = models.DecimalField(max_digits=15, decimal_places=2, default=Decimal(0))
    urlgb = models.URLField(max_length=2000, default='', blank=True)
    urlgb_patocinado = models.URLField(max_length=2000, default='', blank=True)
    titlebg = models.CharField(max_length=512, default='', blank=True)
    namebg = models.CharField(max_length=50, default='', blank=True)
    url_img_bg = models.URLField(max_length=2000, default='', blank=True)
    pricebg = models.DecimalField(max_digits=15, decimal_places=2, default=Decimal(0))
    urlbg = models.URLField(max_length=2000, default='', blank=True)
    urlbg_patocinado = models.URLField(max_length=2000, default='', blank=True)
    namedx = models.CharField(max_length=50, default='', blank=True)
    pricedx = models.DecimalField(max_digits=15, decimal_places=2, default=Decimal(0))
    urldx = models.URLField(max_length=2000, default='', blank=True)
    urldx_patocinado = models.URLField(max_length=2000, default='', blank=True)
    namein = models.CharField(max_length=50, default='', blank=True)
    pricein = models.DecimalField(max_digits=15, decimal_places=2, default=Decimal(0))
    urlin = models.URLField(max_length=2000, default='', blank=True)
    urlin_patocinado = models.URLField(max_length=2000, default='', blank=True)
    namemz = models.CharField(max_length=50, default='', blank=True)
    pricemz = models.DecimalField(max_digits=15, decimal_places=2, default=Decimal(0))
    urlmz = models.URLField(max_length=2000, default='', blank=True)
    urlmz_patocinado = models.URLField(max_length=2000, default='', blank=True)
    best_price = models.DecimalField(max_digits=15, decimal_places=2, default=Decimal(0))
    best_url = models.URLField(max_length=2000, default='', blank=True)
    best_name = models.CharField(max_length=50, default='', blank=True)

    def __str__(self):
        return self.titlegb


class Xiaomi_bg(models.Model):
    titlebg = models.CharField(max_length=512, default='')
    namebg = models.CharField(max_length=50, default='', blank=True)
    url_img_bg = models.URLField(max_length=2000, default='')
    pricebg = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0))
    urlbg = models.URLField(max_length=2000, default='', blank=True)

    def __str__(self):
        return self.titlebg

class Dolar(models.Model):
    dolar_real = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0))


class SearchXiaomi(admin.ModelAdmin):
    search_fields = ('titlegb', 'id')
    list_display = ('id', 'titlegb','pricegb', 'pricebg', 'pricedx', 'pricein')

class SearchXiaomi_bg(admin.ModelAdmin):
    search_fields = ('titlebg', 'id')
    list_display = ('id', 'titlebg','pricebg')
