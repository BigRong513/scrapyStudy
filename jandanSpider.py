# -*- coding = utf-8 -*-
# @Time : 2020/11/24 18:31
# @Author : BigRong
# @File : jandanSpider.py
# @Software : PyCharm
import urllib

import requests

from lxml import etree



def main():
    #url
    url = 'http://jandan.net/ooxx'
    kv = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"}

    i = 0;
    j = 0;
    while i < 20:
        html = ''
        r = requests.get(url, headers=kv)
        html = r.text
        # print(html)
        i += 1
        e = etree.HTML(html)
        image_urls = e.xpath(
            '//ol[@class="commentlist"]//div[@class="row"]//div[@class="text"]//img/@src')

        image_names = e.xpath(
            '//ol[@class="commentlist"]//div[@class="row"]//div[@class="text"]//span[@class="righttext"]/a/text()')


        for url in image_urls:
            urllib.request.urlretrieve("http:" + url,
                                       ".\pic\jiandan\{}.jpg".format(j))
            j += 1
        url = "http:" + e.xpath(
            '//div[@class="comments"]//div[@class="cp-pagenavi"]//a[@class="previous-comment-page"]/@href')[0]
        print(image_urls)
        print(image_names)
        print(url)

if __name__ == "__main__":
    main()

