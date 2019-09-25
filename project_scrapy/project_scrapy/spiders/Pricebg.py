import scrapy
from project_scrapy.items import Xiaomi_bgItem
from xiaomi.models import Xiaomi, Xiaomi_bg

def format_float(my_value):
    return '{:,.2f}'.format(float(my_value))

class Bg231Spider(scrapy.Spider):
    name = "bg231"
    allowed_domains = ["banggood.com"]
    bg231 = Xiaomi_bg.objects.get(id=54)
    start_urls = [bg231.urlbg]

    def parse(self, response):
        price = response.xpath('//meta[@itemprop="description"]/@content').extract()[0][8:14]
        item = Xiaomi_bgItem()
        item['bg_id'] = 231
        item['titlebg'] = response.xpath('//img[@id="landingImage"]/@title').extract()[0]
        item['namebg'] = response.xpath('//img[@alt="Banggood"]/@alt').extract()[0]
        item['url_img_bg'] = response.xpath('//img[@id="landingImage"]/@src').extract()[0]
        item['pricebg'] = format_float(price)
        item['urlbg'] = response.url
        return item

class Bg214Spider(scrapy.Spider):
    name = "bg214"
    allowed_domains = ["banggood.com"]
    bgid = Xiaomi_bg.objects.get(id=2)
    start_urls = [bgid.urlbg]

    def parse(self, response):
        price = response.xpath('//meta[@itemprop="description"]/@content').extract()[0][8:14]
        item = Xiaomi_bgItem()
        item['bg_id'] = 214
        item['titlebg'] = response.xpath('//img[@id="landingImage"]/@title').extract()[0]
        item['namebg'] = response.xpath('//img[@alt="Banggood"]/@alt').extract()[0]
        item['url_img_bg'] = response.xpath('//img[@id="landingImage"]/@src').extract()[0]
        item['pricebg'] = format_float(price)
        item['urlbg'] = response.url
        return item

class Bg202Spider(scrapy.Spider):
    name = "bg202"
    allowed_domains = ["banggood.com"]
    bgid = Xiaomi_bg.objects.get(id=3)
    start_urls = [bgid.urlbg]

    def parse(self, response):
        price = response.xpath('//meta[@itemprop="description"]/@content').extract()[0][8:14]
        item = Xiaomi_bgItem()
        item['bg_id'] = 202
        item['titlebg'] = response.xpath('//img[@id="landingImage"]/@title').extract()[0]
        item['namebg'] = response.xpath('//img[@alt="Banggood"]/@alt').extract()[0]
        item['url_img_bg'] = response.xpath('//img[@id="landingImage"]/@src').extract()[0]
        item['pricebg'] = format_float(price)
        item['urlbg'] = response.url
        return item

class Bg240Spider(scrapy.Spider):
    name = "bg240"
    allowed_domains = ["banggood.com"]
    bgid = Xiaomi_bg.objects.get(id=5)
    start_urls = [bgid.urlbg]

    def parse(self, response):
        price = response.xpath('//meta[@itemprop="description"]/@content').extract()[0][8:14]
        item = Xiaomi_bgItem()
        item['bg_id'] = 240
        item['titlebg'] = response.xpath('//img[@id="landingImage"]/@title').extract()[0]
        item['namebg'] = response.xpath('//img[@alt="Banggood"]/@alt').extract()[0]
        item['url_img_bg'] = response.xpath('//img[@id="landingImage"]/@src').extract()[0]
        item['pricebg'] = format_float(price)
        item['urlbg'] = response.url
        return item

class Bg215Spider(scrapy.Spider):
    name = "bg215"
    allowed_domains = ["banggood.com"]
    bgid = Xiaomi_bg.objects.get(id=6)
    start_urls = [bgid.urlbg]

    def parse(self, response):
        price = response.xpath('//meta[@itemprop="description"]/@content').extract()[0][8:14]
        item = Xiaomi_bgItem()
        item['bg_id'] = 215
        item['titlebg'] = response.xpath('//img[@id="landingImage"]/@title').extract()[0]
        item['namebg'] = response.xpath('//img[@alt="Banggood"]/@alt').extract()[0]
        item['url_img_bg'] = response.xpath('//img[@id="landingImage"]/@src').extract()[0]
        item['pricebg'] = format_float(price)
        item['urlbg'] = response.url
        return item

class Bg230Spider(scrapy.Spider):
    name = "bg230"
    allowed_domains = ["banggood.com"]
    bgid = Xiaomi_bg.objects.get(id=7)
    start_urls = [bgid.urlbg]

    def parse(self, response):
        price = response.xpath('//meta[@itemprop="description"]/@content').extract()[0][8:14]
        item = Xiaomi_bgItem()
        item['bg_id'] = 230
        item['titlebg'] = response.xpath('//img[@id="landingImage"]/@title').extract()[0]
        item['namebg'] = response.xpath('//img[@alt="Banggood"]/@alt').extract()[0]
        item['url_img_bg'] = response.xpath('//img[@id="landingImage"]/@src').extract()[0]
        item['pricebg'] = format_float(price)
        item['urlbg'] = response.url
        return item

class Bg216Spider(scrapy.Spider):
    name = "bg216"
    allowed_domains = ["banggood.com"]
    bgid = Xiaomi_bg.objects.get(id=8)
    start_urls = [bgid.urlbg]

    def parse(self, response):
        price = response.xpath('//meta[@itemprop="description"]/@content').extract()[0][8:14]
        item = Xiaomi_bgItem()
        item['bg_id'] = 216
        item['titlebg'] = response.xpath('//img[@id="landingImage"]/@title').extract()[0]
        item['namebg'] = response.xpath('//img[@alt="Banggood"]/@alt').extract()[0]
        item['url_img_bg'] = response.xpath('//img[@id="landingImage"]/@src').extract()[0]
        item['pricebg'] = format_float(price)
        item['urlbg'] = response.url
        return item

