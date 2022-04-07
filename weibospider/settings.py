# -*- coding: utf-8 -*-

BOT_NAME = 'spider'

SPIDER_MODULES = ['spiders']
NEWSPIDER_MODULE = 'spiders'

ROBOTSTXT_OBEY = False

# change cookie to yours
DEFAULT_REQUEST_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:61.0) Gecko/20100101 Firefox/61.0',
    'Cookie': '_T_WM=ce733841f08e623d1af1718adc1c28bf; SCF=AmN2g1ePZ4eWY6NCnznzJSDXD57yYDm5_jm5WVdWcxWPQ0-eHsKigmMi6ujUtbRjFC4cR5KHOQcwRrzLzXdcTCk.; SUB=_2A25PSwbKDeRhGeBL6FUQ9SfEyzSIHXVst6qCrDV6PUJbktAfLUjSkW1NRw9dpTQ9L3zlEw5oowOT2qzdAVuMTemR; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWn3jOJ4DD-qauufEsRGj235NHD95QcSKeNeK-41h5RWs4Dqc_oi--fi-z4i-z0i--fiKnNi-2pi--NiKLWiKnXi--fi-zRi-2ci--NiKL2iKn7i--NiKLWi-88i--fiKy2i-2pi--Xi-zRiK.Ri--NiKLWiKnXi--fi-z7iKysi--ciK.4i-iW; SSOLoginState=1649374874'}

CONCURRENT_REQUESTS = 16

DOWNLOAD_DELAY = 3

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.cookies.CookiesMiddleware': None,
    'scrapy.downloadermiddlewares.redirect.RedirectMiddleware': None,
    'middlewares.IPProxyMiddleware': 100,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 101,
}

ITEM_PIPELINES = {
    'pipelines.MongoDBPipeline': 300,
}

MONGO_HOST = '127.0.0.1'
MONGO_PORT = 27017
