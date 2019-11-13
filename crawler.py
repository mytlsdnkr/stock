from korea_news_crawler.articlecrawler import ArticleCrawler

Crawler = ArticleCrawler()  
Crawler.set_category("정치")  
Crawler.set_date_range(2019, 11, 2019, 11)  
Crawler.start()



