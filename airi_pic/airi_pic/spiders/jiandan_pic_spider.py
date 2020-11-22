# -*- coding = utf-8 -*-
# @Time : 2020/11/22 16:40
# @Author : BigRong
# @File : jiandan_pic_spider.py
# @Software : PyCharm

import scrapy
from airi_pic.items import JiandanPicItem
import base64

Page = 0
class JiandanPicSpider(scrapy.Spider):
    name = 'jiandan_pic'
    start_urls = ['http://jandan.net/ooxx/page-1#comments']

    def parse(self, response):
        global Page
        sel = scrapy.Selector(response)

        image_urls = sel.xpath(
            '//ol[@class="commentlist"]//div[@class="row"]/div[@class="text"]//span[@class="img-hash"]/text()').extract()

        image_names = sel.xpath(
            '//ol[@class="commentlist"]//div[@class="row"]/div[@class="text"]//span[@class="righttext"]/a/text()').extract()

        new_urls= []
        for xxx in image_urls:
            url = base64.b64decode(xx).decode('utf-8')
            new_urls.append('https' + url)

        item = JiandanPicItem()
        item['image_url'] = new_urls
        item['image_name'] =image_names

        yield item

        while Page <2:
            next_page = response.xpath('//div[@class="cp-pagenavi"/a[@class="next-comment-page"]/@href')
            if next_page:
                url = response.urljoin(next_page[0].extract())
                yield scrapy.Request(url, self.parse)
            Page += 1
