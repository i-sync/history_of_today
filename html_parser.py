# -*- coding: utf-8 -*-
import bs4

class HtmlParser(object):
    
    def __init__(self):
        pass
        
    def get_children_content(self, element):
        result = ''
        for e in element:
            if e.name == 'sup':
                continue
                        
            if e.name == 'mark':
                result += self.get_children_content(e)
                continue
            if e.name == 'ul':
                result += self.get_children_content(e.find('li'))
                continue
            if type(e) is not bs4.element.NavigableString:
                if e.string is not None:
                    result += e.string
            else:
                result += e
        return result.replace('：', ':')

    def get_year(self, element):
        for e in element:
            if e is None:
                continue
            if type(e) is bs4.element.NavigableString and e.find('年：') > -1:
                return e[:e.find('年：')]
            if e.string is not None and e.string.endswith('年'):
                return e.string.strip('年')
        return 'None'

    def get_index(self, doc): 
        res = []       
        for li in doc:
            if li is None:
                continue
            link = li.find('a')            
            if link is None or type(link) is int:
                continue
            #ids.append(link['href'].strip('#'))
            spans = link.find_all('span')
            num = spans[0].string
            name = spans[1].string

            # if it is dashiji get children
            if num == '1':
                r = self.get_index(li.find('ul'))
                for i in r:
                    i[0] = num
                    i[1] = name
                res.extend(r)
                continue
            
            res.append([num, name, link['href'].strip('#')])
            if num == '3':
                break

        return res

    def parse(self, new_cont):
        if new_cont is None:
            return None

        soup = bs4.BeautifulSoup(new_cont, 'html.parser', from_encoding = 'utf-8')
        ul = soup.find('div', id = 'toc').find('ul')

        dicts = {}
        res = self.get_index(ul)
        for r in res:
            #print(r, type(r))
            #if type(r) is bs4.element.NavigableString:
            #    continue
            tag = soup.find(id = r[2]).parent
            ul = tag.find_next_sibling('ul')
            ls = []
            for li in ul:
                if li.name != 'li':
                    continue
                year = self.get_year(li)
                title = self.get_children_content(li)
                ls.append([year,title])

            key = (r[0], r[1])
            #print(key)
            if key in dicts:                
                dicts.get(key).extend(ls)
                continue
            
            dicts[key] = ls
        
        return dicts
