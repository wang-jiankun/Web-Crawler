# -*- coding: utf-8 -*-
import scrapy


# class DemoSpider(scrapy.Spider):
#     """
#     普通版
#     """
#     name = 'demo'
#     # allowed_domains = ['python123.io']
#     start_urls = ['http://python123.io/ws/demo.html']
#
#     def parse(self, response):
#         file_name = response.url.split('/')[-1]
#         with open(file_name, 'wb') as f:
#             f.write(response.body)
#         self.log('Saved file %s.' % file_name)


class DemoSpider(scrapy.Spider):
    """
    yield 版
    """
    name = 'demo'

    def start_requests(self):
        urls = ['http://python123.io/ws/demo.html']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        file_name = response.url.split('/')[-1]
        with open(file_name, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s.' % file_name)