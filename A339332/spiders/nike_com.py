from __future__ import absolute_import

from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Identity
from scrapy.spiders import Rule

from ..utils.spiders import BasePortiaSpider
from ..utils.starturls import FeedGenerator, FragmentGenerator
from ..utils.processors import Item, Field, Text, Number, Price, Date, Url, Image, Regex
from ..items import PortiaItem


class Nike(BasePortiaSpider):
    name = "www.nike.com"
    allowed_domains = [u'www.nike.com']
    start_urls = [u'https://www.nike.com/launch/?s=in-stock']
    rules = [
        Rule(
            LinkExtractor(
                allow=(u'https://www.nike.com/launch/*'),
                deny=()
            ),
            callback='parse_item',
            follow=True
        )
    ]
    items = [[Item(PortiaItem,
                   None,
                   u'.product-info',
                   [Field(u'Product',
                          '.test-subtitle *::text',
                          []),
                       Field(u'Price',
                             '.pb6-sm *::text',
                             []),
                       Field(u'description',
                             '.description-text > p *::text',
                             [])])]]
