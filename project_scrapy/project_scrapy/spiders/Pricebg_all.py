import scrapy
from project_scrapy.items import Celular_bgItem
from celular.models import Celular

def format_float(my_value):
    return '{:,.2f}'.format(float(my_value))

def list_url():
    list_id = list(Celular.objects.values_list("id"))
    list_urlok = []
    list_idok = []
    for a in list_id:
        for f in a:
            dbbgid = Celular.objects.get(id=f)

            if dbbgid.urlbg.replace('"', '$'):
                list_urlok.append(dbbgid.urlbg)
                list_idok.append(f)

    #return list_urlok[:10], list_idok[:10]
    #return list_urlok[10:20], list_idok[10:20]
    #return list_urlok[20:30], list_idok[20:30]
    #return list_urlok[30:40], list_idok[30:40]
    #return list_urlok[40:50], list_idok[40:50]
    #return list_urlok[50:60], list_idok[50:60]
    #return list_urlok[60:70], list_idok[60:70]
    return list_urlok[70:80], list_idok[70:80]
    # return list_urlok[80:90], list_idok[80:90]
    # return list_urlok[90:100], list_idok[90:100]
    # return list_urlok[100:110], list_idok[100:110]
    # return list_urlok[110:120], list_idok[110:120]
    # return list_urlok[120:130], list_idok[120:130]

class list_urlok0Spider(scrapy.Spider):
    name = "bg0"
    allowed_domains = ["banggood.com"]
    start_urls = [list_url()[0][0]]


    def parse(self, response):
        price = response.xpath('//meta[@itemprop="description"]/@content').extract()[0][8:14]
        item = Celular_bgItem()
        item['bg_id'] = list_url()[1][0]
        item['titlebg'] = response.xpath('//img[@id="landingImage"]/@title').extract()[0]
        item['namebg'] = response.xpath('//img[@alt="Banggood"]/@alt').extract()[0]
        item['url_img_bg'] = response.xpath('//img[@id="landingImage"]/@src').extract()[0]
        item['pricebg'] = format_float(price)
        item['urlbg'] = response.url

        return item

class list_urlok1Spider(scrapy.Spider):
    name = "bg1"
    allowed_domains = ["banggood.com"]
    start_urls = [list_url()[0][1]]


    def parse(self, response):
        price = response.xpath('//meta[@itemprop="description"]/@content').extract()[0][8:14]
        item = Celular_bgItem()
        item['bg_id'] = list_url()[1][1]
        item['titlebg'] = response.xpath('//img[@id="landingImage"]/@title').extract()[0]
        item['namebg'] = response.xpath('//img[@alt="Banggood"]/@alt').extract()[0]
        item['url_img_bg'] = response.xpath('//img[@id="landingImage"]/@src').extract()[0]
        item['pricebg'] = format_float(price)
        item['urlbg'] = response.url

        return item

class list_urlok2Spider(scrapy.Spider):
    name = "bg2"
    allowed_domains = ["banggood.com"]
    start_urls = [list_url()[0][2]]


    def parse(self, response):
        price = response.xpath('//meta[@itemprop="description"]/@content').extract()[0][8:14]
        item = Celular_bgItem()
        item['bg_id'] = list_url()[1][2]
        item['titlebg'] = response.xpath('//img[@id="landingImage"]/@title').extract()[0]
        item['namebg'] = response.xpath('//img[@alt="Banggood"]/@alt').extract()[0]
        item['url_img_bg'] = response.xpath('//img[@id="landingImage"]/@src').extract()[0]
        item['pricebg'] = format_float(price)
        item['urlbg'] = response.url

        return item

class list_urlok3Spider(scrapy.Spider):
    name = "bg3"
    allowed_domains = ["banggood.com"]
    start_urls = [list_url()[0][3]]


    def parse(self, response):
        price = response.xpath('//meta[@itemprop="description"]/@content').extract()[0][8:14]
        item = Celular_bgItem()
        item['bg_id'] = list_url()[1][3]
        item['titlebg'] = response.xpath('//img[@id="landingImage"]/@title').extract()[0]
        item['namebg'] = response.xpath('//img[@alt="Banggood"]/@alt').extract()[0]
        item['url_img_bg'] = response.xpath('//img[@id="landingImage"]/@src').extract()[0]
        item['pricebg'] = format_float(price)
        item['urlbg'] = response.url

        return item

