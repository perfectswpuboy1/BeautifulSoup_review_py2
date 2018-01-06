# -*- coding: utf-8 -*-
'''
	输入关键字，从数据库提取搜索结果，保存到文件并打印出结果。
'''
import codecs
import requests
from bs4 import BeautifulSoup
import pymongo_imp


def search_db():

    keys2x = raw_input("请输入搜索关键字：")
#for keys2x in search_list:
    file_name = '/Users/llm/PycharmProjects/' + keys2x + '.getone.txt'
    print "开始进行mongodb数据库操作:"
    #
    db = pymongo_imp.get_db()
    my_collection = pymongo_imp.get_collection(db)


    xlist=pymongo_imp.get_many_docs(db,keys2x)

    for listnet in xlist:
        mag_1=listnet['Magnet_Link'].encode('gb2312')
        with open(file_name, 'a') as p:  # '''Note'''：Ａppend mode, run only once!

            p.write("%s \n \n" % mag_1)  ##!!encode here to utf-8 to avoid encoding

if __name__ == '__main__':

    search_db()