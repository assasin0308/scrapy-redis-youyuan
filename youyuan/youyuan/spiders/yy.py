# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
# from scrapy.spiders import CrawlSpider, Rule
from scrapy.spiders import Rule
from scrapy_redis.spiders import RedisCrawlSpider
from youyuan.items import YouyuanItem

# class YySpider(CrawlSpider):
class Yyspider(RedisCrawlSpider):
    name = 'yy'
    # allowed_domains = ['youyuan.com']
    # start_urls = [
    #     'http://www.youyuan.com/find/beijing/mm0-0/advance-0-0-0-0-0-0-0/p1/'
    # ]
    redis_key = 'yyspider:start_urls'
    # 动态域的获取
    def __init__(self,*args,**kwargs):
        domain = kwargs.pop('domain','')
        self.allowed_domain = filter(None,domain.split(','))
        super(Yyspider,self).__init__(*args,**kwargs)

    # 匹配规则
    # 第一级,北京市女性每一页链接匹配规则
    page_links = LinkExtractor(allow=(r"youyuan.com/find/beijing/mm0-0/advance-0-0-0-0-0-0-0/p\d+/"))
    # 第二级,每页女性个人主页的匹配规则
    profile_links = LinkExtractor(allow=(r"youyuan.com/\d+-profile/"))

    rules = (
        Rule(page_links),
        Rule(profile_links,callback= "parse_item"),
    )

    def parse_item(self, response):
        item = YouyuanItem()

        # 用户名
        item['username'] = self.get_username(response)
        # 年龄
        item['age'] = self.get_age(response)
        # 头像
        item['header_url'] = self.get_header_url(response)
        # 相册
        item['images_url'] = self.get_images_url(response)
        # 内心独白
        item['content'] = self.get_content(response)
        # 籍贯
        item['place'] = self.get_place(response)
        # 学历
        item['education'] = self.get_education(response)
        # 兴趣爱好
        item['hobby'] = self.get_hobby(response)
        # 个人主页
        item['source_url'] = response.url
        # 数据来源网站
        item['source'] = "youyuan"

        yield item







    def get_username(self,response):
        username = response.xpath('//dl[@class="personal_cen"]//div[@class="main"]/strong/text()').extract()
        if len(username):
            username = username[0]
        else:
            username = ""

        return username.strip()

    def get_age(self,response):
        age = response.xpath('//dl[@class="personal_cen"]//dd/p/text()').extract()

        if len(age):
            age = age[0].split(" ")[2]
        else:
            age = 'NULL'

        return age

    def get_header_url(self,response):
        header_url = response.xpath('//dl[@class="personal_cen"]/dt/img/@src').extract()
        if len(header_url):
            header_url = header_url[0]
        else:
            header_url = ""

        return header_url.strip()

    def get_images_url(self,response):
        images_url = response.xpath('//div[@class="ph_show"]/ul/li/a/img/@src').extract()
        if len(images_url):
            images_url = images_url
        else:
            images_url = "NULL"

        return images_url

    def get_content(self,response):
        content = response.xpath('//div[@class="pre_data"]/ul/li/p/text()').extract()
        if len(content):
            content = content[0]
        else:
            content = 'NULL'

        return content.strip()

    def get_place(self,response):
        place = response.xpath('//div[@class="pre_data"]/ul/li[2]//ol[1]/li[1]/span/text()').extract()
        if len(place):
            place = place[0]
        else:
            place = 'NULL'
        return place.strip()

    def get_education(self,response):
        education = response.xpath('//div[@class="pre_data"]/ul/li[3]//ol[2]/li[2]/span/text()').extract()
        if len(education):
            education = education[0]
        else:
            education = 'NULL'

        return education.strip()

    def get_hobby(self,response):
        hobby = response.xpath('//dl[@class="personal_cen"]//ol/li/text()').extract()
        if len(hobby):
            hobby = ",".join(hobby).replace(" ","")
        else:
            hobby = 'NULL'

        return hobby






