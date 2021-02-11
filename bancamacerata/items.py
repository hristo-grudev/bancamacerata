import scrapy


class BancamacerataItem(scrapy.Item):
    title = scrapy.Field()
    description = scrapy.Field()
