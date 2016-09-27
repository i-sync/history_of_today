# -*- coding: utf-8 -*-

class UrlManager(object):
    
    def __init__(self):
        self.base_url = 'https://zh.wikipedia.org/zh-cn/{month}%E6%9C%88{day}%E6%97%A5'
        self.urls = []
        
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