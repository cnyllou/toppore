# Scrapy settings for toppore project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

from os.path import dirname

import sys
import os

path = dirname(dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.append(path)

BOT_NAME = 'toppore'

SPIDER_MODULES = ['toppore.spiders']
NEWSPIDER_MODULE = 'toppore.spiders'

DOWNLOADER_MIDDLEWARES = {
    'misc.middleware.CustomUserAgentMiddleware': 401,
}

ITEM_PIPELINES = {
    'toppore.pipelines.JSONLinesPipeline': 300,
}

LOG_LEVEL = 'INFO'

# DOWNLOAD_DELAY = 1  # Needs to be set only for the Repo Spider
