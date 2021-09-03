from math import ceil
from toppore.constants import (
    MAX_REPO_PER_PAGE, REPO_SEARCH_QUERY, GITHUB_BASE, FILE_SEARCH_KEYWORD,
    TOPIC_OUTPUT, REPO_OUTPUT, REPO_SPIDER_NAME
)

import json
import re


def get_spider_name(spider):
    """Get output filename based on spider.name"""
    return REPO_OUTPUT if spider.name == REPO_SPIDER_NAME else TOPIC_OUTPUT


def load_repo_list() -> list:
    """Load the results from the topic search spider"""
    repo_list = prepend_host(load_jl())
    return create_search_list(repo_list)


def load_jl(filename: str = TOPIC_OUTPUT) -> list:
    """Load the contents of a JSON lines file"""
    with open(filename, 'r') as f:
        content = f.read().replace('\n', ',')[:-1]
        return [v
                for el in json.loads(f"[{content}]")
                for k, v in el.items()]


def prepend_host(repo_list):
    """Add a search query to all repositories in a list"""
    return [GITHUB_BASE + _ for _ in repo_list]


def create_search_list(repo_list):
    """Add a search query to all repositories in a list"""
    return [f"{_}/{REPO_SEARCH_QUERY}" for _ in repo_list]


def calculate_page_count(count):
    """Return the count of pages to crawl"""
    return ceil(count / MAX_REPO_PER_PAGE)


def extract_a_tag_value(text):
    """Extract the value of the a tag"""
    return re.search('<a.*>(.*)</a>', text).group(1)


def search_package_in_list(list_):
    """Search if strings in a list_ contain package.json"""
    return [_ for _ in list_ if FILE_SEARCH_KEYWORD in _]
