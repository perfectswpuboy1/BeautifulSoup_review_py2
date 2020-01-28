# -*- coding: utf-8 -*-
import urllib2
import urllib
from lxml import etree
from bs4 import BeautifulSoup

'''
    一定要注意从网上粘贴过来的代码需要重新调整一下缩进！！！
    本代码是python2的代码，python3不适用。
    #任务1:筛选文件大小满足条件的文件
    #任务2:使用代理，而不是使用全局代理。使得其他软件的使用不受影响。
    #任务3:根据搜索内容，转换为正常字符，命名文件名保存，而不是每次都是同一个文件名。     <<<<<<OK!>>>>>>
    #任务4:每20个链接保存一个文件，之后另增加文件保存。                             <<<<<<OK!>>>>>>
    #任务5:将抓取内容存放到MySQL或者其他简单数据库。
    #任务6:增加用户输入，然后搜索用户输入的内容。                                  <<<<<<OK!>>>>>>
    #任务7:使用beautifulsoup方法实现抓取。实现高级筛选功能。
'''

'''
	思考：
	BS貌似比xpath更加简洁。
	BS
	目前关键问题是大小标签和magnet标签是同级别的，如何去判断然后筛选，很伤脑经。
'''

url = 'https://www.torrentkitty.tv/search/'

keys2x = raw_input("请输入搜索关键字：")

keyword = urllib.quote(keys2x)  # 这是python2的语法

pages = 5

# os.chdir('/Users/llm/PycharmProjects/')

file_name = '/Users/llm/PycharmProjects/' + keys2x + '.txt'

ks = file_name

for page in range(0, pages):
    page = str(page)

    site = url + keyword + '/' + page

    h = urllib2.Request(site)

    h.add_header('User-Agent',
                 'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.8.1.14) Gecko/20080404 (FoxPlus) Firefox/2.0.0.14')

    ht = urllib2.urlopen(h)
    html = ht.read(ht)
########################从这以后对其改造为Beautifulsoup解析。

    #content=BeautifulSoup(html.lower().decode('utf-8'),"html.parser")
    #mags = content.find_all()




    content = etree.HTML(html.lower().decode('utf-8'))
    # print content
    mags = content.xpath("//a[@rel='magnet']")  # 精确定位标签属性值为‘magnet’的内容
    # 如何存储多个内容？？
    # mags=content.xpath("//a[@rel='magnet']")   #关键是这个函数。如何控制？
    # print mags
    file_name = ks + '_' + page  # 让文件按页码保存，避免一个文件中链接数量太多。
    with open(file_name, 'a') as p:  # '''Note'''：Ａppend mode, run only once!
        # cont=0
        for mag in mags:
            # cont=cont+1
            # print "%s \n \n"%(mag.attrib['href'])
            p.write("%s \n \n" % (mag.attrib['href']))  ##!!encode here to utf-8 to avoid encoding
            '''
            获取mag对象的attrib属性
            '''














