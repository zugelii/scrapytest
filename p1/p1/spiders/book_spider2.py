# -*- coding: utf-8 -*-
import scrapy
from ..items import BookItem

class BooksSpider(scrapy.Spider):
    name = "books2"
    #allowed_domains = ["books.toscrape.com"]
    start_urls = [
        'http://books.toscrape.com/',
    ]

    def parse(self, response):
        for sel in response.xpath('//article[@class="product_pod"]'):
            book = BookItem()
            book['name'] = sel.xpath('./h3/a/@title').extract_first()
            #book['price'] = sel.xpath('./div/p[@class="price_color"]/text()').extract_first()
            book['price'] = sel.css('p.price_color::text').extract_first()
            #print(book['name'] +  "  " + book['price'])
            yield book

        #next_url = response.xpath('//li[@class="next"]/a/@href').extract_first()
        next_url = response.css('ul.pager li.next a:: attr(href)').extract_first()
        print(next_url)
        if next_url:
            next_url = response.urljoin(next_url)
            print("get nexurl" + next_url)
            #yield scrapy.Request(next_url, callback=self.parse)
        else:
            print("do not get next_url")