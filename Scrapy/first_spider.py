# Import library
import scrapy

# Documentantion: https://docs.scrapy.org/en/latest/intro/tutorial.html

def clean_text(text):
        text = text.strip(u'\u201c')
        text = text.strip(u'\u201d')
        return text

class QuoteSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
            'http://quotes.toscrape.com/page/1/'
    ]
    def parse(self, response):
        for quote in response.css('div.quote'):
                yield {
                        'text': clean_text(quote.css('span.text::text').get()),
                        'author': quote.css('small.author::text').get(),
                        'tags': quote.css('div.tags a.tag::text').getall()
                        }
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
                yield response.follow(next_page, callback=self.parse)
    # Pegar em JSON:
        # scrapy crawl quotes -o quotes.json