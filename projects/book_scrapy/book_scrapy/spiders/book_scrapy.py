import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request
from book_scrapy.items import BookScrapyItem


class Myspider(scrapy.Spider):
    name = 'book_scrapy'
    url = 'http://www.23us.so/xiaoshuo/13694.html'

    def start_requests(self):
        yield Request(self.url, self.parse)
        # yield session.get(url) # 没有self.parse的API

    def parse(self, response):
        catalog_url = BeautifulSoup(response.text, 'lxml').find(
            'a', class_='read')['href']
        yield Request(catalog_url, self.get_chapter_url)

    def get_chapter_url(self, response):
        trs = BeautifulSoup(response.text, 'lxml').find_all('tr')
        for tr in trs:
            tds = tr.find_all('td')
            for td in tds:
                chapter_url = td.find('a')['href']
                yield Request(chapter_url, self.get_chapter_content)

    def get_chapter_content(self, response):
        chapter_title = BeautifulSoup(response.text,
                                      'lxml').find('dd').h1.get_text()
        chapter_content = BeautifulSoup(response.text, 'lxml').find(
            'dd', id='contents').get_text()

        item = BookScrapyItem()
        item['chapter_title'] = chapter_title
        item['chapter_content'] = chapter_content

        return item
