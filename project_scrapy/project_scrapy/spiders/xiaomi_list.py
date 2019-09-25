import scrapy
from project_scrapy.items import Xiaomi_gb_listItem, Xiaomi_bg_listItem


class Xiaomi_GbSpider(scrapy.Spider):
    name = "xiaomi_gb"
    allowed_domains = ["gearbest.com"]
    start_urls = ['https://br.gearbest.com/celulares-c_11293/?brand=xiaomi&odr=new&page_size=120']

    def parse(self, response):
        title_list = response.xpath('//div[@class="gbGoodsItem_outBox"]//p//a/@title').extract()
        url_img_list = response.xpath('//ul[@class="clearfix js_seachResultList"]//li//a//img/@data-lazy').extract()
        price_list = response.xpath('//div[@class="gbGoodsItem_outBox"]//p/@data-currency').extract()
        url_list = response.xpath('//div[@class="gbGoodsItem_outBox"]//p//a[@class="gbGoodsItem_title   "]//@href').extract()
        i = 0

        for url in url_list:
            item = Xiaomi_gb_listItem()
            item['titlegb'] = title_list[i]
            item['url_img_gb'] = url_img_list[i]
            item['namegb'] = response.xpath('//img[@class="footerLogo_img"]/@alt').extract()[0]
            item['pricegb'] = format_float(price_list[i])
            item['urlgb'] = url
            if i != len(title_list):
                i = i + 1
            yield item

class Xiaomi_BgSpider(scrapy.Spider):
    name = "xiaomi_bg"
    allowed_domains = ["banggood.com"]
    #start_urls = ['https://www.banggood.com/Wholesale-Smartphones-c-1567.html?brand=520']
    #start_urls = ['https://www.banggood.com/Wholesale-Smartphones-c-1567-0-1-1-36-0_page2.html?brand=520']
    #start_urls = ['https://www.banggood.com/Wholesale-Smartphones-c-1567-0-1-1-36-0_page3.html?brand=520']
    #start_urls = ['https://www.banggood.com/Wholesale-Smartphones-c-1567-0-1-1-36-0_page4.html?brand=520']

    def parse(self, response):
        title_list = response.xpath('//a[@data-point-id="18206083330"]/@title').extract()
        url_img_list = response.xpath('//img[@class="bg_lazy"]/@src').extract()
        price_list = response.xpath('//span[@class="price wh_cn"]/@oriattrmin').extract()
        url_list = response.xpath('//a[@data-point-id="18206083330"]/@href').extract()
        i = 0

        for url in url_list:
            item = Xiaomi_bg_listItem()
            item['titlebg'] = title_list[i]
            item['namebg'] = response.xpath('//img[@class="logo1"]/@alt').extract()[0]
            item['url_img_bg'] = url_img_list[i]
            item['pricebg'] = format_float(price_list[i])
            item['urlbg'] = url
            if i != len(title_list):
                i = i + 1

            yield item

def format_float(my_value):
    return '{:,.2f}'.format(float(my_value))