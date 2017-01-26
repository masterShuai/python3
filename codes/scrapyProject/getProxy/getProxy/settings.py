# -*- coding: utf-8 -*-

# Scrapy settings for getProxy project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'getProxy'

SPIDER_MODULES = ['getProxy.spiders']
NEWSPIDER_MODULE = 'getProxy.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'getProxy (+http://www.yourdomain.com)'


### user add
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'
ITEM_PIPELINES = {
'getProxy.pipelines.GetproxyPipeline':100
}