class Bg205Spider(scrapy.Spider):
    name = "bg205"
    allowed_domains = ["banggood.com"]
    bgid = Xiaomi_bg.objects.get(id=9)
    start_urls = [bgid.urlbg]

    def parse(self, response):
        price = response.xpath('//meta[@itemprop="description"]/@content').extract()[0][8:14]
        item = Xiaomi_bgItem()
        item['bg_id'] = 205
        item['titlebg'] = response.xpath('//img[@id="landingImage"]/@title').extract()[0]
        item['namebg'] = response.xpath('//img[@alt="Banggood"]/@alt').extract()[0]
        item['url_img_bg'] = response.xpath('//img[@id="landingImage"]/@src').extract()[0]
        item['pricebg'] = format_float(price)
        item['urlbg'] = response.url
        return item

class Bg212Spider(scrapy.Spider):
    name = "bg212"
    allowed_domains = ["banggood.com"]
    bgid = Xiaomi_bg.objects.get(id=10)
    start_urls = [bgid.urlbg]

    def parse(self, response):
        price = response.xpath('//meta[@itemprop="description"]/@content').extract()[0][8:14]
        item = Xiaomi_bgItem()
        item['bg_id'] = 212
        item['titlebg'] = response.xpath('//img[@id="landingImage"]/@title').extract()[0]
        item['namebg'] = response.xpath('//img[@alt="Banggood"]/@alt').extract()[0]
        item['url_img_bg'] = response.xpath('//img[@id="landingImage"]/@src').extract()[0]
        item['pricebg'] = format_float(price)
        item['urlbg'] = response.url
        return item

class Bg227Spider(scrapy.Spider):
    name = "bg227"
    allowed_domains = ["banggood.com"]
    bgid = Xiaomi_bg.objects.get(id=11)
    start_urls = [bgid.urlbg]

    def parse(self, response):
        price = response.xpath('//meta[@itemprop="description"]/@content').extract()[0][8:14]
        item = Xiaomi_bgItem()
        item['bg_id'] = 227
        item['titlebg'] = response.xpath('//img[@id="landingImage"]/@title').extract()[0]
        item['namebg'] = response.xpath('//img[@alt="Banggood"]/@alt').extract()[0]
        item['url_img_bg'] = response.xpath('//img[@id="landingImage"]/@src').extract()[0]
        item['pricebg'] = format_float(price)
        item['urlbg'] = response.url
        return item

class Bg228Spider(scrapy.Spider):
    name = "bg228"
    allowed_domains = ["banggood.com"]
    bgid = Xiaomi_bg.objects.get(id=12)
    start_urls = [bgid.urlbg]

    def parse(self, response):
        price = response.xpath('//meta[@itemprop="description"]/@content').extract()[0][8:14]
        item = Xiaomi_bgItem()
        item['bg_id'] = 228
        item['titlebg'] = response.xpath('//img[@id="landingImage"]/@title').extract()[0]
        item['namebg'] = response.xpath('//img[@alt="Banggood"]/@alt').extract()[0]
        item['url_img_bg'] = response.xpath('//img[@id="landingImage"]/@src').extract()[0]
        item['pricebg'] = format_float(price)
        item['urlbg'] = response.url
        return item

class Bg203Spider(scrapy.Spider):
    name = "bg203"
    allowed_domains = ["banggood.com"]
    bgid = Xiaomi_bg.objects.get(id=13)
    start_urls = [bgid.urlbg]

    def parse(self, response):
        price = response.xpath('//meta[@itemprop="description"]/@content').extract()[0][8:14]
        item = Xiaomi_bgItem()
        item['bg_id'] = 203
        item['titlebg'] = response.xpath('//img[@id="landingImage"]/@title').extract()[0]
        item['namebg'] = response.xpath('//img[@alt="Banggood"]/@alt').extract()[0]
        item['url_img_bg'] = response.xpath('//img[@id="landingImage"]/@src').extract()[0]
        item['pricebg'] = format_float(price)
        item['urlbg'] = response.url
        return item

class Bg249Spider(scrapy.Spider):
    name = "bg249"
    allowed_domains = ["banggood.com"]
    bgid = Xiaomi_bg.objects.get(id=14)
    start_urls = [bgid.urlbg]

    def parse(self, response):
        price = response.xpath('//meta[@itemprop="description"]/@content').extract()[0][8:14]
        item = Xiaomi_bgItem()
        item['bg_id'] = 249
        item['titlebg'] = response.xpath('//img[@id="landingImage"]/@title').extract()[0]
        item['namebg'] = response.xpath('//img[@alt="Banggood"]/@alt').extract()[0]
        item['url_img_bg'] = response.xpath('//img[@id="landingImage"]/@src').extract()[0]
        item['pricebg'] = format_float(price)
        item['urlbg'] = response.url
        return item

class Bg225Spider(scrapy.Spider):
    name = "bg225"
    allowed_domains = ["banggood.com"]
    bgid = Xiaomi_bg.objects.get(id=15)
    start_urls = [bgid.urlbg]

    def parse(self, response):
        price = response.xpath('//meta[@itemprop="description"]/@content').extract()[0][8:14]
        item = Xiaomi_bgItem()
        item['bg_id'] = 225
        item['titlebg'] = response.xpath('//img[@id="landingImage"]/@title').extract()[0]
        item['namebg'] = response.xpath('//img[@alt="Banggood"]/@alt').extract()[0]
        item['url_img_bg'] = response.xpath('//img[@id="landingImage"]/@src').extract()[0]
        item['pricebg'] = format_float(price)
        item['urlbg'] = response.url
        return item

class Bg223Spider(scrapy.Spider):
    name = "bg223"
    allowed_domains = ["banggood.com"]
    bgid = Xiaomi_bg.objects.get(id=16)
    start_urls = [bgid.urlbg]

    def parse(self, response):
        price = response.xpath('//meta[@itemprop="description"]/@content').extract()[0][8:14]
        item = Xiaomi_bgItem()
        item['bg_id'] = 223
        item['titlebg'] = response.xpath('//img[@id="landingImage"]/@title').extract()[0]
        item['namebg'] = response.xpath('//img[@alt="Banggood"]/@alt').extract()[0]
        item['url_img_bg'] = response.xpath('//img[@id="landingImage"]/@src').extract()[0]
        item['pricebg'] = format_float(price)
        item['urlbg'] = response.url
        return item

