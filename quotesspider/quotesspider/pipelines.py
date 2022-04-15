import sqlite3

"""
Item pipeline is similar to 
Post processing for each item crawled
"""


class QuotesspiderPipeline:

    def open_spider(self, spider):
        # called when the spider is opened
        self.con = sqlite3.connect('quotes.db') # create a DB
        self.cur = self.con.cursor()
        self.cur.execute('''DROP TABLE IF EXISTS quotes''') # drop table if already exists
        self.cur.execute('''CREATE TABLE quotes
                       (quote text, author text)''') # create a table
        self.con.commit()

    def close_spider(self, spider):
        # called when the spider is closed
        self.con.close()

    def process_item(self, item, spider):
        # called for each item crawled from spiders/quotes-spiders.py
        # insert the each item crawled into DB
        self.cur.execute("insert into quotes values (?, ?)", (item['quote'], item['author']))
        self.con.commit()
        return item
