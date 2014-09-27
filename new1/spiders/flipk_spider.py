import scrapy
from urlparse import urljoin
from scrapy.http import Request
from new1.items import DmozItem

class Dmoz1Spider(scrapy.Spider):
    name = "flip"
    allowed_domains = ["flipkart.com"]
    start_urls = [
        "http://www.flipkart.com/google-nexus-5/product-reviews/ITMDZKKQHQXYC64R"
    
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
        for big in item['link']:
            print "--------------------------------------------------"
            print big
            #item['desc'] = sel.xpath('text()').extract()
            #link = item['link'][0] if len(item['link']) else None
            if big:
                yield Request(urljoin(response.url, big),
                    callback=self.parse_link,
                    errback=lambda _: item,
                    meta=dict(item=item),
                    )
                print "iiiiiiiiiiiiiiiiiiiiiiiiiiiiiii"
                print item
                print "iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii"
            else:
                yield items
            
    def parse_link(self, response):
        item = response.meta.get('item')
        item['title'] = response.xpath("//span[@class='review-text']").extract()
        return item
