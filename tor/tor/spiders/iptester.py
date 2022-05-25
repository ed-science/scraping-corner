import logging
import scrapy
from bs4 import BeautifulSoup

class IPTesterSpider(scrapy.Spider):
    name = 'IPtester'
    allowed_domains = ['icanhazip.com']
    start_urls = (
        'https://icanhazip.com',
    )

    def parse(self, response):
        soup = BeautifulSoup(response.body, 'html.parser')
        if ip_address := soup.get_text().rstrip('\n'):
            logging.info('IP ADDRESS = %s', ip_address)
        else:
            logging.info('IP ADDRESS NOT FOUND')