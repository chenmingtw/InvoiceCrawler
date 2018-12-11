# -*- coding: utf-8 -*-
import scrapy
from scrapy import Item, Field


class InvoiceSpider(scrapy.Spider):
    name = 'invoice'
    allowed_domains = ['invoice.etax.nat.gov.tw']
    start_urls = ['http://invoice.etax.nat.gov.tw/']

    def parse(self, response):
        for sel in response.css('div#number tr'):
            invoice_item = InvoiceItem()
            invoice_item['award'] = sel.css('td.title::text').extract_first()
            invoice_item['number'] = sel.css('span.t18Red::text').extract_first()
            yield invoice_item


class InvoiceItem(Item):
    award = Field()
    number = Field()