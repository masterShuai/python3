# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import time
import urllib


class WeatherPipeline(object):
    def process_item(self, item, spider):
        today = time.strftime('%Y%m%d', time.localtime())
        fileName = today + '.txt'
        imgPath = os.getcwd() + '/images'
        if os.path.isdir(imgPath) == False:
            os.mkdir(imgPath)
        with open(fileName, 'a', encoding='utf-8') as fp:
            fp.write(item['cityDate'] + '\t')
            fp.write(item['week'] + '\t')
            imgName = 'images/' + os.path.basename(item['img'])
            fp.write(imgName + '\t')
            #判断图片是否重复
            if os.path.exists(imgName):
                pass
            else:
                with open(imgName, 'wb') as ifp:
                    response = urllib.request.urlopen(item['img'])
                    ifp.write(response.read())
            fp.write(item['temperature'].encode('utf-8').decode('utf-8') + '\t')
            fp.write(item['weather'] + '\t')
            fp.write(item['wind'] + '\n\n')
            time.sleep(1)  # 避免因写入太快丢失数据
        return item
