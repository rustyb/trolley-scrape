#!/usr/bin/env python

import os
# morph.io requires this db filename, but scraperwiki doesn't nicely
# expose a way to alter this. So we'll fiddle our environment ourselves
# before our pipeline modules load.
os.environ['SCRAPERWIKI_DATABASE_NAME'] = 'sqlite:///data.sqlite'

# from twisted.internet import reactor
# from scrapy.crawler import Crawler
# # from scrapy import log, signals
# from phr_scrapers.spiders.trollies import TrolliesSpider
# from scrapy.utils.project import get_project_settings

# spider = TrolliesSpider()
# settings = get_project_settings()
# crawler = Crawler(settings)
# # crawler.signals.connect(reactor.stop, signal=signals.spider_closed)
# crawler.configure()
# crawler.crawl(spider)
# crawler.start()
# # log.start()
# reactor.run()

import subprocess


subprocess.call('scrapy crawl trollies --loglevel=INFO', shell=True)