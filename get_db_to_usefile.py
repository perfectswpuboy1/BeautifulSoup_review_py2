# -*- coding: utf-8 -*-
'''
	将数据库数据取出，每20条一个文件，存储到文件。
	改天再来。

'''

import codecs
import requests
from bs4 import BeautifulSoup
import pymongo_imp

db = pymongo_imp.get_db()
my_collection = pymongo_imp.get_collection(db)



#print "截止目前，数据库中存放条目数量：%s个" % int(my_collection.count())