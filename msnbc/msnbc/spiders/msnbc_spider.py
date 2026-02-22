# it's a new day let's try running a separate python file on the json of the titles instead of doing it all in one spider...


from pathlib import Path

import sys
import os

import scrapy

print(f"{os.getcwd()}")
print(sys.path)



#from msnbc.additional_scripts import word_data
#import msnbc.msnbc.additional_scripts.word_data as word_data


class QuotesSpider(scrapy.Spider):
    name = "msnbc"

    async def start(self):
        
        urls = [
            "https://www.ms.now"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        links = response.css("a.rkv-card-headline-link::attr(href)").getall()
        
        #links = links[0:3] #to test it out
        
        
        for i in range(len(links)):
            link = links[i]
            full_link = link # i think so
            yield scrapy.Request(full_link, callback=self.parse_article)

    
    def parse_article(self, response):
        titles = response.css("h1.wp-block-post-title::text").getall()
        title = titles[0]
        
        if title == "MaddowBlog":
            title = titles[1]
        
        yield {
            "title": title
        }