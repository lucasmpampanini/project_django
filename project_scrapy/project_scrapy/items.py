import scrapy

class Celular_gb_listItem(scrapy.Item):
    gb_id = scrapy.Field()
    titlegb = scrapy.Field()
    url_img_gb = scrapy.Field()
    namegb = scrapy.Field()
    pricegb = scrapy.Field()
    urlgb = scrapy.Field()

class Celular_bg_listItem(scrapy.Item):
    bg_id = scrapy.Field()
    titlebg = scrapy.Field()
    namebg = scrapy.Field()
    url_img_bg = scrapy.Field()
    pricebg = scrapy.Field()
    urlbg = scrapy.Field()

class Celular_gbItem(scrapy.Item):
    gb_id = scrapy.Field()
    titlegb = scrapy.Field()
    namegb = scrapy.Field()
    pricegb = scrapy.Field()
    urlgb = scrapy.Field()

class Celular_bgItem(scrapy.Item):
    bg_id = scrapy.Field()
    titlebg = scrapy.Field()
    namebg = scrapy.Field()
    url_img_bg = scrapy.Field()
    pricebg = scrapy.Field()
    urlbg = scrapy.Field()

class Celular_dxItem(scrapy.Item):
    dx_id = scrapy.Field()
    titledx = scrapy.Field()
    namedx = scrapy.Field()
    pricedx = scrapy.Field()
    urldx = scrapy.Field()

class Celular_inItem(scrapy.Item):
    in_id = scrapy.Field()
    namein = scrapy.Field()
    pricein = scrapy.Field()
    urlin = scrapy.Field()

class Loja_listItem(scrapy.Item):
    title = scrapy.Field()
    store = scrapy.Field()
    url_img = scrapy.Field()
    price = scrapy.Field()
    url = scrapy.Field()

class Loja_gb_listItem(scrapy.Item):
    gb_id = scrapy.Field()
    title = scrapy.Field()
    store = scrapy.Field()
    url_img = scrapy.Field()
    price = scrapy.Field()
    url = scrapy.Field()