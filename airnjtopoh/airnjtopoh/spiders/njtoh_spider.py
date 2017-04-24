import scrapy
from airnjtopoh.items import AirnjtopohItem
import csv

class HlSpider(scrapy.Spider):
    base_url = "https://www.airdna.co/top/cn/nanjing-shi"
    url_suffix = ""
    init_url = base_url + url_suffix

    name = "nt"
    allowed_domains = ["airdna.co"]
    start_urls = [
        init_url
    ]

    csvfile = file('csv_test.csv', 'wb')
    writer = csv.writer(csvfile)

    def parse(self, response):
        for curr_page in range(0, 100):
            item = AirnjtopohItem()
            item['houseName'] = response.xpath('//div[@class="panel-body"]//table[@class="table property-list"]//tr//a[@target="_blank"]/text()').extract()[curr_page].encode('utf-8')
            item['houseLink'] = response.xpath('//div[@class="panel-body"]//table[@class="table property-list"]//tr//a[@target="_blank"]/@href').extract()[curr_page].encode('utf-8')
            item['houseDetail'] = response.xpath('//div[@class="panel-body"]//table[@class="table property-list"]//tr//span[1]/text()').extract()[curr_page].encode('utf-8')
            item['housePrice'] = response.xpath('//div[@class="panel-body"]//table[@class="table property-list"]//tr//strong/text()').extract()[curr_page].encode('utf-8').strip()
            self.writer.writerow([item['houseName'], item['houseLink'], item['houseDetail'], item['housePrice']])
