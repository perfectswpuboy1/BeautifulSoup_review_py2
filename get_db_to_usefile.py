# -*- coding: utf-8 -*-
'''
	将数据库数据取出，每20条一个文件，存储到文件。
	改天再来。

'''

import codecs
import requests
from bs4 import BeautifulSoup
import pymongo_imp


search_list=['SNIS','MIRD','MILD','PPPD','DPMI','HEYZO','IPTD','MIGD','carib','MXGS','MIAD','WANZ','E-BODY','ONSD','SOE','LAFBD','MIDD','Moodyz','MCB3DBD','JUFD','MIDE','DPMX','HODV','MIDD','明日花','神咲詩織','天海翼','市来美保','吉沢明歩','仁科百華','Julia','SSNI','Rion','明日花绮罗','桃谷绘里香','冲田杏梨','大桥未久','AIKA']

for keys2x in search_list:
    file_name = '/Users/llm/PycharmProjects/' + keys2x + '.txt'
    print "开始进行mongodb数据库操作:"
    #
    db = pymongo_imp.get_db()
    my_collection = pymongo_imp.get_collection(db)


    xlist=pymongo_imp.get_many_docs(db,keys2x)
   
    for listnet in xlist:
        mag_1=listnet['Magnet_Link'].encode('gb2312')
        with open(file_name, 'a') as p:  # '''Note'''：Ａppend mode, run only once!

            p.write("%s \n \n" % mag_1)  ##!!encode here to utf-8 to avoid encoding










    #print "截止目前，数据库中存放条目数量：%s个" % int(my_collection.count())





#print "截止目前，数据库中存放条目数量：%s个" % int(my_collection.count())