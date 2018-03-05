# -*- coding: utf-8 -*-
import scrapy
import re

class Book2Spider(scrapy.Spider):
    name = 'book2'
    #allowed_domains = ['www.douban.com/doulist/1264675']
    start_urls = ['http://www.douban.com/doulist/1264675/']

    def parse(self, response):
        #print(response.body)
        books = response.xpath('//div[@class="bd doulist-subject"]')
        for each in books:
        	title = each.xpath('div[@class="title"]/a/text()').extract_first()
        	rate  = each.xpath('div[@class="rating"]/span[@class="rating_nums"]/text()').extract_first()
        	author= re.search('<div class="abstract">(.*?)<br', each.extract(), re.S).group(1)
        	title = title.replace(' ', '').replace('\n', '')
        	author = author.replace(' ', '').replace('\n', '')
        	print("title:" + title)
        	print("rate:" + rate)
        	print(author)
