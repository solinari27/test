# -*- coding:utf-8 -*-
import scrapy

class BaiduStockSpider(scrapy.Spider):
    # spider need a name
    name = "baiduCrawler"
    # spider start url
    start_urls = [
        'https://gupiao.baidu.com/stock/',
    ]

    def parse(self, response):
        # # for <div class='quote'>
        # for quote in response.css('div.quote'):
        #     # for <span class='text'>取text
        #     # for <span><small>取text
        #     yield {
        #         'text': quote.css('span.text::text').extract_first(),
        #         'author': quote.xpath('span/small/text()').extract_first(),
        #     }
        #
        # next_page = response.css('li.next a::attr("href")').extract_first()
        # if next_page is not None:
        #     yield response.follow(next_page, self.parse)
        print response
