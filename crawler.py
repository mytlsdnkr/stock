from korea_news_crawler.articlecrawler import ArticleCrawler
Crawler = ArticleCrawler()  
Crawler.set_category("정치","경제","사회","생활문화","세계","IT과학","오피니언")  
Crawler.set_date_range(2019, 11, 2019, 11)  
Crawler.start()


