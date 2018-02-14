# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from sastobazaar.models import DarazItem, NepBayItem, SdealItem
from scrapper.scrappe.items import scrappeItem
from scrapper.scrappe.spiders import daraz


class ScrappePipeline(object):
    def process_item(self, item, spider):
        if spider.name == 'daraz':
            try:
                darazz = DarazItem.objects.get(title=item["title"])
                print ("Item already exists")
                return item
            except DarazItem.DoesNotExist:
                pass


            darazz = DarazItem()
            darazz.title = item["title"]
            darazz.image = item["image"]
            darazz.url = item["url"]
            darazz.price = item["price"]
            darazz.description = item["description"]
            darazz.save()
            return darazz


# class ScrappeNPipeline(object):
#      def process_item(self, item, spider):
        elif spider.name == 'nepbay':
            try:
                nepbay = NepBayItem.objects.get(title=item["title"])
                print ("Item already exists")
                return item
            except NepBayItem.DoesNotExist:
                pass

            nepbay = NepBayItem()
            nepbay.title = item["title"]
            nepbay.image = item["image"]
            nepbay.url = item["url"]
            nepbay.price = item["price"]
            nepbay.description = item["description"]
            nepbay.save()
            return nepbay


        else:
            try:
                sdeal = SdealItem.objects.get(title=item["title"])
                print ("Item already exists")
                return item
            except SdealItem.DoesNotExist:
                pass

            sdeal = SdealItem()
            sdeal.title = item["title"]
            sdeal.image = item["image"]
            sdeal.url = item["url"]
            sdeal.price = item["price"]
            sdeal.description = item["description"]
            sdeal.save()
            return sdeal
