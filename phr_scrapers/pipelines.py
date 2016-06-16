# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

# from sqlalchemy.orm import sessionmaker
# from phr_scrapers.models import Homes, db_connect, create_homes_table
import logging
import scraperwiki

class MorphIOPipeline(object):
    def process_item(self, item, domain):
        try:
            scraperwiki.sql.save(unique_keys=['uid'], data=item)
        except:
            logging.warning('Failed to insert item: ' + item['uid'])
        return item