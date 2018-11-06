"""
网络爬虫 -- 实战：淘宝商品比价定向爬虫
author: 王建坤
date: 2018-11-6
"""
import requests
import re


def get_html_text(url):
    """
    获取 HTML 页面内容
    :param url:
    :return:
    """
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def parse_page(goods_list, html):
    """
    解析 HTML 页面内容，提取商品的名称和价格
    :param goods_list:
    :param html:
    :return:
    """
    try:
        # 提取页面中商品的名称和价格
        plt = re.findall(r'"view_price":"[\d.]*"', html)
        tlt = re.findall(r'"raw_title":".*?"', html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            goods_list.append([price, title])
    except:
        print("")


def print_goods_list(goods_list):
    """
    打印商品的列表
    :param goods_list:
    :return:
    """
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0
    for g in goods_list:
        count = count + 1
        print(tplt.format(count, g[0], g[1]))


def main():
    """
    根据商品名称进行爬取
    :return:
    """
    goods = '书包'
    depth = 3
    # 淘宝搜索入口
    start_url = 'https://s.taobao.com/search?q=' + goods
    goods_list = []
    for i in range(depth):
        try:
            # 每页有44个商品，但现在提交&s参数会要求登录
            # url = start_url + '&s=' + str(44 * i)
            url = start_url
            html = get_html_text(url)
            parse_page(goods_list, html)
        except:
            continue
    print_goods_list(goods_list)


if __name__ == '__main__':
    print('running crawl_taobao')
    main()
