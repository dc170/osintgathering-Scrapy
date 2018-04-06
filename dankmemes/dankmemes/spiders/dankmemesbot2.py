# -*- coding: utf-8 -*-
import scrapy
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import FormRequest

import wget

class DankmemesbotSpider(scrapy.Spider):
	name = 'dankmemesbot2'
	start_urls = ['http://www.reddit.com/r/dankmemes//']


	def parse(self, response):
		titles = response.css('.title.may-blank::text').extract()
		votes = response.css('.score.unvoted::text').extract()
		times = response.css('time::attr(title)').extract()
		url = response.css('.title.may-blank::attr(href)').extract()
		print "URLS........"
		for u in url:
			posturl = "https://reddit.com/"+u
			print posturl
			yield scrapy.Request(url=posturl, callback=self.scan_post)
			
	def scan_post(self,response):
		
		img = response.css('img.preview::attr(src)').extract()[0]
		print img
		filename = wget.download(img, out="/home/sandbox/memes/")
	