class list_urlok4Spider(scrapy.Spider):
    name = "bg4"
    allowed_domains = ["banggood.com"]
    start_urls = [list_url()[0][4]]


    def parse(self, response):
        price = response.xpath('//meta[@itemprop="description"]/@content').extract()[0][8:14]
        item = Celular_bgItem()
        item['bg_id'] = list_url()[1][4]
        item['titlebg'] = response.xpath('//img[@id="landingImage"]/@title').extract()[0]
        item['namebg'] = response.xpath('//img[@alt="Banggood"]/@alt').extract()[0]
        item['url_img_bg'] = response.xpath('//img[@id="landingImage"]/@src').extract()[0]
        item['pricebg'] = format_float(price)
        item['urlbg'] = response.url

        return item

class list_urlok5Spider(scrapy.Spider):
    name = "bg5"
    allowed_domains = ["banggood.com"]
    start_urls = [list_url()[0][5]]


    def parse(self, response):
        price = response.xpath('//meta[@itemprop="description"]/@content').extract()[0][8:14]
        item = Celular_bgItem()
        item['bg_id'] = list_url()[1][5]
        item['titlebg'] = response.xpath('//img[@id="landingImage"]/@title').extract()[0]
        item['namebg'] = response.xpath('//img[@alt="Banggood"]/@alt').extract()[0]
        item['url_img_bg'] = response.xpath('//img[@id="landingImage"]/@src').extract()[0]
        item['pricebg'] = format_float(price)
        item['urlbg'] = response.url

        return item

class list_urlok6Spider(scrapy.Spider):
    name = "bg6"
    allowed_domains = ["banggood.com"]
    start_urls = [list_url()[0][6]]


    def parse(self, response):
        price = response.xpath('//meta[@itemprop="description"]/@content').extract()[0][8:14]
        item = Celular_bgItem()
        item['bg_id'] = list_url()[1][6]
        item['titlebg'] = response.xpath('//img[@id="landingImage"]/@title').extract()[0]
        item['namebg'] = response.xpath('//img[@alt="Banggood"]/@alt').extract()[0]
        item['url_img_bg'] = response.xpath('//img[@id="landingImage"]/@src').extract()[0]
        item['pricebg'] = format_float(price)
        item['urlbg'] = response.url

        return item

class list_urlok7Spider(scrapy.Spider):
    name = "bg7"
    allowed_domains = ["banggood.com"]
    start_urls = [list_url()[0][7]]


    def parse(self, response):
        price = response.xpath('//meta[@itemprop="description"]/@content').extract()[0][8:14]
        item = Celular_bgItem()
        item['bg_id'] = list_url()[1][7]
        item['titlebg'] = response.xpath('//img[@id="landingImage"]/@title').extract()[0]
        item['namebg'] = response.xpath('//img[@alt="Banggood"]/@alt').extract()[0]
        item['url_img_bg'] = response.xpath('//img[@id="landingImage"]/@src').extract()[0]
        item['pricebg'] = format_float(price)
        item['urlbg'] = response.url

        return item

class list_urlok8Spider(scrapy.Spider):
    name = "bg8"
    allowed_domains = ["banggood.com"]
    start_urls = [list_url()[0][8]]


    def parse(self, response):
        price = response.xpath('//meta[@itemprop="description"]/@content').extract()[0][8:14]
        item = Celular_bgItem()
        item['bg_id'] = list_url()[1][8]
        item['titlebg'] = response.xpath('//img[@id="landingImage"]/@title').extract()[0]
        item['namebg'] = response.xpath('//img[@alt="Banggood"]/@alt').extract()[0]
        item['url_img_bg'] = response.xpath('//img[@id="landingImage"]/@src').extract()[0]
        item['pricebg'] = format_float(price)
        item['urlbg'] = response.url

        return item

class list_urlok9Spider(scrapy.Spider):
    name = "bg9"
    allowed_domains = ["banggood.com"]
    start_urls = [list_url()[0][9]]


    def parse(self, response):
        price = response.xpath('//meta[@itemprop="description"]/@content').extract()[0][8:14]
        item = Celular_bgItem()
        item['bg_id'] = list_url()[1][9]
        item['titlebg'] = response.xpath('//img[@id="landingImage"]/@title').extract()[0]
        item['namebg'] = response.xpath('//img[@alt="Banggood"]/@alt').extract()[0]
        item['url_img_bg'] = response.xpath('//img[@id="landingImage"]/@src').extract()[0]
        item['pricebg'] = format_float(price)
        item['urlbg'] = response.url

        return item