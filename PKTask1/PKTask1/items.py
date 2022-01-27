# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Pktask1Item(scrapy.Item):
    # define the fields for your item here like:

    brand = scrapy.Field()
    product_name = scrapy.Field()
    product_price =scrapy.Field()
    product_image_url = scrapy.Field()
    # product_page_url = scrapy.Field()
    product_category = scrapy.Field()