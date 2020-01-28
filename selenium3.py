#coding:utf-8
from selenium import webdriver
driver = webdriver.Chrome()#如果不方便配置环境变量。就使用phantomjs的绝对路径也可以

driver.get('http://image.baidu.com/i?ie=utf-8&word=%E5%91%A8%E6%9D%B0%E4%BC%A6')#抓取了百度图片，query：周杰伦

driver.page_source #这就是返回的页面内容了，与urllib2.urlopen().read()的效果是类似的，但比urllib2强在能抓取到动态渲染后的内容。
#print driver.page_source
driver.quit()