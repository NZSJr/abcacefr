import scrapy
class NewSpider(scrapy.Spider):
    name = "new_spider"
    start_urls = ['http://brickset.com/sets/year-2019']

    def parse(self, response):
        xpath_selector = '//img'
        for x in response.xpath(xpath_selector):
            newsel = '@src'
            yield {'Image Link': x.xpath(newsel).extract_first(), }

# To Recurse next page
        page_selector = '.next a ::attr(href)'
        next_page = response.css(page_selector).extract_first
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)

#wengkuen
