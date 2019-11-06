# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class SautekfirmsSpider(CrawlSpider):
    name = 'sautekfirms'
    allowed_domains = ['sakaryateknokent.com']
    start_urls = ['http://www.sakaryateknokent.com']
    rules = (
        Rule(LinkExtractor(deny=('/cv-ekle', '/staj-basvurusu'),
                           restrict_xpaths="//div[@class='mpc-callout__button']/a"),
             callback='parse_item',
             follow=True),
    )

    def parse_item(self, response):
        print(response.url)
