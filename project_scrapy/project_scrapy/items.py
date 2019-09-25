import scrapy

class Xiaomi_gb_listItem(scrapy.Item):
    gb_id = scrapy.Field()
    titlegb = scrapy.Field()
    url_img_gb = scrapy.Field()
    namegb = scrapy.Field()
    pricegb = scrapy.Field()
    urlgb = scrapy.Field()

class Xiaomi_bg_listItem(scrapy.Item):
    bg_id = scrapy.Field()
    titlebg = scrapy.Field()
    namebg = scrapy.Field()
    url_img_bg = scrapy.Field()
    pricebg = scrapy.Field()
    urlbg = scrapy.Field()

class Xiaomi_gbItem(scrapy.Item):
    gb_id = scrapy.Field()
    titlegb = scrapy.Field()
    url_img_gb = scrapy.Field()
    namegb = scrapy.Field()
    pricegb = scrapy.Field()
    urlgb = scrapy.Field()

class Xiaomi_bgItem(scrapy.Item):
    bg_id = scrapy.Field()
    titlebg = scrapy.Field()
    namebg = scrapy.Field()
    url_img_bg = scrapy.Field()
    pricebg = scrapy.Field()
    urlbg = scrapy.Field()

class Xiaomi_dxItem(scrapy.Item):
    dx_id = scrapy.Field()
    namedx = scrapy.Field()
    pricedx = scrapy.Field()
    urldx = scrapy.Field()

class Xiaomi_inItem(scrapy.Item):
    in_id = scrapy.Field()
    namein = scrapy.Field()
    pricein = scrapy.Field()
    urlin = scrapy.Field()