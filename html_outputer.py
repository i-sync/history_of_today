# -*- coding: utf-8 -*-
import json

class OutPutResult(object):
    month = 1
    day = 1
    res = []
    def __init__(self, month, day):
        self.month = month
        self.day = day

    def add_list(self, model):
        self.res.append(model)

    def to_json(self):
        return json.dumps(self, default = lambda o : o.__dict__, indent = 4)

class OutPutResultChild(object):
    id = 0
    

class HtmlOutputer(object):

    def collect_data(self, new_data):
        pass
    
    def output_json(self):
        pass