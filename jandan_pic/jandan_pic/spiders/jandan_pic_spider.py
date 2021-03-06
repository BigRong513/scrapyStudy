# -*- coding = utf-8 -*-

import scrapy
from jandan_pic.items import JandanPicItem

Page = 0
class JandanPicSpider(scrapy.Spider):
    name = 'jandan_pic'
    start_urls = ['http://jandan.net/ooxx/']

    def parse(self, response):
        global Page
        sel = scrapy.Selector(response)

        image_urls = sel.xpath(
            '//ol[@class="commentlist"]//div[@class="row"]//div[@class="text"]//img/@src').extract()

        image_names = sel.xpath(
            '//ol[@class="commentlist"]//div[@class="row"]//div[@class="text"]//span[@class="righttext"]/a/text()').extract()


        new_urls= []
        for xxx in image_urls:
            # url = base64.b64decode(xxx).decode('utf-8')
            # new_urls.append('https' + url)
            # print("Debug #############################")
            # print(xxx)
            new_urls.append('https:' + xxx)

        item = JandanPicItem()
        item['image_url'] = new_urls
        item['image_name'] =image_names

        yield item

        if Page <3:
            # print("Before Debug!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            next_page = response.xpath('//div[@class="comments"]//div[@class="cp-pagenavi"]//a[@class="previous-comment-page"]/@href')
            # print("Debug!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            if next_page:
                # print("next_page is %s"%next_page)
                url = response.urljoin(next_page[1].extract())
                print("Debug%s"%url)
                yield scrapy.Request(url, self.parse)
            Page += 1

