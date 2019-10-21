# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from .items import Celular_bg_listItem, Celular_gb_listItem, Celular_bgItem, Celular_dxItem, Celular_gbItem, Celular_inItem, \
    Loja_listItem, Loja_gb_listItem

from celular.models import Celular
from loja.models import Loja



class ProjectScrapyPipeline(object):
    def process_item(self, item, spider):

        def Celular_gb_list(self, item, spider):
            db = Celular()
            db.titlegb = item['titlegb']
            db.url_img_gb = item['url_img_gb']
            db.namegb = item['namegb']
            db.pricegb = item['pricegb']
            db.urlgb = item['urlgb']
            db.save()
            return item

        def Celular_bg_list(self, item, spider):
            db = Celular()
            db.titlebg = item['titlebg']
            db.namebg = item['namebg']
            db.url_img_bg = item['url_img_bg']
            db.pricebg = item['pricebg']
            db.urlbg = item['urlbg']
            db.save()
            return item

        def Celular_gb(self, item, spider):
            db = Celular.objects.get(id=item['gb_id'])
            db.titlegb = item['titlegb']
            db.namegb = item['namegb']
            db.pricegb = item['pricegb']
            db.urlgb = item['urlgb']
            db.save()
            return item

        def Celular_bg(self, item, spider):
            db = Celular.objects.get(id=item['bg_id'])
            db.titlebg = item['titlebg']
            db.namebg = item['namebg']
            db.url_img_bg = item['url_img_bg']
            db.pricebg = item['pricebg']
            db.urlbg = item['urlbg']
            db.save()
            return item

        def Celular_dx(self, item, spider):
            db = Celular.objects.get(id=item['dx_id'])
            db.titledx = item['titledx']
            db.namedx = item['namedx']
            db.pricedx = item['pricedx']
            db.urldx = item['urldx']
            db.save()
            return item

        def Celular_in(self, item, spider):
            db = Celular.objects.get(id=item['in_id'])
            db.namein = item['namein']
            db.pricein = item['pricein']
            db.urlin = item['urlin']
            db.save()
            return item

        def Loja_list(self, item, spider):
            db = Loja()
            db.title = item['title']
            db.store = item['store']
            db.url_img = item['url_img']
            db.price = item['price']
            db.url = item['url']
            db.save()
            return item

        def Loja_gb(self, item, spider):
            db = Loja.objects.get(id=item['gb_id'])
            db.title = item['title']
            db.store = item['store']
            db.price = item['price']
            db.url = item['url']
            db.save()
            return item

        if isinstance(item, Celular_gb_listItem):
            return Celular_gb_list(self, item, spider)

        if isinstance(item, Celular_bg_listItem):
            return Celular_bg_list(self, item, spider)

        if isinstance(item, Celular_gbItem):
            return Celular_gb(self, item, spider)

        if isinstance(item, Celular_bgItem):
            return Celular_bg(self, item, spider)

        if isinstance(item, Celular_dxItem):
            return Celular_dx(self, item, spider)

        if isinstance(item, Celular_inItem):
            return Celular_in(self, item, spider)

        if isinstance(item, Loja_listItem):
            return Loja_list(self, item, spider)

        if isinstance(item, Loja_gb_listItem):
            return Loja_gb(self, item, spider)



