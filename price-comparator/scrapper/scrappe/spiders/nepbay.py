# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrappe.items import scrappeItem


class NepbaySpider(CrawlSpider):
	name = 'nepbay'
	allowed_domains = ['nepbay.com']
	start_urls = ['http://nepbay.com/shopping/nepal/smart-phones-mobiles-in-nepal/']

	rules = (
		Rule(LinkExtractor(allow=(), restrict_xpaths = ('//div[@class="pager_right tag_cloud"]/ul/li/a',)),
			 callback="parse_item",
			 follow=True),)

	def parse_item(self, response):

		print('processing....'+response.url)
		items_link = response.css('a.link::attr(href)').extract()
		for a in items_link:
			yield scrapy.Request(a, callback=self.parse_detail_page)

	def parse_detail_page(self, response):
		title = response.css('div.detail-page-title.hidden-lg.hidden-md::text').extract()[0]
		description= response.css('div.detail-info-body > div > div > div::text').extract()[2:14]

		price = response.css('div.detail-price > span.product-price > b::text').extract()[0]
		image = response.css('img#zoom_01::attr(src)').extract()[0]
		item = scrappeItem()
		item['title'] = title
		item['price'] = price
		item['url'] = response.url
		item['image']=image
		item['description']=description

		yield item