# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json

class YouyuanPipeline(object):
    def __init__(self):
        self.data_list = []
        self.filename = open('youyuan-bj.json','w')

    def process_item(self, item, spider):
        youyuan_json_data = json.dumps(dict(item),ensure_ascii=False) + ",\n"
        # self.data_list.append(youyuan_json_data.encode('utf-8'))
        self.filename.write(youyuan_json_data.encode('utf-8'))
        return item

    def close_spider(self,spider):
        # self.filename.write(self.data_list)
        self.filename.close()
