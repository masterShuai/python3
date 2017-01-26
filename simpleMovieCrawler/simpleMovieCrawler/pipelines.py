# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import time


class SimplemoviecrawlerPipeline(object):

    def process_item(self, item, spider):
        now = time.strftime('%Y-%m-%d', time.localtime())
        #_basePath_ = './data/movie/'
        fileName = 'movie ' + now + '.txt'
        with open(fileName, 'a') as fp:
            fp.write(item['moiveName'][0].encode('utf-8').decode('utf-8') + '\n\n')
        return item
