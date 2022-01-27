#this is task 1 created for Topware items
import scrapy
from ..items import Pktask1Item

class Task1Spider(scrapy.Spider):
    name = 'Topwares'
    page_number = 2
    start_urls = [
        'https://www.net-a-porter.com/en-in/shop/clothing/tops'
    ]

    def parse(self, response):
        items = Pktask1Item()
        product_name = response.css('span.ProductItem24__name::text').extract()
        brand = response.css('span.ProductItem24__designer::text').extract()
        product_price = response.css('span.price::text').extract()
        product_image_url = response.css('img.Image18__image--loaded::text').extract()
        # product_page_url  = response.css('').extract()
        product_category = response.css('div.ShopMore84 ProductDetailsPage84__shopMore ProductDetailsPage84__shopMore--bottomDetails ShopMore84__links::text').extract()

        items['product_name'] = product_name
        items['brand'] = brand
        items['product_price'] = product_price
        items['product_image_url'] = product_image_url
        # items['product_page_url'] = product_page_url
        items['product_category'] = product_category

        yield items

        next_page = 'https://www.net-a-porter.com/en-in/shop/clothing/tops?pageNumber='+ str(Task1Spider.page_number)
        if Task1Spider.page_number <= 25:
            Task1Spider.page_number += 1
            yield response.follow(next_page, callback= self.parse)


