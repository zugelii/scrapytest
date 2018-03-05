#-*- coding: utf-8 -*-


import scrapy
from douban.items import BookItem


class BookSpider(scrapy.Spider):
	name = 'books'
	#allowed_domains = ["books.douban.com"]
	start_urls = [
		'http://book.douban.com/',
	]
	def parse(self, response):
		print(response.body)
		for book_url in response.xpath('//ul[@class="list-col list-col5 list-express slide-item"'):
			book = BookItem()
			book['name'] = book_url.xpath('./li/div[@class="infor"]/div[@class="title"]/a/text()').extract_first()
			book['author'] = book_url.xpath('./li/div[@class="info"/div[@class="more-meta"]/h4/text()').extract_first()
			print(book['name'] + book['author'])
			yield book

