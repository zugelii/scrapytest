import scrapy

class BookSpider(scrapy.Spider):
    name = "books3"
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        for book in response.css('article.product_pod'):
            name = book.xpath('./h3/a/@title').extract_first()
            price = book.css('p.price_color::text').extract_first()

            yield {
                'name':name,
                'price':price
            }

        for url in response.xpath('//ul[@class="pager"]/li[@class="next"]'):
            u = url.xpath('./a/@href').extract_first()
            yield scrapy.Request(response.urljoin(u), callback=self.parse)