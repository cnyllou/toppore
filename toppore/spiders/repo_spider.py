#!/usr/bin/env python3

from scrapy import Spider
from toppore.items import RepoItem
from toppore.utils import (
    load_repo_list, extract_a_tag_value
)
from toppore.constants import (ALLOWED_DOMAINS, REPO_SPIDER_NAME)


class RepoSpider(Spider):
    """Spider which crawls each repository

    scrapy.downloadermiddlewares.retry - needs to adapt to 429 rate limiting
    error."""
    name = REPO_SPIDER_NAME
    allowed_domains = ALLOWED_DOMAINS
    start_urls = load_repo_list()  # [:3]

    # In order to bypass github second rate limiting
    download_delay = 5

    def add_item(self, repo, searched_file, item_class):
        item = item_class()
        item['repo'] = repo
        item['searched_file'] = searched_file
        return item

    def parse(self, response):
        """Yield repository URLs and package.json paths"""
        packages = response.xpath(
            '//*[@id="code_search_results"]/div[1]//div/a[contains(text(),' +
            '"package.json")]').getall()

        if bool(packages):
            repo = response.url
            searched_file = ", ".join([extract_a_tag_value(_)
                                       for _ in packages])

            return self.add_item(repo, searched_file, RepoItem)
