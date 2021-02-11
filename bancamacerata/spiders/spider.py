import scrapy

from scrapy.loader import ItemLoader
from ..items import BancamacerataItem
from itemloaders.processors import TakeFirst


class BancamacerataSpider(scrapy.Spider):
	name = 'bancamacerata'
	start_urls = ['https://www.bancamacerata.it/news/',
	              'https://www.bancamacerata.it/blog-banca-macerata'
	              ]

	def parse(self, response):
		post_links = response.xpath('//h2[@itemprop="name"]/a/@href').getall()
		yield from response.follow_all(post_links, self.parse_post)

		next_page = response.xpath('//a[@title="Avanti"]/@href').getall()
		yield from response.follow_all(next_page, self.parse)


	def parse_post(self, response):
		title = response.xpath('//h1[@itemprop="name"]/text()').get()
		description = response.xpath('//div[@itemprop="articleBody"]//text()[normalize-space()]').getall()
		description = [p.strip() for p in description]
		description = ' '.join(description).strip()

		item = ItemLoader(item=BancamacerataItem(), response=response)
		item.default_output_processor = TakeFirst()
		item.add_value('title', title)
		item.add_value('description', description)

		return item.load_item()
