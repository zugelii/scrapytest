# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class P1Pipeline(object):
	exchange_rate = 8.5308
    def process_item(self, item, spider):
    	#提取item的price字段
    	#去掉前面英镑符号￡，转换成float类型，乘以汇率
    	price = float(item['price'][1:]) * self.exchange_rate
    	#保留两位小数，赋值回item的price字段
    	item['price'] = '￥%.2f' % price
        return item
