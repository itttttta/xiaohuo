# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XiaoshuoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    _id = scrapy.Field()
    #标题
    title = scrapy.Field()
    #简介
    description = scrapy.Field()
    #类型
    type = scrapy.Field()
    #分类
    catalogue = scrapy.Field()
    #地址
    book_url = scrapy.Field()
    #作者
    author = scrapy.Field()
    #书名
    book_name = scrapy.Field()
    #目录 默认正序
    chapters = scrapy.Field()
    #数据库更新时间
    update_time = scrapy.Field()
    #书更新时间
    book_update_time = scrapy.Field()
    # 最新章节
    latest_chapter = scrapy.Field()
    #是否完结 yes 完结 no 未完结
    is_complecated = scrapy.Field()
    #封面
    img = scrapy.Field()
    #阅读量
    read_count = scrapy.Field()
    #留存量
    save_count = scrapy.Field()
    #点赞量
    up_count = scrapy.Field()
    #评论数
    comment_count = scrapy.Field()
    pass