class Bg201Spider(scrapy.Spider):
    name = "bg201"
    allowed_domains = ["banggood.com"]
    bgid = Xiaomi_bg.objects.get(id=17)
    start_urls = [bgid.urlbg]

    def parse(self, response):
        price = response.xpath('//meta[@itemprop="description"]/@content').extract()[0][8:14]
        item = Xiaomi_bgItem()
        item['bg_id'] = 201
        item['titlebg'] = response.xpath('//img[@id="landingImage"]/@title').extract()[0]
        item['namebg'] = response.xpath('//img[@alt="Banggood"]/@alt').extract()[0]
        item['url_img_bg'] = response.xpath('//img[@id="landingImage"]/@src').extract()[0]
        item['pricebg'] = format_float(price)
        item['urlbg'] = response.url
        return item

class Bg199Spider(scrapy.Spider):
    name = "bg199"
    allowed_domains = ["banggood.com"]
    bgid = Xiaomi_bg.objects.get(id=18)
    start_urls = [bgid.urlbg]

    def parse(self, response):
        price = response.xpath('//meta[@itemprop="description"]/@content').extract()[0][8:14]
        item = Xiaomi_bgItem()
        item['bg_id'] = 199
        item['titlebg'] = response.xpath('//img[@id="landingImage"]/@title').extract()[0]
        item['namebg'] = response.xpath('//img[@alt="Banggood"]/@alt').extract()[0]
        item['url_img_bg'] = response.xpath('//img[@id="landingImage"]/@src').extract()[0]
        item['pricebg'] = format_float(price)
        item['urlbg'] = response.url
        return item

class Bg217Spider(scrapy.Spider):
    name = "bg217"
    allowed_domains = ["banggood.com"]
    bgid = Xiaomi_bg.objects.get(id=19)
    start_urls = [bgid.urlbg]

    def parse(self, response):
        price = response.xpath('//meta[@itemprop="description"]/@content').extract()[0][8:14]
        item = Xiaomi_bgItem()
        item['bg_id'] = 217
        item['titlebg'] = response.xpath('//img[@id="landingImage"]/@title').extract()[0]
        item['namebg'] = response.xpath('//img[@alt="Banggood"]/@alt').extract()[0]
        item['url_img_bg'] = response.xpath('//img[@id="landingImage"]/@src').extract()[0]
        item['pricebg'] = format_float(price)
        item['urlbg'] = response.url
        return item

class Bg200Spider(scrapy.Spider):
    name = "bg200"
    allowed_domains = ["banggood.com"]
    bgid = Xiaomi_bg.objects.get(id=20)
    start_urls = [bgid.urlbg]

    def parse(self, response):
        price = response.xpath('//meta[@itemprop="description"]/@content').extract()[0][8:14]
        item = Xiaomi_bgItem()
        item['bg_id'] = 200
        item['titlebg'] = response.xpath('//img[@id="landingImage"]/@title').extract()[0]
        item['namebg'] = response.xpath('//img[@alt="Banggood"]/@alt').extract()[0]
        item['url_img_bg'] = response.xpath('//img[@id="landingImage"]/@src').extract()[0]
        item['pricebg'] = format_float(price)
        item['urlbg'] = response.url
        return item

class Bg229Spider(scrapy.Spider):
    name = "bg229"
    allowed_domains = ["banggood.com"]
    bgid = Xiaomi_bg.objects.get(id=21)
    start_urls = [bgid.urlbg]

    def parse(self, response):
        price = response.xpath('//meta[@itemprop="description"]/@content').extract()[0][8:14]
        item = Xiaomi_bgItem()
        item['bg_id'] = 229
        item['titlebg'] = response.xpath('//img[@id="landingImage"]/@title').extract()[0]
        item['namebg'] = response.xpath('//img[@alt="Banggood"]/@alt').extract()[0]
        item['url_img_bg'] = response.xpath('//img[@id="landingImage"]/@src').extract()[0]
        item['pricebg'] = format_float(price)
        item['urlbg'] = response.url
        return item

class Bg220Spider(scrapy.Spider):
    name = "bg220"
    allowed_domains = ["banggood.com"]
    bgid = Xiaomi_bg.objects.get(id=25)
    start_urls = [bgid.urlbg]

    def parse(self, response):
        price = response.xpath('//meta[@itemprop="description"]/@content').extract()[0][8:14]
        item = Xiaomi_bgItem()
        item['bg_id'] = 220
        item['titlebg'] = response.xpath('//img[@id="landingImage"]/@title').extract()[0]
        item['namebg'] = response.xpath('//img[@alt="Banggood"]/@alt').extract()[0]
        item['url_img_bg'] = response.xpath('//img[@id="landingImage"]/@src').extract()[0]
        item['pricebg'] = format_float(price)
        item['urlbg'] = response.url
        return item

class Bg219Spider(scrapy.Spider):
    name = "bg219"
    allowed_domains = ["banggood.com"]
    bgid = Xiaomi_bg.objects.get(id=26)
    start_urls = [bgid.urlbg]

    def parse(self, response):
        price = response.xpath('//meta[@itemprop="description"]/@content').extract()[0][8:14]
        item = Xiaomi_bgItem()
        item['bg_id'] = 219
        item['titlebg'] = response.xpath('//img[@id="landingImage"]/@title').extract()[0]
        item['namebg'] = response.xpath('//img[@alt="Banggood"]/@alt').extract()[0]
        item['url_img_bg'] = response.xpath('//img[@id="landingImage"]/@src').extract()[0]
        item['pricebg'] = format_float(price)
        item['urlbg'] = response.url
        return item

