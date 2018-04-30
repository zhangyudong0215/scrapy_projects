# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AllvisitItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    words = scrapy.Field()
    update_time = scrapy.Field()
    status = scrapy.Field()
    latest_chapter = scrapy.Field()
    main_page_url = scrapy.Field()
    catalog_url = scrapy.Field()
