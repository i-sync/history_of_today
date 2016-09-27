# -*- coding: utf-8 -*-
import url_manager
import html_downloader
import html_outputer
import html_parser
#new_url = (12, 11, 'https://zh.wikipedia.org/zh-cn/12%E6%9C%8811%E6%97%A5')
class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self):
        while self.urls.has_new_url():
            new_url = self.urls.get_new_url()
            html_cont = self.downloader.download(new_url)
            new_data = self.parser.parse(html_cont)
            self.outputer.collect_data(new_url, new_data)
            
        #self.outputer.output_json()
             
if __name__ == '__main__':
    obj_spider = SpiderMain()
    obj_spider.craw()