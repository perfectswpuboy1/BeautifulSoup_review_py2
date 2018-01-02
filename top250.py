#coding:utf-8
#!/usr/bin/env python
# encoding=utf-8

"""
爬取豆瓣电影TOP250 - 完整示例代码
"""

import codecs

import requests
from bs4 import BeautifulSoup

DOWNLOAD_URL = 'http://movie.douban.com/top250/'


def download_page(url):
    return requests.get(url, headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }).content


def parse_html(html):
    soup = BeautifulSoup(html,"lxml")

    movie_list_soup = soup.find('ol', attrs={'class': 'grid_view'})  #查找ol标签，就是网页中电影介绍的主体。将它保存到参数。

    movie_name_list = []  #新建一个空的列表，用来存储电影名字

    for movie_li in movie_list_soup.find_all('li'):                            #得到刚才  movie_list_soup 下面所有li的内容，并且用for循环遍历其元素
        detail = movie_li.find('div', attrs={'class': 'hd'})                   #找到满足要求的div标签，条件是calss名称是hd。  就是影片详情。
        movie_name = detail.find('span', attrs={'class': 'title'}).getText()   #<span class="title">肖申克的救赎</span>
                                                                               #这里用到了getText()方法

        movie_name_list.append(movie_name)                                     #列表中增加影片名称。

    next_page = soup.find('span', attrs={'class': 'next'}).find('a')
    if next_page:
        return movie_name_list, DOWNLOAD_URL + next_page['href']
    return movie_name_list, None


def main():
    url = DOWNLOAD_URL

    with codecs.open('movies', 'wb', encoding='utf-8') as fp:
        while url:
            html = download_page(url)
            movies, url = parse_html(html)
            fp.write(u'{movies}\n'.format(movies='\n'.join(movies)))


if __name__ == '__main__':
    main()