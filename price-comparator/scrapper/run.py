from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess

from scrappe.spiders import daraz,nepbay

Spider1 = daraz.DarazSpider()
Spider2 = nepbay.NepbaySpider()
process = CrawlerProcess(get_project_settings())
process.crawl(Spider1)
process.crawl(Spider2)
process.start()