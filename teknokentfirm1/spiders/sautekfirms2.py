# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class Sautekfirms2Spider(CrawlSpider):
    name = 'sautekfirms2'
    allowed_domains = ['sakaryateknokent.com']
    start_urls = ['http://sakaryateknokent.com/']

    # rules = (
    #     Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    # )
    #
    # def parse_item(self, response):
    #     item = {}
    #     #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
    #     #item['name'] = response.xpath('//div[@id="name"]').get()
    #     #item['description'] = response.xpath('//div[@id="description"]').get()
    #     return item
    rules = (
        Rule(LinkExtractor(deny=('/cv-ekle', '/staj-basvurusu'),
                           restrict_xpaths="//div[@class='mpc-callout__button']/a"),
             callback='parse_item',
             follow=True),
        # Rule(LinkExtractor(restrict_xpaths="//li[@class='next']/a")),
    )

    def parse_item(self, response):
        ftitles = response.xpath("//h3/span/strong/text()").getall()
        frepresentatives = response.xpath("(//tr[1]/td/text())").getall()
        # yield {
        #     'firm_title': ftitle,
        #     'firm_representative': frepresentative
        # }
        # item = {}
        # item['firm_title'] = response.xpath('//h3/span/strong/text()').getall()
        # item['firm_representative'] = response.xpath('(//tr[1]/td/text())').getall()
        # return item
        # //h3/span/strong/text()//following::h3
        # firm_count = len(item['firm_title'])
        firm_count = len(ftitles)
        for i in range(firm_count):
            yield {
                'firm_title': response.xpath("//h3/span/strong/text()//following::h3").get(),
                'firm_representative': response.xpath("//tr[1]/td/text()//following::table//tr[1]/td/text()").get()
            }
# I was trying to get each firm infos seperated with others in json file

