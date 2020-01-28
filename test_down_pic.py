#coding:utf-8
#!/usr/bin/env python
# encoding=utf-8
#http://www.qpic.ws/images/m002eve.jpg



import os,sys,urllib2,urllib

PROXY_INFO = {
	'host' : '127.0.0.1' ,
	'port' : 1087
}

def load_url(url): 
	proxy_support = urllib2.ProxyHandler( { 'http' : 'http://%(host)s:%(port)d' % PROXY_INFO } ) 
	opener = urllib2.build_opener(proxy_support,urllib2.HTTPHandler)
	urllib2.install_opener(opener) 
	src = urllib2.urlopen(url)
	return src.read()
    
if __name__=='__main__':
  print load_url("http://anzaimisa.vastserve.com/Despacito/Matteo/juicyhoney/jh208_yua/images/l_003.jpg")






#########

save_dir='/Users/llm/Downloads/webPICs'


#pic_name=str(i+1).zfill(3)+'.jpg'
pic_name='m002eve.jpg'
print pic_name
local = os.path.join(save_dir,pic_name)
url='http://www.qpic.ws/images/m002eve.jpg'

#url=url_base+pic_name
print url
f=urllib2.urlopen(url)
data=f.read()
with open(local, "wb") as code:
	code.write(data)