import scrapy

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
        #item['title'] = sel.xpath('a/text()').extract()
        item['link'] = response.xpath("//a[@class='nav_bar_link']/@href").extract()
        bigs = []
        bigs = response.xpath("//a[@class='nav_bar_link']/@href")
        print "--------------------------------------------------"
        print bigs
        for big in item['link']:
            print "--------------------------------------------------"
            print big
            #item['desc'] = sel.xpath('text()').extract()
            item['title'] = big.xpath("//span[@class='review-text']").extract()
            yield item
