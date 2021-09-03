# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from collections import OrderedDict
from toppore.utils import get_spider_name

import json
import codecs


class JSONLinesPipeline:
    """Pipeline to JSON lines file."""

    def open_spider(self, spider):
        filename = get_spider_name(spider)
        self.file = codecs.open(filename, 'w', encoding='utf-8')

    def process_item(self, item, spider):
        for el in item:
            line = json.dumps(
                OrderedDict(item), ensure_ascii=False, sort_keys=True
            ) + "\n"
            self.file.write(line)

        return item

    def close_spider(self, spider):
        self.file.close()
