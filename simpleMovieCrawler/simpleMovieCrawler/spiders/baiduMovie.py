# -*- coding: utf-8 -*-
import scrapy

from simpleMovieCrawler.items import SimplemoviecrawlerItem

class BaidumovieSpider(scrapy.Spider):
    name = "baiduMovie"
    allowed_domains = ["dianying.nuomi.com"]
    start_urls = ['https://dianying.nuomi.com']

    def parse(self, response):
        #pass
        # 选择正在热映的电影信息列表
        liSelector = response.xpath('//html/body//div[@id="flexslider1"]/ul/li')
        items = []
        for eachLi in liSelector:
            item = SimplemoviecrawlerItem()
            item['moiveName'] = eachLi.xpath('p')[0].xpath('text()').extract()
            items.append(item)
        return items
