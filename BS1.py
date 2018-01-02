# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
'''
beautifulsoup对象创建
'''


soup=BeautifulSoup('<b class="boldent">Extrenmely bold </b>',"lxml")

a=soup.b
type(a)
print type(a)
print a

print "Tag a's name is %s \n" %a.name
print "Tag a's attrs is %s \n" %a.attrs
print a['class']
print "-"*20+"华丽的分割线"+"-"*20
print a.string
print type(a.string)
print "-"*20+"华丽的分割线"+"-"*20


