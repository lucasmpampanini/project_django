import scrapy
from project_scrapy.items import Xiaomi_dxItem

def format_float(my_value):
    return '{:,.2f}'.format(float(my_value))

class Dx205Spider(scrapy.Spider):
    name = "dx205"
    allowed_domains = ["dx.com"]
    start_urls = ['https://www.dx.com/p/original-global-version-xiaomi-mi-a3-4g-phablet-with-4gb-ram-64gb-rom-6088-inch-octacore-4030mah-battery-smartphone-eu-plug-2628818#.XXsIbvcpBhQ']

    def parse(self, response):
        price = response.xpath('//i[@class="low-sale-price"]//text()').extract()[0]
        item = Xiaomi_dxItem()
        item['dx_id'] = 205
        item['namedx'] = response.xpath('//div[@class="logo fl"]//a//img/@id').extract()[0]
        item['pricedx'] = format_float(price)
        item['urldx'] = response.url
        return item