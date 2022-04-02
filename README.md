# scrapy-tutorials
Tutorial on scrapy web scraping framework

# environment setup

pip install scrapy


>>> response
<200 https://quotes.toscrape.com/>

response.text

response.xpath('//title').get()
'<title>Quotes to Scrape</title>'

>>> quote = response.xpath('//div[@class="quote"]')[0]
>>> quote
<Selector xpath='//div[@class="quote"]' data='<div class="quote" itemscope itemtype...'>
> 
> 
> 
> >>> quote.xpath('span/text()').get()
'“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”'
>>> quote.xpath('span/small/text()').get()
'Albert Einstein'
> 
> 