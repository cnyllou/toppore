from os.path import (
    dirname, join
)

SCRIPT_DIR = dirname(__file__)
OUTPUT_DIR = join(SCRIPT_DIR, 'output')
REPO_OUTPUT = join(OUTPUT_DIR, 'repo_output.jl')
TOPIC_OUTPUT = join(OUTPUT_DIR, 'topic_output.jl')

TOPIC_SPIDER_NAME = 'topic_spider'
REPO_SPIDER_NAME = 'repo_spider'

GITHUB_BASE = 'https://github.com'
TOPICS_ENDPOINT = 'topics'
SEARCH_ENDPOINT = 'search'

GITHUB_HOST = 'github.com'
ALLOWED_DOMAINS = ['github.com']

TOPIC = 'i18n'
LANGUAGE = 'vue'
SEARCH_KEYWORD = 'vue-i18n'
FILE_SEARCH_KEYWORD = 'package.json'

NEXT_PAGE_QUERY = f"?l={LANGUAGE}&page="  # Page number
REPO_SEARCH_QUERY = f"{SEARCH_ENDPOINT}?q={SEARCH_KEYWORD}"

GITHUB_TOPIC_QUERY = f"{GITHUB_BASE}/{TOPICS_ENDPOINT}/{TOPIC}/" \
                     f"{NEXT_PAGE_QUERY}"

MAX_REPO_PER_PAGE = 30
