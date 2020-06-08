# coding:utf-8
# Scrapy settings for example project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#
SPIDER_MODULES = ['example.spiders']
NEWSPIDER_MODULE = 'example.spiders'

USER_AGENT = 'scrapy-redis (+https://github.com/rolando/scrapy-redis)'
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# 允许中途暂停,Redis数据不丢失
SCHEDULER_PERSIST = True
# 默认的scrapy-redis请求集合
SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"
# 队列形式
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"
# 栈的形式
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack"
# scrapy-redis.pipeline.RedisPipeline支持将数据存储到Redis数据库中 必须
ITEM_PIPELINES = {
    'example.pipelines.ExamplePipeline': 300,
    'scrapy_redis.pipelines.RedisPipeline': 400,
}
# 指定数据库的IP
REDIS_HOST = "192.168.2.102"
REDIS_PORT = 6379

# 日志级别
LOG_LEVEL = 'DEBUG'

# Introduce an artifical delay to make use of parallelism. to speed up the
# crawl.
# 下载延时
DOWNLOAD_DELAY = 1
