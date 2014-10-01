import scrapy
from urlparse import urljoin
from scrapy.http import Request
from new1.items import DmozItem

class Dmoz1Spider(scrapy.Spider):
    name = "flip"
    allowed_domains = ["flipkart.com"]
    start_urls = [
        "http://www.flipkart.com/apple-16gb-ipad-mini-wi-fi/product-reviews/ITMDXF5ZQAVRTUZC"
    ]
    
    def parse(self, response):
        #for sel in response.xpath('//ul/li'):
        item = DmozItem()
        items = []
        #item['title'] = sel.xpath('a/text()').extract()
        #item['link'] = response.xpath("//a[@class='nav_bar_link']/@href").extract()
        bigs = response.xpath("//a[@class='nav_bar_link']/@href").extract()
        #item['date'] = response.xpath("//div[@class='date line fk-font-small']").extract()
        #item['desc'] = response.xpath("//span[@class='review-text']").extract()
        #item['title'] = response.xpath("//div[@class='line fk-font-normal bmargin5 dark-gray']").extract()
        #yield item
        for big in bigs:
            #item['linknext'] = big
            #yield item
            #item['desc'] = sel.xpath('text()').extract()
            #link = item['link'][0] if len(item['link']) else None
            if big:
                yield(Request(urljoin(response.url,big), callback=self.parse_link))
            else:
                yield items
            
    def parse_link(self, response):
        item = response.meta.get('item')
        item = DmozItem()
        item['linknext'] = response
        item['date'] = response.xpath("//div[@class='date line fk-font-small']").extract()
        item['desc'] = response.xpath("//span[@class='review-text']").extract()
        item['title'] = response.xpath("//div[@class='line fk-font-normal bmargin5 dark-gray']").extract()
        return item