class Bg244Spider(scrapy.Spider):
    name = "bg244"
    allowed_domains = ["banggood.com"]
    bgid = Xiaomi_bg.objects.get(id=28)
    start_urls = [bgid.urlbg]

    def parse(self, response):
        price = response.xpath('//meta[@itemprop="description"]/@content').extract()[0][8:14]
        item = Xiaomi_bgItem()
        item['bg_id'] = 244
        item['titlebg'] = response.xpath('//img[@id="landingImage"]/@title').extract()[0]
        item['namebg'] = response.xpath('//img[@alt="Banggood"]/@alt').extract()[0]
        item['url_img_bg'] = response.xpath('//img[@id="landingImage"]/@src').extract()[0]
        item['pricebg'] = format_float(price)
        item['urlbg'] = response.url
        return item

class Bg246Spider(scrapy.Spider):
    name = "bg246"
    allowed_domains = ["banggood.com"]
    bgid = Xiaomi_bg.objects.get(id=30)
    start_urls = [bgid.urlbg]

    def parse(self, response):
        price = response.xpath('//meta[@itemprop="description"]/@content').extract()[0][8:14]
        item = Xiaomi_bgItem()
        item['bg_id'] = 246
        item['titlebg'] = response.xpath('//img[@id="landingImage"]/@title').extract()[0]
        item['namebg'] = response.xpath('//img[@alt="Banggood"]/@alt').extract()[0]
        item['url_img_bg'] = response.xpath('//img[@id="landingImage"]/@src').extract()[0]
        item['pricebg'] = format_float(price)
        item['urlbg'] = response.url
        return item

class Bg258Spider(scrapy.Spider):
    name = "bg258"
    allowed_domains = ["banggood.com"]
    bgid = Xiaomi_bg.objects.get(id=31)
    start_urls = [bgid.urlbg]

    def parse(self, response):
        price = response.xpath('//meta[@itemprop="description"]/@content').extract()[0][8:14]
        item = Xiaomi_bgItem()
        item['bg_id'] = 258
        item['titlebg'] = response.xpath('//img[@id="landingImage"]/@title').extract()[0]
        item['namebg'] = response.xpath('//img[@alt="Banggood"]/@alt').extract()[0]
        item['url_img_bg'] = response.xpath('//img[@id="landingImage"]/@src').extract()[0]
        item['pricebg'] = format_float(price)
        item['urlbg'] = response.url
        return item

class Bg255Spider(scrapy.Spider):
    name = "bg255"
    allowed_domains = ["banggood.com"]
    bgid = Xiaomi_bg.objects.get(id=45)
    start_urls = [bgid.urlbg]

    def parse(self, response):
        price = response.xpath('//meta[@itemprop="description"]/@content').extract()[0][8:14]
        item = Xiaomi_bgItem()
        item['bg_id'] = 255
        item['titlebg'] = response.xpath('//img[@id="landingImage"]/@title').extract()[0]
        item['namebg'] = response.xpath('//img[@alt="Banggood"]/@alt').extract()[0]
        item['url_img_bg'] = response.xpath('//img[@id="landingImage"]/@src').extract()[0]
        item['pricebg'] = format_float(price)
        item['urlbg'] = response.url
        return item

class Bg207Spider(scrapy.Spider):
    name = "bg207"
    allowed_domains = ["banggood.com"]
    bgid = Xiaomi_bg.objects.get(id=35)
    start_urls = [bgid.urlbg]

    def parse(self, response):
        price = response.xpath('//meta[@itemprop="description"]/@content').extract()[0][8:14]
        item = Xiaomi_bgItem()
        item['bg_id'] = 207
        item['titlebg'] = response.xpath('//img[@id="landingImage"]/@title').extract()[0]
        item['namebg'] = response.xpath('//img[@alt="Banggood"]/@alt').extract()[0]
        item['url_img_bg'] = response.xpath('//img[@id="landingImage"]/@src').extract()[0]
        item['pricebg'] = format_float(price)
        item['urlbg'] = response.url
        return item

class Bg245Spider(scrapy.Spider):
    name = "bg245"
    allowed_domains = ["banggood.com"]
    bgid = Xiaomi_bg.objects.get(id=36)
    start_urls = [bgid.urlbg]

    def parse(self, response):
        price = response.xpath('//meta[@itemprop="description"]/@content').extract()[0][8:14]
        item = Xiaomi_bgItem()
        item['bg_id'] = 245
        item['titlebg'] = response.xpath('//img[@id="landingImage"]/@title').extract()[0]
        item['namebg'] = response.xpath('//img[@alt="Banggood"]/@alt').extract()[0]
        item['url_img_bg'] = response.xpath('//img[@id="landingImage"]/@src').extract()[0]
        item['pricebg'] = format_float(price)
        item['urlbg'] = response.url
        return item

class Bg261Spider(scrapy.Spider):
    name = "bg261"
    allowed_domains = ["banggood.com"]
    bgid = Xiaomi_bg.objects.get(id=37)
    start_urls = [bgid.urlbg]

    def parse(self, response):
        price = response.xpath('//meta[@itemprop="description"]/@content').extract()[0][8:14]
        item = Xiaomi_bgItem()
        item['bg_id'] = 261
        item['titlebg'] = response.xpath('//img[@id="landingImage"]/@title').extract()[0]
        item['namebg'] = response.xpath('//img[@alt="Banggood"]/@alt').extract()[0]
        item['url_img_bg'] = response.xpath('//img[@id="landingImage"]/@src').extract()[0]
        item['pricebg'] = format_float(price)
        item['urlbg'] = response.url
        return item

class Bg213Spider(scrapy.Spider):
    name = "bg213"
    allowed_domains = ["banggood.com"]
    bgid = Xiaomi_bg.objects.get(id=38)
    start_urls = [bgid.urlbg]

    def parse(self, response):
        price = response.xpath('//meta[@itemprop="description"]/@content').extract()[0][8:14]
        item = Xiaomi_bgItem()
        item['bg_id'] = 213
        item['titlebg'] = response.xpath('//img[@id="landingImage"]/@title').extract()[0]
        item['namebg'] = response.xpath('//img[@alt="Banggood"]/@alt').extract()[0]
        item['url_img_bg'] = response.xpath('//img[@id="landingImage"]/@src').extract()[0]
        item['pricebg'] = format_float(price)
        item['urlbg'] = response.url
        return item

