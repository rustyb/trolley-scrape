# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, Join, TakeFirst

import datetime, json
import time

from datetime import date

def clean_spaces(value):
    return _clean_spaces_re.sub(' ', value)

def strip(value):
    return value.strip()


def get_date_item1(date_str, format):
        date_obj = datetime.datetime.strptime(date_str, format).date().isoformat()
        return date_obj

def get_json(value):
    return json.dumps(value)


class TrolliesItem(scrapy.Item):
    uid = scrapy.Field()
    date = scrapy.Field(input_processor=MapCompose(lambda s: get_date_item1(s, '%d/%m/%Y')))
    hospital = scrapy.Field()
    region = scrapy.Field()
    trolly_total = scrapy.Field()
    ward_total = scrapy.Field()
    total = scrapy.Field()

class TrollyLoader(ItemLoader):
    default_output_processor = TakeFirst()


