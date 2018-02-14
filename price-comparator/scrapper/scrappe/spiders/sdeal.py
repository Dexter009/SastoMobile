# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrappe.items import scrappeItem




class SdealSpider(CrawlSpider):
    name = 'sdeal'
    allowed_domains = ['www.sastodeal.com']
    start_urls = ['https://www.sastodeal.com/sastodeal/cta-mobiles-28']



    def parse(self, response):
        #print(response.meta)
        item_links=response.css('div.prod-detail > a.fullWidth::attr(href)').extract()
        for item_link in item_links:
            a='https://www.sastodeal.com'+item_link
            yield scrapy.Request(a,callback=self.parse_detail_page)


    def parse_detail_page(self,response):
        title = response.css('div.detailLeft > h1.name > p::text').extract()
        description = response.xpath('//div["@prodSpecification"]/ul/li/text()').extract()[0:6]

        price = response.css('ul.row mrp-outer > li.mrp mrpPrice::text').extract()
        image = response.css('div.productBigImage > a > img::attr(src)').extract()
        item = scrappeItem()
        item['title'] = title
        item['price'] = price
        item['url'] = response.url
        item['image'] = image
        item['description'] = description

        yield item


