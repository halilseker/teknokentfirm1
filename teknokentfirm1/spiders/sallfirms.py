# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class SallfirmsSpider(CrawlSpider):
    name = 'sallfirms'
    allowed_domains = ['sakaryada.com']
    start_urls = ['http://sakaryada.com/']

    rules = (
        Rule(LinkExtractor(restrict_xpaths=("//div[@class='block']/ul/li/a")), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        print(response.url)
