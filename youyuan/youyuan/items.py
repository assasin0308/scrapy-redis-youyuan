# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Field,Item


class YouyuanItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 用户名
    username = Field()
    # 年龄
    age = Field()
    # 头像
    header_url = Field()
    # 相册
    images_url = Field()
    # 内心独白
    content = Field()
    # 籍贯
    place = Field()
    # 学历
    education = Field()
    # 兴趣爱好
    hobby = Field()
    # 个人主页
    source_url = Field()
    # 数据来源网站
    source = Field()
