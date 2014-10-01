import scrapy
from urlparse import urljoin
from scrapy.http import Request
from new1.items import DmozItem

class Dmoz1Spider(scrapy.Spider):
    name = "flip1page"
    allowed_domains = ["flipkart.com"]
    start_urls = [
        "http://www.flipkart.com/moto-e/product-reviews/ITMDVUWSYBGNBTHA
    ]
    
    def parse(self, response):
        #for sel in response.xpath('//ul/li'):
        item = DmozItem()
        items = []
        #item['title'] = sel.xpath('a/text()').extract()
        item['link'] = response.xpath("//a[@class='nav_bar_link']/@href").extract()
        bigs = []
        bigs = response.xpath("//a[@class='nav_bar_link']/@href")
        print "--------------------------------------------------"
        print bigs
        print "--------------------------------------------------"
        item['date'] = response.xpath("//div[@class='date line fk-font-small']").extract()
        item['desc'] = response.xpath("//span[@class='review-text']").extract()
        item['title'] = response.xpath("//div[@class='line fk-font-normal bmargin5 dark-gray']").extract()
        yield item