class Bg259Spider(scrapy.Spider):
    name = "bg259"
    allowed_domains = ["banggood.com"]
    bgid = Xiaomi_bg.objects.get(id=44)
    start_urls = [bgid.urlbg]

    def parse(self, response):
        price = response.xpath('//meta[@itemprop="description"]/@content').extract()[0][8:14]
        item = Xiaomi_bgItem()
        item['bg_id'] = 259
        item['titlebg'] = response.xpath('//img[@id="landingImage"]/@title').extract()[0]
        item['namebg'] = response.xpath('//img[@alt="Banggood"]/@alt').extract()[0]
        item['url_img_bg'] = response.xpath('//img[@id="landingImage"]/@src').extract()[0]
        item['pricebg'] = format_float(price)
        item['urlbg'] = response.url
        return item

class Bg254Spider(scrapy.Spider):
    name = "bg254"
    allowed_domains = ["banggood.com"]
    bgid = Xiaomi_bg.objects.get(id=46)
    start_urls = [bgid.urlbg]

    def parse(self, response):
        price = response.xpath('//meta[@itemprop="description"]/@content').extract()[0][8:14]
        item = Xiaomi_bgItem()
        item['bg_id'] = 254
        item['titlebg'] = response.xpath('//img[@id="landingImage"]/@title').extract()[0]
        item['namebg'] = response.xpath('//img[@alt="Banggood"]/@alt').extract()[0]
        item['url_img_bg'] = response.xpath('//img[@id="landingImage"]/@src').extract()[0]
        item['pricebg'] = format_float(price)
        item['urlbg'] = response.url
        return item

class Bg250Spider(scrapy.Spider):
    name = "bg250"
    allowed_domains = ["banggood.com"]
    bgid = Xiaomi_bg.objects.get(id=47)
    start_urls = [bgid.urlbg]

    def parse(self, response):
        price = response.xpath('//meta[@itemprop="description"]/@content').extract()[0][8:14]
        item = Xiaomi_bgItem()
        item['bg_id'] = 250
        item['titlebg'] = response.xpath('//img[@id="landingImage"]/@title').extract()[0]
        item['namebg'] = response.xpath('//img[@alt="Banggood"]/@alt').extract()[0]
        item['url_img_bg'] = response.xpath('//img[@id="landingImage"]/@src').extract()[0]
        item['pricebg'] = format_float(price)
        item['urlbg'] = response.url
        return item

class Bg257Spider(scrapy.Spider):
    name = "bg257"
    allowed_domains = ["banggood.com"]
    bgid = Xiaomi_bg.objects.get(id=59)
    start_urls = [bgid.urlbg]

    def parse(self, response):
        price = response.xpath('//meta[@itemprop="description"]/@content').extract()[0][8:14]
        item = Xiaomi_bgItem()
        item['bg_id'] = 257
        item['titlebg'] = response.xpath('//img[@id="landingImage"]/@title').extract()[0]
        item['namebg'] = response.xpath('//img[@alt="Banggood"]/@alt').extract()[0]
        item['url_img_bg'] = response.xpath('//img[@id="landingImage"]/@src').extract()[0]
        item['pricebg'] = format_float(price)
        item['urlbg'] = response.url
        return item

class Bg248Spider(scrapy.Spider):
    name = "bg248"
    allowed_domains = ["banggood.com"]
    bgid = Xiaomi_bg.objects.get(id=61)
    start_urls = [bgid.urlbg]

    def parse(self, response):
        price = response.xpath('//meta[@itemprop="description"]/@content').extract()[0][8:14]
        item = Xiaomi_bgItem()
        item['bg_id'] = 248
        item['titlebg'] = response.xpath('//img[@id="landingImage"]/@title').extract()[0]
        item['namebg'] = response.xpath('//img[@alt="Banggood"]/@alt').extract()[0]
        item['url_img_bg'] = response.xpath('//img[@id="landingImage"]/@src').extract()[0]
        item['pricebg'] = format_float(price)
        item['urlbg'] = response.url
        return item

class Bg260Spider(scrapy.Spider):
    name = "bg260"
    allowed_domains = ["banggood.com"]
    bgid = Xiaomi_bg.objects.get(id=66)
    start_urls = [bgid.urlbg]

    def parse(self, response):
        price = response.xpath('//meta[@itemprop="description"]/@content').extract()[0][8:14]
        item = Xiaomi_bgItem()
        item['bg_id'] = 260
        item['titlebg'] = response.xpath('//img[@id="landingImage"]/@title').extract()[0]
        item['namebg'] = response.xpath('//img[@alt="Banggood"]/@alt').extract()[0]
        item['url_img_bg'] = response.xpath('//img[@id="landingImage"]/@src').extract()[0]
        item['pricebg'] = format_float(price)
        item['urlbg'] = response.url
        return item

class Bg232Spider(scrapy.Spider):
    name = "bg232"
    allowed_domains = ["banggood.com"]
    bgid = Xiaomi_bg.objects.get(id=72)
    start_urls = [bgid.urlbg]

    def parse(self, response):
        price = response.xpath('//meta[@itemprop="description"]/@content').extract()[0][8:14]
        item = Xiaomi_bgItem()
        item['bg_id'] = 232
        item['titlebg'] = response.xpath('//img[@id="landingImage"]/@title').extract()[0]
        item['namebg'] = response.xpath('//img[@alt="Banggood"]/@alt').extract()[0]
        item['url_img_bg'] = response.xpath('//img[@id="landingImage"]/@src').extract()[0]
        item['pricebg'] = format_float(price)
        item['urlbg'] = response.url
        return item

