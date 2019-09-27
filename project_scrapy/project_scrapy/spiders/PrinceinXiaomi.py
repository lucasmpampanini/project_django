import scrapy
from project_scrapy.items import Xiaomi_inItem
from xiaomi.models import Xiaomi

def format_float(my_value):
    return '{:,.2f}'.format(float(my_value))

def list_url():
    list_id = list(Xiaomi.objects.values_list("id"))
    list_urlok = []
    list_idok = []
    for a in list_id:
        for f in a:
            dbxiaomiid = Xiaomi.objects.get(id=f)

            if dbxiaomiid.urlin.replace('"', '$'):
                list_urlok.append(dbxiaomiid.urlin)
                list_idok.append(f)

    return list_urlok, list_idok

class list_urlok0Spider(scrapy.Spider):
    name = "in0"
    allowed_domains = ["lightinthebox.com"]
    start_urls = [list_url()[0][0]]


    def parse(self, response):
        price = response.xpath('//strong[@itemprop="price"]//text()').extract()[0][7:13]
        item = Xiaomi_inItem()
        item['in_id'] = list_url()[1][0]
        item['namein'] = response.xpath('//div[@class="litb-logo"]//a/@title').extract()[0]
        item['pricein'] = format_float(price)
        item['urlin'] = response.url

        return item

class list_urlok1Spider(scrapy.Spider):
    name = "in1"
    allowed_domains = ["lightinthebox.com"]
    start_urls = [list_url()[0][1]]


    def parse(self, response):
        price = response.xpath('//strong[@itemprop="price"]//text()').extract()[0][7:13]
        item = Xiaomi_inItem()
        item['in_id'] = list_url()[1][1]
        item['namein'] = response.xpath('//div[@class="litb-logo"]//a/@title').extract()[0]
        item['pricein'] = format_float(price)
        item['urlin'] = response.url

        return item