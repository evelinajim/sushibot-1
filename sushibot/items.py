# -*- coding: utf-8 -*-
from pprint import pformat

import scrapy


class SushibotItem(scrapy.Item):
    url = scrapy.Field()
    body = scrapy.Field()

    def __str__(self):
        return pformat({
            'url': self['url'],
            'body': self['body'][:10] + '...',
        })
