# -*- coding: utf-8 -*-
import scrapy


class DankmemesbotSpider(scrapy.Spider):
	name = 'dmemessimple'
	allowed_domains = ['www.reddit.com/r/dankmemes/']
	start_urls = ['http://www.reddit.com/r/dankmemes/']


	def parse(self, response):
		titles = response.css('.title.may-blank::text').extract()
		url = response.css('.title.may-blank::attr(href)').extract()
		print "TITLES AND URLS:"
		for t,v in zip(titles,url):
			print t
			print v

		print "DONE"