class Bg256Spider(scrapy.Spider):
    name = "bg256"
    allowed_domains = ["banggood.com"]
    bgid = Xiaomi_bg.objects.get(id=75)
    start_urls = [bgid.urlbg]

    def parse(self, response):
        price = response.xpath('//meta[@itemprop="description"]/@content').extract()[0][8:14]
        item = Xiaomi_bgItem()
        item['bg_id'] = 256
        item['titlebg'] = response.xpath('//img[@id="landingImage"]/@title').extract()[0]
        item['namebg'] = response.xpath('//img[@alt="Banggood"]/@alt').extract()[0]
        item['url_img_bg'] = response.xpath('//img[@id="landingImage"]/@src').extract()[0]
        item['pricebg'] = format_float(price)
        item['urlbg'] = response.url
        return item

class Bg251Spider(scrapy.Spider):
    name = "bg251"
    allowed_domains = ["banggood.com"]
    bgid = Xiaomi_bg.objects.get(id=89)
    start_urls = [bgid.urlbg]

    def parse(self, response):
        price = response.xpath('//meta[@itemprop="description"]/@content').extract()[0][8:14]
        item = Xiaomi_bgItem()
        item['bg_id'] = 251
        item['titlebg'] = response.xpath('//img[@id="landingImage"]/@title').extract()[0]
        item['namebg'] = response.xpath('//img[@alt="Banggood"]/@alt').extract()[0]
        item['url_img_bg'] = response.xpath('//img[@id="landingImage"]/@src').extract()[0]
        item['pricebg'] = format_float(price)
        item['urlbg'] = response.url
        return item

class Bg247Spider(scrapy.Spider):
    name = "bg247"
    allowed_domains = ["banggood.com"]
    bgid = Xiaomi_bg.objects.get(id=110)
    start_urls = [bgid.urlbg]

    def parse(self, response):
        price = response.xpath('//meta[@itemprop="description"]/@content').extract()[0][8:14]
        item = Xiaomi_bgItem()
        item['bg_id'] = 247
        item['titlebg'] = response.xpath('//img[@id="landingImage"]/@title').extract()[0]
        item['namebg'] = response.xpath('//img[@alt="Banggood"]/@alt').extract()[0]
        item['url_img_bg'] = response.xpath('//img[@id="landingImage"]/@src').extract()[0]
        item['pricebg'] = format_float(price)
        item['urlbg'] = response.url
        return item

class Bg243Spider(scrapy.Spider):
    name = "bg243"
    allowed_domains = ["banggood.com"]
    bgid = Xiaomi_bg.objects.get(id=55)
    start_urls = [bgid.urlbg]

    def parse(self, response):
        price = response.xpath('//meta[@itemprop="description"]/@content').extract()[0][8:14]
        item = Xiaomi_bgItem()
        item['bg_id'] = 243
        item['titlebg'] = response.xpath('//img[@id="landingImage"]/@title').extract()[0]
        item['namebg'] = response.xpath('//img[@alt="Banggood"]/@alt').extract()[0]
        item['url_img_bg'] = response.xpath('//img[@id="landingImage"]/@src').extract()[0]
        item['pricebg'] = format_float(price)
        item['urlbg'] = response.url
        return item

class Bg242Spider(scrapy.Spider):
    name = "bg242"
    allowed_domains = ["banggood.com"]
    bgid = Xiaomi_bg.objects.get(id=54)
    start_urls = [bgid.urlbg]

    def parse(self, response):
        price = response.xpath('//meta[@itemprop="description"]/@content').extract()[0][8:14]
        item = Xiaomi_bgItem()
        item['bg_id'] = 242
        item['titlebg'] = response.xpath('//img[@id="landingImage"]/@title').extract()[0]
        item['namebg'] = response.xpath('//img[@alt="Banggood"]/@alt').extract()[0]
        item['url_img_bg'] = response.xpath('//img[@id="landingImage"]/@src').extract()[0]
        item['pricebg'] = format_float(price)
        item['urlbg'] = response.url
        return item

class Bg241Spider(scrapy.Spider):
    name = "bg241"
    allowed_domains = ["banggood.com"]
    bgid = Xiaomi_bg.objects.get(id=91)
    start_urls = [bgid.urlbg]

    def parse(self, response):
        price = response.xpath('//meta[@itemprop="description"]/@content').extract()[0][8:14]
        item = Xiaomi_bgItem()
        item['bg_id'] = 241
        item['titlebg'] = response.xpath('//img[@id="landingImage"]/@title').extract()[0]
        item['namebg'] = response.xpath('//img[@alt="Banggood"]/@alt').extract()[0]
        item['url_img_bg'] = response.xpath('//img[@id="landingImage"]/@src').extract()[0]
        item['pricebg'] = format_float(price)
        item['urlbg'] = response.url
        return item

class Bg237Spider(scrapy.Spider):
    name = "bg237"
    allowed_domains = ["banggood.com"]
    bgid = Xiaomi_bg.objects.get(id=90)
    start_urls = [bgid.urlbg]

    def parse(self, response):
        price = response.xpath('//meta[@itemprop="description"]/@content').extract()[0][8:14]
        item = Xiaomi_bgItem()
        item['bg_id'] = 237
        item['titlebg'] = response.xpath('//img[@id="landingImage"]/@title').extract()[0]
        item['namebg'] = response.xpath('//img[@alt="Banggood"]/@alt').extract()[0]
        item['url_img_bg'] = response.xpath('//img[@id="landingImage"]/@src').extract()[0]
        item['pricebg'] = format_float(price)
        item['urlbg'] = response.url
        return item

class Bg234Spider(scrapy.Spider):
    name = "bg234"
    allowed_domains = ["banggood.com"]
    bgid = Xiaomi_bg.objects.get(id=118)
    start_urls = [bgid.urlbg]

    def parse(self, response):
        price = response.xpath('//meta[@itemprop="description"]/@content').extract()[0][8:14]
        item = Xiaomi_bgItem()
        item['bg_id'] = 234
        item['titlebg'] = response.xpath('//img[@id="landingImage"]/@title').extract()[0]
        item['namebg'] = response.xpath('//img[@alt="Banggood"]/@alt').extract()[0]
        item['url_img_bg'] = response.xpath('//img[@id="landingImage"]/@src').extract()[0]
        item['pricebg'] = format_float(price)
        item['urlbg'] = response.url
        return item

