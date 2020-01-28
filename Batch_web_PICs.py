#coding:utf-8
#!/usr/bin/env python
# encoding=utf-8
import urllib
import os
import urllib2

def Schedule(a,b,c):
    '''''
    a:已经下载的数据块
    b:数据块的大小
    c:远程文件的大小
   '''
    per = 100.0 * a * b / c
    if per > 100 :
        per = 100
    print '%.2f%%' % per
#url = 'http://anzaimisa.vastserve.com/Despacito/Matteo/juicyhoney/jh208_yua/imagepages/image150.htm'
#url = 'http://anzaimisa.vastserve.com/Despacito/Matteo/juicyhoney/jh208_yua/images/l_150.jpg'
url_base = 'http://whoowhoo.byethost31.com/gra_julia6/image/gra_julia6'

#local = url.split('/')[-1]
#i=0
#for i in range(1,120):
#   n=str(i)
#   s = n.zfill(3)
#   print s
i=0   
save_dir='/Users/llm/Downloads/webPICs'

for i in range(5):
	pic_name=str(i+1).zfill(3)+'.jpg'
	print pic_name
	local = os.path.join(save_dir,pic_name)
	url=url_base+pic_name
	print url
	f=urllib2.urlopen(url)
	data=f.read()
	with open(local, "wb") as code:
		code.write(data)


	#urllib.urlretrieve(url,local,Schedule)

'''This site requires Javascript to work, please enable Javascript in your browser or use a browser with Javascript support'''





