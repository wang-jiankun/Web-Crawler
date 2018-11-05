"""
网络爬虫 -- Requests 库实战案例
author: 王建坤
date: 2018-11-5
"""
import requests
import os


def get_html_text(url):
    """
    爬取网页的通用代码框架
    :param url:
    :return:
    """
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return '产生异常'


def jd_goods():
    """
    爬取京东上的某个商品，以华为 mate20 为例
    :return:
    """
    url = 'https://item.jd.com/100000822981.html'
    print(get_html_text(url))


def amazon_goods():
    """
    爬取京东上的某个商品，以Kindle为例
    :return:
    """
    url = 'https://www.amazon.cn/gp/product/B07746N2J9'
    try:
        hd = {'user-agent': 'Mozilla/5.0'}
        r = requests.get(url, headers=hd)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(r.text)
    except:
        print('爬取失败')


def baidu_search():
    """
    使用百度搜索引擎，提交关键词查询
    :return:
    """
    url = 'http://www.baidu.com/s'
    keyword = 'python'
    try:
        kv = {'wd': keyword}
        r = requests.get(url, params=kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(r.text)
    except:
        print('爬取失败')


def download_image():
    """
    爬取图片，以百度的logo为例
    :return:
    """
    url = 'https://www.baidu.com/img/bd_logo1.png'
    root = 'E:/pics/'
    path = root + url.split('/')[-1]
    try:
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            r = requests.get(url)
            with open(path, 'wb') as f:
                f.write(r.content)
                f.close()
                print('图片保存成功')
        else:
            print('图片已存在')
    except:
        print('爬取失败')


def ip_attribution():
    """
    IP地址归属地查询, 使用138的接口查询百度的IP归属地
    :return:
    """
    url = 'http://m.ip138.com/ip.asp?ip='
    ip = '14.215.177.39'
    try:
        r = requests.get(url+ip, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(r.text)
    except:
        print('查询失败')


if __name__ == '__main__':
    print('running request:')

