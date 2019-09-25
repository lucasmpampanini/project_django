# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from .items import Xiaomi_gbItem, Xiaomi_bgItem, Xiaomi_dxItem, Xiaomi_inItem,\
    Xiaomi_gb_listItem, Xiaomi_bg_listItem
from xiaomi.models import Xiaomi, Xiaomi_bg



class ProjectScrapyPipeline(object):
    def process_item(self, item, spider):

        def Xiaomi_gb_list(self, item, spider):
            db = Xiaomi()
            db.titlegb = item['titlegb']
            db.url_img_gb = item['url_img_gb']
            db.namegb = item['namegb']
            db.pricegb = item['pricegb']
            db.urlgb = item['urlgb']
            db.save()
            return item

        def Xiaomi_bg_list(self, item, spider):
            db = Xiaomi_bg()
            db.titlebg = item['titlebg']
            db.namebg = item['namebg']
            db.url_img_bg = item['url_img_bg']
            db.pricebg = item['pricebg']
            db.urlbg = item['urlbg']
            db.save()
            return item

        def Xiaomi_gb(self, item, spider):
            db = Xiaomi.objects.get(id=item['gb_id'])
            db.titlegb = item['titlegb']
            db.url_img_gb = item['url_img_gb']
            db.namegb = item['namegb']
            db.pricegb = item['pricegb']
            db.urlgb = item['urlgb']
            db.save()
            return item

        def Xiaomi_bg(self, item, spider):
            db = Xiaomi.objects.get(id=item['bg_id'])
            db.titlebg = item['titlebg']
            db.namebg = item['namebg']
            db.url_img_bg = item['url_img_bg']
            db.pricebg = item['pricebg']
            db.urlbg = item['urlbg']
            db.save()
            return item

        def Xiaomi_dx(self, item, spider):
            db = Xiaomi.objects.get(id=item['dx_id'])
            db.namedx = item['namedx']
            db.pricedx = item['pricedx']
            db.urldx = item['urldx']
            db.save()
            return item

        def Xiaomi_in(self, item, spider):
            db = Xiaomi.objects.get(id=item['in_id'])
            db.namein = item['namein']
            db.pricein = item['pricein']
            db.urlin = item['urlin']
            db.save()
            return item

        if isinstance(item, Xiaomi_gb_listItem):
            return Xiaomi_gb_list(self, item, spider)

        if isinstance(item, Xiaomi_bg_listItem):
            return Xiaomi_bg_list(self, item, spider)

        if isinstance(item, Xiaomi_gbItem):
            return Xiaomi_gb(self, item, spider)

        if isinstance(item, Xiaomi_bgItem):
            return Xiaomi_bg(self, item, spider)

        if isinstance(item, Xiaomi_dxItem):
            return Xiaomi_dx(self, item, spider)

        if isinstance(item, Xiaomi_inItem):
            return Xiaomi_in(self, item, spider)



