# -*- coding: utf-8 -*-
html_data="""
<html><head><title>The Dorman's story</title></head></html>
<p class="title"><b>The Dorman's story</b></p>
<p class ="story">Come opus time were ljljljlkajldfjaldfjasd
<a href="http://example.com/eccc" class="sister" id="link1">Elsie</a>
<a href="http://example.com/jljlk" class="sister> id="link2">Lasii</a>
<a href="http://example.com/jljl" class ="sister" id="link3">Tills</a>
and they lived at the hotformof well </p>
<p class="story">.........</p>
"""
from bs4 import BeautifulSoup
soup=BeautifulSoup(html_data,"html.parser")  #只有使用html.parser解析器find_all才管用！！！
#print soup   #点取只能取到第一个条目
x1=soup.find_all('a')  #为何这里取到的也只有第一条？？？？
print x1

import re
for tag in soup.find_all(re.compile("^b")):
    #正则表达式
    print(tag.name)