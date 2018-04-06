# -*- coding: utf-8 -*-
import scrapy


class DankmemesbotSpider(scrapy.Spider):
	name = 'dankmemesbot'
	allowed_domains = ['www.reddit.com/r/dankmemes/']
	start_urls = ['http://www.reddit.com/r/dankmemes//']


	def parse(self, response):
		titles = response.css('.title.may-blank::text').extract()
		votes = response.css('.score.unvoted::text').extract()
		times = response.css('time::attr(title)').extract()
		url = response.css('.title.may-blank::attr(href)').extract()
		print "URLS........"
		for u in url:
			print u
		for item in zip(titles,votes,times,url):
			scraped_info = {
				'title' : item[0],
				'vote' : item[1],
				'created_at' : item[2],
				'urls' : item[3],
			}

			yield scraped_info
