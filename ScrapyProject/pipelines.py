# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import openpyxl

class ScrapyprojectPipeline:
    def  __init__(self):
        self.wb = openpyxl.Workbook()
        self.ws = self.wb.active

    def process_item(self, item, spider):
        line = [item['title'],item['publish'], item['score']]
        self.ws.append(line)
        return item

    def close_spider(self, spider):
        self.wb.save('book.xlsx')
        self.wb.close()
