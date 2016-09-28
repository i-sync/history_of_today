# -*- coding: utf-8 -*-

import os

class UrlManager(object):
    
    def __init__(self):
        self.base_url = 'https://zh.wikipedia.org/zh-cn/{month}%E6%9C%88{day}%E6%97%A5'
        self.urls = []
        
        #first check error.txt file content, then generate before error url
        filename = 'files/error.txt'
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                for data in f:
                    data = data.strip()
                    #print(data)
                    if data.find('-') > -1:
                        date = data.split('-')
                        self.urls.append((date[0], date[1], self.base_url.format(month = date[0], day = date[1])))

            #truncate file
            with open(filename, 'w') as f:
                pass

            if len(self.urls) > 0:
                return

        for m in range(1, 13):
            for d in range(1, 32):
                if m == 2 and d > 29:
                    continue
                if m in [4,6,9,11] and d > 30:
                    continue
                #print('%d - %d' % (m, d))
                self.urls.append((m, d, self.base_url.format(month = m, day = d)))
    
    def get_new_url(self):
        if len(self.urls) > 0:
            return self.urls.pop()
        else:
            return None

    def has_new_url(self):
        return len(self.urls) > 0

        
'''
url = UrlManager()
while url.has_new_url():
    print(url.get_new_url())
'''