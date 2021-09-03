# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class TopicItem(Item):
    """Topic page item"""
    repo = Field()


class RepoItem(Item):
    """Repository item"""
    repo = Field()
    searched_file = Field()
