# -*- coding: utf-8 -*-
import csv
from urllib.parse import urlsplit
from seo_crawler.items import SeoCrawlerItem
import scrapy


class SeoSpider(scrapy.Spider):
    name = 'seo_spider'
    allowed_domains = ['example.com']
    start_urls = ['http://example.com/']


    def parse(self, response):
        item = SeoCrawlerItem()
        item['url'] = response.url
        item['slug'] = urlsplit(response.url).path
        item['directories'] = ', '.join([x for x in urlsplit(response.url).path.split('/')[1:]]),
        item['title'] = response.xpath('//title/text()').extract()
        item['h1'] = response.xpath('//h1//text()').extract()
        item['h2'] = response.xpath('//h2//text()').extract()
        item['h3'] = response.xpath('//h3//text()').extract()
        item['h4'] = response.xpath('//h4//text()').extract()
        item['description'] = response.xpath("//meta[@name='description']/@content")[0].extract()
        item['img_links'] = 0
        item['img_alt_tags'] = 0
        item['img_count'] = 0
#        item['link_urls'] = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "btTextLeft", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "bt_bb_wrapper", " " ))]//a/@href').extract() 
#        item['link_text'] = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "btTextLeft", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "bt_bb_wrapper", " " ))]//a/text()').extract()
#        item['link_count'] = len(item['link_urls'])        
        item['load_time'] = response.meta['download_latency']
        item['status_code'] = response.status 
        return item





