# scrapy-tutorials
Tutorial on scrapy web scraping framework

# This is github repo for Medium Blog post

# environment setup

```shell
pip install -r requirements.txt
```

# run the scrapyd server

```shell
scrapyd
```

# run locally

scrapy crawl quotes

# deploy to scrapyd server

```shell
scrapyd-deploy local -p quotesspider
scrapyd-client schedule -p quotesspider quotes
```