class Bg233Spider(scrapy.Spider):
    name = "bg233"
    allowed_domains = ["banggood.com"]
    bgid = Xiaomi_bg.objects.get(id=21)
    start_urls = [bgid.urlbg]

    def parse(self, response):
        price = response.xpath('//meta[@itemprop="description"]/@content').extract()[0][8:14]
        item = Xiaomi_bgItem()
        item['bg_id'] = 233
        item['titlebg'] = response.xpath('//img[@id="landingImage"]/@title').extract()[0]
        item['namebg'] = response.xpath('//img[@alt="Banggood"]/@alt').extract()[0]
        item['url_img_bg'] = response.xpath('//img[@id="landingImage"]/@src').extract()[0]
        item['pricebg'] = format_float(price)
        item['urlbg'] = response.url
        return item

class Bg226Spider(scrapy.Spider):
    name = "bg226"
    allowed_domains = ["banggood.com"]
    bgid = Xiaomi_bg.objects.get(id=5)
    start_urls = [bgid.urlbg]

    def parse(self, response):
        price = response.xpath('//meta[@itemprop="description"]/@content').extract()[0][8:14]
        item = Xiaomi_bgItem()
        item['bg_id'] = 226
        item['titlebg'] = response.xpath('//img[@id="landingImage"]/@title').extract()[0]
        item['namebg'] = response.xpath('//img[@alt="Banggood"]/@alt').extract()[0]
        item['url_img_bg'] = response.xpath('//img[@id="landingImage"]/@src').extract()[0]
        item['pricebg'] = format_float(price)
        item['urlbg'] = response.url
        return item

class Bg224Spider(scrapy.Spider):
    name = "bg224"
    allowed_domains = ["banggood.com"]
    bgid = Xiaomi_bg.objects.get(id=130)
    start_urls = [bgid.urlbg]

    def parse(self, response):
        price = response.xpath('//meta[@itemprop="description"]/@content').extract()[0][8:14]
        item = Xiaomi_bgItem()
        item['bg_id'] = 224
        item['titlebg'] = response.xpath('//img[@id="landingImage"]/@title').extract()[0]
        item['namebg'] = response.xpath('//img[@alt="Banggood"]/@alt').extract()[0]
        item['url_img_bg'] = response.xpath('//img[@id="landingImage"]/@src').extract()[0]
        item['pricebg'] = format_float(price)
        item['urlbg'] = response.url
        return item

class Bg222Spider(scrapy.Spider):
    name = "bg222"
    allowed_domains = ["banggood.com"]
    bgid = Xiaomi_bg.objects.get(id=137)
    start_urls = [bgid.urlbg]

    def parse(self, response):
        price = response.xpath('//meta[@itemprop="description"]/@content').extract()[0][8:14]
        item = Xiaomi_bgItem()
        item['bg_id'] = 222
        item['titlebg'] = response.xpath('//img[@id="landingImage"]/@title').extract()[0]
        item['namebg'] = response.xpath('//img[@alt="Banggood"]/@alt').extract()[0]
        item['url_img_bg'] = response.xpath('//img[@id="landingImage"]/@src').extract()[0]
        item['pricebg'] = format_float(price)
        item['urlbg'] = response.url
        return item

class Bg221Spider(scrapy.Spider):
    name = "bg221"
    allowed_domains = ["banggood.com"]
    bgid = Xiaomi_bg.objects.get(id=136)
    start_urls = [bgid.urlbg]

    def parse(self, response):
        price = response.xpath('//meta[@itemprop="description"]/@content').extract()[0][8:14]
        item = Xiaomi_bgItem()
        item['bg_id'] = 221
        item['titlebg'] = response.xpath('//img[@id="landingImage"]/@title').extract()[0]
        item['namebg'] = response.xpath('//img[@alt="Banggood"]/@alt').extract()[0]
        item['url_img_bg'] = response.xpath('//img[@id="landingImage"]/@src').extract()[0]
        item['pricebg'] = format_float(price)
        item['urlbg'] = response.url
        return item

class Bg218Spider(scrapy.Spider):
    name = "bg218"
    allowed_domains = ["banggood.com"]
    bgid = Xiaomi_bg.objects.get(id=134)
    start_urls = [bgid.urlbg]

    def parse(self, response):
        price = response.xpath('//meta[@itemprop="description"]/@content').extract()[0][8:14]
        item = Xiaomi_bgItem()
        item['bg_id'] = 218
        item['titlebg'] = response.xpath('//img[@id="landingImage"]/@title').extract()[0]
        item['namebg'] = response.xpath('//img[@alt="Banggood"]/@alt').extract()[0]
        item['url_img_bg'] = response.xpath('//img[@id="landingImage"]/@src').extract()[0]
        item['pricebg'] = format_float(price)
        item['urlbg'] = response.url
        return item

class Bg211Spider(scrapy.Spider):
    name = "bg211"
    allowed_domains = ["banggood.com"]
    bgid = Xiaomi_bg.objects.get(id=104)
    start_urls = [bgid.urlbg]

    def parse(self, response):
        price = response.xpath('//meta[@itemprop="description"]/@content').extract()[0][8:14]
        item = Xiaomi_bgItem()
        item['bg_id'] = 211
        item['titlebg'] = response.xpath('//img[@id="landingImage"]/@title').extract()[0]
        item['namebg'] = response.xpath('//img[@alt="Banggood"]/@alt').extract()[0]
        item['url_img_bg'] = response.xpath('//img[@id="landingImage"]/@src').extract()[0]
        item['pricebg'] = format_float(price)
        item['urlbg'] = response.url
        return item

