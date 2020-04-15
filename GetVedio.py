# -*- coding:utf-8 -*-
# from<库名>import<函数名>
import requests
from bs4 import BeautifulSoup
# selenium 模拟浏览器打开网页
# from selenium import webdriver

# 下载在线播放的视频 m3u8
# 1、访问网站获取m3u8文件
# 2、下载ts文件

class GetVedio:

    # 目标url
    # url = 'http://dm.dm530.net/v/6761-0-145.html'

    # 构造函数，类里面的方法一定要有参数，默认self
    def __init__(self):
        # 目标url
        self.url = 'http://dm.dm530.net/v/21481-0-0.html'

    # 获取m3u8文件
    def getM3U8(self):
        print()
        req = requests.get(url=self.url)
        req.encoding = 'GBK'
        html = req.text
        # print(html)
        # browser = webdriver.Chrome()
        # browser.get('http://dm.dm530.net/v/21481-0-0.html')
        content = req.content
        # 要有正确的解析器module
        bf = BeautifulSoup(html, 'html5lib')
        # find_all返回的是数组
        iframe = bf.find_all('iframe')
        print(iframe)

if __name__ == '__main__':
    print('在线视频下载开始')
    gv = GetVedio()
    # 1.获取m3u8文件
    gv.getM3U8()

