# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from xiaoshuo.Dao.mongodb import mongodb


class XiaoshuoPipeline(object):
    def process_item(self, item, spider):
        mongodb().biquge_insert(item)
        return item
