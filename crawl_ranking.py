"""
网络爬虫 -- Beautiful Soup 库实战：爬取中国大学排名
author: 王建坤
date: 2018-11-5
"""
import requests
from bs4 import BeautifulSoup
import bs4


def get_html_text(url):
    """
    从网络上获取大学排名网页内容
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


def fill_univ_list(univ_list, html):
    """
    提取网页内容中的信息（大学排名表）到合适的数据结构
    :param univ_list:
    :param html:
    :return:
    """
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            univ_list.append([tds[0].string, tds[1].string, tds[3].string])


def print_univ_list(univ_list, num):
    """
    输出结果，即大学排名表
    :param univ_list:
    :param num:
    :return:
    """
    # 格式化输出，使用中文字符填充空白实现居中对齐
    template = "{0:^10}\t{1:{3}^10}\t{2:^10}"
    print(template.format("排名", "学校名称", "总分", chr(12288)))
    for i in range(num):
        u = univ_list[i]
        print(template.format(u[0], u[1], u[2], chr(12288)))


def main():
    """
    输入大学排名的 url，得到排名表
    :return:
    """
    univ_info = []
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2018.html'
    html = get_html_text(url)
    fill_univ_list(univ_info, html)
    print_univ_list(univ_info, 20)  # 20 univs


if __name__ == '__main__':
    print('running crawl_ranking')
    main()
