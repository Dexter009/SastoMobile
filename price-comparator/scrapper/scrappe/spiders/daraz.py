# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrappe.items import scrappeItem

class DarazSpider(CrawlSpider):

	
	name = 'daraz'
	allowed_domains = ['www.daraz.com.np']
	start_urls = [
		'https://www.daraz.com.np/smartphones/'


	]
	handle_httpstatus_list = [403]

	rules = (
		Rule(LinkExtractor(allow=(), restrict_xpaths = ('//a[contains(@title, "Next")]',)),
			 callback="parse_item",
			 follow=True),)

	def parse_item(self, response):
		category = response.url.split('/')[-1]
		item_links = response.css('.products > div.sku.-gallery>a.link::attr(href)').extract()
		for a in item_links:
			yield scrapy.Request(a, callback=self.parse_detail_page)

	def parse_detail_page(self, response):
		title = response.css('h1::text').extract()[0].strip()
		description= response.xpath('//div["@features.-compact.-no-float "]/ul/li/text()').extract()[0:6]

		price = response.css('.price > span::text').extract()[1].strip()
		image = response.css('.product-preview > img::attr(data-src)').extract()[0]
		item = scrappeItem()
		item['title'] = title
		item['price'] = price
		item['url'] = response.url
		item['image']=image
		item['description']=description

		yield item
