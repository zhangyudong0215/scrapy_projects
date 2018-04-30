import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request
from allvisit.items import AllvisitItem


class Myspider(scrapy.Spider):
    name = 'allvisit'
    url_head = 'http://www.23us.so/top/allvisit_'
    url_tail = '.html'

    def start_requests(self):
        url = self.url_head + '1' + self.url_tail
        yield Request(url, self.parse)

    def parse(self, response):
        max_page_index = BeautifulSoup(response.text, 'lxml').find(
            'a', class_='last').get_text()
        for index in range(1, int(max_page_index)+1):
            url = self.url_head + str(index) + self.url_tail
            yield Request(url, self.get_info)

    def get_info(self, response):
        trs = BeautifulSoup(response.text, 'lxml').find_all(
            'tr', bgcolor='#FFFFFF')
        for tr in trs:
            yield self.getBook(tr)

    def getBook(self, tr):
        tds = tr.find_all('td')
        title = tds[0].a.get_text()
        main_page_url = tds[0].a['href']
        catalog_url = tds[1].a['href']
        latest_chapter = tds[1].a.get_text()
        author = tds[2].get_text()
        words = tds[3].get_text()
        update_time = tds[4].get_text()
        status = tds[5].get_text()

        item = AllvisitItem()
        item['title'] = title
        item['author'] = author
        item['words'] = words
        item['update_time'] = update_time
        item['status'] = status
        item['latest_chapter'] = latest_chapter
        item['main_page_url'] = main_page_url
        item['catalog_url'] = catalog_url

        return item
