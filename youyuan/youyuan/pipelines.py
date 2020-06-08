# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json

class YouyuanPipeline(object):
    def __init__(self):
        self.filename = open('youyuan.json','w')

    def process_item(self, item, spider):
        youyuan_json_data = json.dumps(dict(item),ensure_ascii=False) + ","
        self.filename.write(youyuan_json_data.encode('utf-8'))
        return item

    def close_spider(self,spider):
        self.filename.close()
