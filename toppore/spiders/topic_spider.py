#!/usr/bin/env python3

from toppore.constants import (
    GITHUB_TOPIC_QUERY, ALLOWED_DOMAINS, TOPIC_SPIDER_NAME
)
from toppore.utils import calculate_page_count
from toppore.items import TopicItem

from scrapy import Spider
# from misc.log import *

import re

repo_count_regex = r'(\d+) public'
public_repo_count_xpath = \
    '//*[@id="js-pjax-container"]/div[2]/div[2]/div/div[1]/h2'


class TopicSpider(Spider):
    """Spider for crawling GitHub topics"""
    name = TOPIC_SPIDER_NAME
    allowed_domains = ALLOWED_DOMAINS
    start_urls = [GITHUB_TOPIC_QUERY]

    current_page = 1  # To keep track of the pages
    items = list()    # For storing results

    def add_item(self, repo, item_class):
        item = item_class()
        item['repo'] = repo
        return item

    def parse(self, response):
        next_page_num = self.current_page + 1
        page_count_element = response.xpath(public_repo_count_xpath
                                            ).get().strip('\n')

        match = re.search(repo_count_regex, page_count_element)
        page_count = calculate_page_count(int(match.group(1)))

        for repo in response.xpath('//article/div//h3'):
            repo = repo.xpath('a[contains(@class, "text-bold")]/@href').get()
            self.items.append(self.add_item(repo, TopicItem))

        if next_page_num <= page_count:
            next_page = GITHUB_TOPIC_QUERY + str(next_page_num)

            if next_page is not None:
                self.current_page += 1
                return response.follow(next_page, self.parse)

        return self.items