class Bg209Spider(scrapy.Spider):
    name = "bg209"
    allowed_domains = ["banggood.com"]
    bgid = Xiaomi_bg.objects.get(id=103)
    start_urls = [bgid.urlbg]

    def parse(self, response):
        price = response.xpath('//meta[@itemprop="description"]/@content').extract()[0][8:14]
        item = Xiaomi_bgItem()
        item['bg_id'] = 209
        item['titlebg'] = response.xpath('//img[@id="landingImage"]/@title').extract()[0]
        item['namebg'] = response.xpath('//img[@alt="Banggood"]/@alt').extract()[0]
        item['url_img_bg'] = response.xpath('//img[@id="landingImage"]/@src').extract()[0]
        item['pricebg'] = format_float(price)
        item['urlbg'] = response.url
        return item

class Bg210Spider(scrapy.Spider):
    name = "bg210"
    allowed_domains = ["banggood.com"]
    bgid = Xiaomi_bg.objects.get(id=121)
    start_urls = [bgid.urlbg]

    def parse(self, response):
        price = response.xpath('//meta[@itemprop="description"]/@content').extract()[0][8:14]
        item = Xiaomi_bgItem()
        item['bg_id'] = 210
        item['titlebg'] = response.xpath('//img[@id="landingImage"]/@title').extract()[0]
        item['namebg'] = response.xpath('//img[@alt="Banggood"]/@alt').extract()[0]
        item['url_img_bg'] = response.xpath('//img[@id="landingImage"]/@src').extract()[0]
        item['pricebg'] = format_float(price)
        item['urlbg'] = response.url
        return item

class Bg208Spider(scrapy.Spider):
    name = "bg208"
    allowed_domains = ["banggood.com"]
    bgid = Xiaomi_bg.objects.get(id=122)
    start_urls = [bgid.urlbg]

    def parse(self, response):
        price = response.xpath('//meta[@itemprop="description"]/@content').extract()[0][8:14]
        item = Xiaomi_bgItem()
        item['bg_id'] = 208
        item['titlebg'] = response.xpath('//img[@id="landingImage"]/@title').extract()[0]
        item['namebg'] = response.xpath('//img[@alt="Banggood"]/@alt').extract()[0]
        item['url_img_bg'] = response.xpath('//img[@id="landingImage"]/@src').extract()[0]
        item['pricebg'] = format_float(price)
        item['urlbg'] = response.url
        return item

class Bg206Spider(scrapy.Spider):
    name = "bg206"
    allowed_domains = ["banggood.com"]
    bgid = Xiaomi_bg.objects.get(id=105)
    start_urls = [bgid.urlbg]

    def parse(self, response):
        price = response.xpath('//meta[@itemprop="description"]/@content').extract()[0][8:14]
        item = Xiaomi_bgItem()
        item['bg_id'] = 206
        item['titlebg'] = response.xpath('//img[@id="landingImage"]/@title').extract()[0]
        item['namebg'] = response.xpath('//img[@alt="Banggood"]/@alt').extract()[0]
        item['url_img_bg'] = response.xpath('//img[@id="landingImage"]/@src').extract()[0]
        item['pricebg'] = format_float(price)
        item['urlbg'] = response.url
        return item

class Bg204Spider(scrapy.Spider):
    name = "bg204"
    allowed_domains = ["banggood.com"]
    bgid = Xiaomi_bg.objects.get(id=102)
    start_urls = [bgid.urlbg]

    def parse(self, response):
        price = response.xpath('//meta[@itemprop="description"]/@content').extract()[0][8:14]
        item = Xiaomi_bgItem()
        item['bg_id'] = 204
        item['titlebg'] = response.xpath('//img[@id="landingImage"]/@title').extract()[0]
        item['namebg'] = response.xpath('//img[@alt="Banggood"]/@alt').extract()[0]
        item['url_img_bg'] = response.xpath('//img[@id="landingImage"]/@src').extract()[0]
        item['pricebg'] = format_float(price)
        item['urlbg'] = response.url
        return item

class Bg196Spider(scrapy.Spider):
    name = "bg196"
    allowed_domains = ["banggood.com"]
    bgid = Xiaomi_bg.objects.get(id=100)
    start_urls = [bgid.urlbg]

    def parse(self, response):
        price = response.xpath('//meta[@itemprop="description"]/@content').extract()[0][8:14]
        item = Xiaomi_bgItem()
        item['bg_id'] = 196
        item['titlebg'] = response.xpath('//img[@id="landingImage"]/@title').extract()[0]
        item['namebg'] = response.xpath('//img[@alt="Banggood"]/@alt').extract()[0]
        item['url_img_bg'] = response.xpath('//img[@id="landingImage"]/@src').extract()[0]
        item['pricebg'] = format_float(price)
        item['urlbg'] = response.url
        return item

class Bg197Spider(scrapy.Spider):
    name = "bg197"
    allowed_domains = ["banggood.com"]
    bgid = Xiaomi_bg.objects.get(id=101)
    start_urls = [bgid.urlbg]

    def parse(self, response):
        price = response.xpath('//meta[@itemprop="description"]/@content').extract()[0][8:14]
        item = Xiaomi_bgItem()
        item['bg_id'] = 197
        item['titlebg'] = response.xpath('//img[@id="landingImage"]/@title').extract()[0]
        item['namebg'] = response.xpath('//img[@alt="Banggood"]/@alt').extract()[0]
        item['url_img_bg'] = response.xpath('//img[@id="landingImage"]/@src').extract()[0]
        item['pricebg'] = format_float(price)
        item['urlbg'] = response.url
        return item

class Bg198Spider(scrapy.Spider):
    name = "bg198"
    allowed_domains = ["banggood.com"]
    bgid = Xiaomi_bg.objects.get(id=99)
    start_urls = [bgid.urlbg]

    def parse(self, response):
        price = response.xpath('//meta[@itemprop="description"]/@content').extract()[0][8:14]
        item = Xiaomi_bgItem()
        item['bg_id'] = 198
        item['titlebg'] = response.xpath('//img[@id="landingImage"]/@title').extract()[0]
        item['namebg'] = response.xpath('//img[@alt="Banggood"]/@alt').extract()[0]
        item['url_img_bg'] = response.xpath('//img[@id="landingImage"]/@src').extract()[0]
        item['pricebg'] = format_float(price)
        item['urlbg'] = response.url
        return item