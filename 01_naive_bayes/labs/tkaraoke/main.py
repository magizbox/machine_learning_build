from scrapy import cmdline
cmdline.execute("scrapy runspider spider.py -o poems.csv".split())