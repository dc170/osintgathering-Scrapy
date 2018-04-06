# -*- coding: utf-8 -*-

BOT_NAME = 'tormonitor'

SPIDER_MODULES = ['tormonitor.spiders']
NEWSPIDER_MODULE = 'tormonitor.spiders'

HTTP_PROXY = 'http://127.0.0.1:8123'
DOWNLOADER_MIDDLEWARES = {
  #Tor Middleware
  'tormonitor.middlewares.ProxyMiddleware': 400
}
