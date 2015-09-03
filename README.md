# Sushibot :sushi:

Scrapy crawler to collect Sushi images using Flickr API.

## Requirements

* Python 2.7
* libxml2 and libxslt
* [Flickr API Key](https://www.flickr.com/services/api/misc.api_keys.html)

## Setup

```sh
$ pip install -r requirements.txt
```

## Run crawler

```sh
$ FLICKR_KEY=******* scrapy crawl sushi
```

Sushi images are saved into `images` dir, which will be created if not exists.
