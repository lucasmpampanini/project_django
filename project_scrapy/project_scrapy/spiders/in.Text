import scrapy
from project_scrapy.items import Xiaomi_inItem

def format_float(my_value):
    return '{:,.2f}'.format(float(my_value))

class In205Spider(scrapy.Spider):
    name = "in205"
    allowed_domains = ["lightinthebox.com"]
    start_urls = ['https://www.lightinthebox.com/pt/p/xiaomi-mi-a3-global-version-6-088-polegada-celular-4g-4gb-64gb-2-mp-8-mp-48-mp-qualcomm-snapdragon-665-4030-mah-mah_p7506227.html?prm=1.5.1.1&country_code=br&currency=BRL']

    def parse(self, response):
        price = response.xpath('//strong[@itemprop="price"]//text()').extract()[0][7:13]
        item = Xiaomi_inItem()
        item['in_id'] = 205
        item['namein'] = response.xpath('//div[@class="litb-logo"]//a/@title').extract()[0]
        item['pricein'] = format_float(price)
        item['urlin'] = response.url
        return item

class In202Spider(scrapy.Spider):
    name = "in202"
    allowed_domains = ["lightinthebox.com"]
    start_urls = ['https://www.lightinthebox.com/pt/p/xiaomi-mi-9t-global-version-6-39-polegada-celular-4g-6gb-64gb-8-mp-13-mp-48-mp-qualcomm-snapdragon-730-4000-mah-mah_p7401310.html?prm=1.5.1.1&sku=1_45']

    def parse(self, response):
        price = response.xpath('//strong[@itemprop="price"]//text()').extract()[0][7:13]
        item = Xiaomi_inItem()
        item['in_id'] = 202
        item['namein'] = response.xpath('//div[@class="litb-logo"]//a/@title').extract()[0]
        item['pricein'] = format_float(price)
        item['urlin'] = response.url
        return item