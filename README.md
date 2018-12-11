# InvoiceCrawler
Implement Python with the Scrapy to crawl invoice award number from Ministry of Finance.  
實作 Python 搭配 Scrapy 套件來爬取財政部的發票中獎號碼

Use these commands to crawl below. The data will be saved as a CSV file.  
使用下列指令開始爬取。資料將儲存為 CSV 檔。

    scrapy crawl invoice -o award_num.csv