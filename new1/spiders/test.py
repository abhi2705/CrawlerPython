import scrapy
from scrapy.http import Request
from scrapy.selector import Selector
from scrapy.spider import BaseSpider

from new1.items import DmozItem

class Dmoz1Spider(scrapy.Spider):
    name = "test"
    allowed_domains = ["flipkart.com"]
    start_urls = [
        "http://www.flipkart.com/google-nexus-5/product-reviews/ITMDZKKQHQXYC64R"
    ]

    def parse(self, response):
        #for sel in response.xpath('//ul/li'):
            #hxs = HtmlXPathSelector(response)
            sel = Selector(response)
	    bigs = sel.select("//a[@class='nav_bar_link']/@href").extract()
            items = []
            item = DmozItem()
            yield bigs
    #return(items)
