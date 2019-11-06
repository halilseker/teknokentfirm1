# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

# It collects all firm infos from sakaryateknokent.com with successfully
class Sautekfirm3Spider(CrawlSpider):
    name = 'sautekfirm3'
    allowed_domains = ['sakaryateknokent.com']
    start_urls = ['http://sakaryateknokent.com/']

    rules = (
        Rule(LinkExtractor(deny=('/cv-ekle', '/staj-basvurusu'),
                           restrict_xpaths="//div[@class='mpc-callout__button']/a"),
             callback='parse_item',
             follow=True),
    )

    def parse_item(self, response):
        ftitles = response.xpath("//h3/span/strong/text()").getall()
        frepresentatives = response.xpath("(//tr[1]/td/text())").getall()
        fphonenumber = response.xpath("//tr[2]/td/text()").getall()
        femail = response.xpath("//tr[3]/td/text()").getall()
        faddress = response.xpath("//tr[4]/td/text()").getall()
        fservices = response.xpath("//tr[5]/td/text()").getall()

        firm_count = len(ftitles)
        for i in range(firm_count):
            yield {
                'firm_title': ftitles[i],
                'firm_representative': frepresentatives[i],
                'firm_phone_number': fphonenumber[i],
                'firm_email': femail[i],
                'firm_address': faddress[i],
                'firm_services': fservices[i]
            }