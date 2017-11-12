# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class SeoCrawlerItem(scrapy.Item):

    url = Field()
    slug = Field()
    directories = Field()
    title = Field()
    h1 = Field()
    h2 = Field()
    h3 = Field()
    h4 = Field()
    description = Field()
    img_count = Field()
    img_links = Field()
    img_alt_tags = Field()
    link_count = Field()
    link_urls = Field()
    link_text = Field()
    load_time = Field()
    status_code = Field()
    
