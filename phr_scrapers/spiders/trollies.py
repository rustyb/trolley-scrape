# -*- coding: utf-8 -*-
import scrapy
from phr_scrapers.items import (TrolliesItem, TrollyLoader)

from hashlib import md5


class TrolliesSpider(scrapy.Spider):
    name = "trollies"
    allowed_domains = ["inmo.ie"]
    start_urls = (
        'https://www.inmo.ie/Trolley_Ward_Watch',
    )

    
    custom_settings = {
        'ITEM_PIPELINES' : {
           'phr_scrapers.pipelines.MorphIOPipeline': 300
        }
    }

    def parse(self, response):
        rows = response.xpath('//*[@id="TrolleyTable"]/tr')
        for row in rows:
            #md5 = hashlib.md5()
            #trolly = TrolliesItem()
            d = row.xpath('td[1]/text()').extract_first()
            hospital = row.xpath('td[2]/text()').extract_first()
            trolly_total = row.xpath('td[4]/text()').extract_first()
            l = TrollyLoader(item=TrolliesItem(), selector=row)
            l.add_xpath('date', 'td[1]/text()')
            l.add_xpath('hospital', 'td[2]/text()')
            l.add_xpath('region', 'td[3]/text()')
            l.add_xpath('trolly_total', 'td[4]/text()')
            l.add_xpath('ward_total', 'td[5]/text()')
            l.add_xpath('total', 'td[6]/text()')
            l.add_value('uid', md5(''.join(['trollies', d, hospital, trolly_total]).encode('utf8')).hexdigest())

            # trolly['date'] = row.xpath('td[1]/text()').extract_first()
            # trolly['hospital'] = row.xpath('td[2]/text()').extract_first()
            # trolly['region'] = row.xpath('td[3]/text()').extract_first()
            # trolly['trolly_total'] = row.xpath('td[4]/text()').extract_first()
            # trolly['ward_total'] =  row.xpath('td[5]/text()').extract_first()
            # trolly['total'] = row.xpath('td[6]/text()').extract_first()
            # trolly['uid'] = md5(''.join(['trollies', trolly['date'], trolly['hospital'], trolly['trolly_total']]).encode('utf8')).hexdigest()
            #print(trolly['date'],trolly['hospital'],trolly['region'],trolly['trolly_total'],trolly['ward_total'],trolly['total'] )
            yield l.load_item()
