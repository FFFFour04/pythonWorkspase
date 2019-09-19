# -*- coding:UTF-8 -*-
import requests
from bs4 import BeautifulSoup
# import html5lib

"""
《一念永恒下载》
"""
class DownYnyh:

    # 构造函数，类里面的方法一定要有参数，默认self
    def __init__(self):
        # 网址目录页
        meanListHtml = 'https://www.biqukan.com/1_1094/'
        # 存放章节链接
        self.urls = []

    # 获取菜单目录
    def findMeanList(self):
        meanresponse = requests.get(url=self.meanListHtml)
        # 需要与网页的字符集保持一致
        meanresponse.encoding = 'gbk'
        meanHtml = meanresponse.text
        # 要有正确的解析器
        bf = BeautifulSoup(meanHtml, 'html5lib')
        # find_all返回的是数组
        meanList = bf.find_all('div', class_='showtxt')


if __name__ == '__main__':
    print('下载《一念永恒》--start--')
    down = DownYnyh()
    response = requests.get
    print(text[0].text.replace('\xa0' * 8, '\n\n'))
    print('下载《一念永恒》--end--')