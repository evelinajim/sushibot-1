# -*- coding: utf-8 -*-
import os

import scrapy

from sushibot.items import SushibotItem


class SushiSpider(scrapy.Spider):
    name = "sushi"
    allowed_domains = ["api.flickr.com", "staticflickr.com"]
    start_urls = (
        'https://api.flickr.com/services/rest/?method=flickr.photos.search&api_key=' +
        os.environ['FLICKR_KEY'] + '&text=sushi&sort=relevance',
    )

    def parse(self, response):
        for photo in response.css('photo'):
            yield scrapy.Request(photo_url(photo), self.handle_image)

    def handle_image(self, response):
        return SushibotItem(url=response.url, body=response.body)


def photo_url(photo):
    return 'https://farm{farm}.staticflickr.com/{server}/{id}_{secret}_{size}.jpg'.format(
        farm=photo.xpath('@farm').extract_first(),
        server=photo.xpath('@server').extract_first(),
        id=photo.xpath('@id').extract_first(),
        secret=photo.xpath('@secret').extract_first(),
        size='b',
    )
