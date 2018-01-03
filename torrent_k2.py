# -*- coding: utf-8 -*-
import urllib2
import urllib
from lxml import etree

###########################华丽分割线
import codecs

import requests
from bs4 import BeautifulSoup

'''
    一定要注意从网上粘贴过来的代码需要重新调整一下缩进！！！
    本代码是python2的代码，python3不适用。
    #任务1:筛选文件大小满足条件的文件                                              <<<<<<OK!>>>>>>
    #任务2:使用代理，而不是使用全局代理。使得其他软件的使用不受影响。
    #任务3:根据搜索内容，转换为正常字符，命名文件名保存，而不是每次都是同一个文件名。     <<<<<<OK!>>>>>>
    #任务4:每20个链接保存一个文件，之后另增加文件保存。                               <<<<<<OK!>>>>>>
    #任务5:将抓取内容存放到MySQL或者其他简单数据库。
    #任务6:增加用户输入，然后搜索用户输入的内容。                                    <<<<<<OK!>>>>>>
    #任务7:使用beautifulsoup方法实现抓取。实现高级筛选功能。                         <<<<<<OK!>>>>>>
'''

'''
	心得：
	BS的语法确实比xpath更加简洁容易懂，理清思路，分步一步一步循序渐进，就能够得到解决方案。

'''

url = 'https://www.torrentkitty.tv/search/'

keys2x = raw_input("请输入搜索关键字：")

keyword = urllib.quote(keys2x)  # 这是python2的语法

pages = 40

# os.chdir('/Users/llm/PycharmProjects/')

file_name = '/Users/llm/PycharmProjects/' + keys2x + '.txt'

ks = file_name




for page in range(0, pages):
    page = str(page)

    site = url + keyword + '/' + page

    h = urllib2.Request(site)  ###

    h.add_header('User-Agent',
                 'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.8.1.14) Gecko/20080404 (FoxPlus) Firefox/2.0.0.14')



    ht = urllib2.urlopen(h)
    html = ht.read(ht)

    soup = BeautifulSoup(html, "lxml")                                              #####>>>>>>1     创建美丽汤。
    movie_list_soup = soup.find('table', attrs={'id': 'archiveResult'})             #####>>>>>>2     定位到列表所在位置。#archiveResult
    movie_name_list = []                                                            #####>>>>>>3     新建列表，存放查找内容。
    search_flag=0
    for movie_li in movie_list_soup.find_all('tr'):                                 #####>>>>>>4     设置过滤器。找到所有tr标签。
        search_flag=search_flag+1
        if search_flag > 1:                                                         #####>>>>>>4.1   设置查找标志，跳过第一个，因为第一个是表头。
            #还需要考虑翻页的问题？
            detail = movie_li.find('td', attrs={'class': 'size'}).getText()         #####>>>>>>5     定位所有的size标签，得到字符串。
            #print "%s \n" % detail
            if movie_li.find('a', attrs={'rel': 'magnet'}) is None:
                pass
            else:

                detail_name1 = movie_li.find('a', attrs={'rel': 'magnet'})['title']
                FHD_flag=detail_name1.find('FHD')
                Thz_flag=detail_name1.find('Thz.la')
            if FHD_flag<>-1 or Thz_flag<>-1:                                         #####>>>>>>5.1     如果是高清或者是tha.lz那么就存档。


            ##if detail.find('mb')<>-1:                                               #####>>>>>>6     如果文件大小满足要求，那么下一步寻找兄弟节点。
                #文件名称
                if movie_li.find('a', attrs={'rel': 'magnet'}) is None:
                    pass
                else:
                    detail_name=movie_li.find('a', attrs={'rel': 'magnet'})['title']
                    print detail_name
                # 文件大小  detail
                print detail
                #链接地址
                file_name = ks + '_' + page  # 让文件按页码保存，避免一个文件中链接数量太多。
                if movie_li.find('a', attrs={'rel': 'magnet'}) is None:                ####>>>>>>>      如果为非空，那么就获取。
                    pass
                else:
                    detail_mag=movie_li.find('a', attrs={'rel': 'magnet'})['href']      #####>>>>>>7     获取磁力链接地址。
                    print detail_mag

                    with open(file_name, 'a') as p:  # '''Note'''：Ａppend mode, run only once!
                        p.write("%s \n \n" % detail_mag)  ##!!encode here to utf-8 to avoid encoding






    #file_name = ks + '_' + page  # 让文件按页码保存，避免一个文件中链接数量太多。


    #with open(file_name, 'a') as p:  # '''Note'''：Ａppend mode, run only once!

       # for mag in mags:

            #p.write("%s \n \n" % (mag.attrib['href']))  ##!!encode here to utf-8 to avoid encoding















