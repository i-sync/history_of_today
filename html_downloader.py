# -*- coding: utf-8 -*-

import urllib.request

class HtmlDownloader(object):

    def download(self, new_url):
        if new_url is None:
            return None
        request = urllib.request.Request(new_url[2], headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36'})
        try:
            response = urllib.request.urlopen(request)
        except urllib.error.HTTPError as e:
            print(e.getcode())
            print(e.reason)
            print(e.geturl())
            print('-----------------')
            print(e.info())
            print(e.read())
            return None
            
        if response.getcode() != 200:
            return None
        return response.read()