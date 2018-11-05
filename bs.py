"""
网络爬虫 -- Beautiful Soup 库基础
author: 王建坤
date: 2018-11-5
"""
import requests
from bs4 import BeautifulSoup


def bs4_test():
    """
    BeautifulSoup 库安装测试
    :return:
    """
    r = requests.get('https://python123.io/ws/demo.html')
    demo = r.text
    soup = BeautifulSoup(demo, 'html.parser')
    print(soup.prettify())


def tag_element():
    """
    BeautifulSoup 的 tag，及其属性
    :return:
    """
    html = requests.get('https://python123.io/ws/demo.html')
    soup = BeautifulSoup(html.text, 'html.parser')
    # Tag
    tag = soup.p
    print(type(tag))
    print(tag)
    # Name
    name = tag.name
    print(type(name))
    print(name)
    # Attributes
    attrs = tag.attrs
    print(type(attrs))
    print(attrs)
    # NavigableString
    content = tag.string
    print(type(content))
    print(content)
    # Comment
    soup1 = BeautifulSoup('<b><!--This is a comment--></b>', 'html.parser')
    comment = soup1.b.string
    print(type(comment))
    print(comment)


def x_traversal():
    """
    下行遍历
    :param demo:
    :return:
    """
    html = requests.get('https://python123.io/ws/demo.html')
    soup = BeautifulSoup(html.text, 'html.parser')
    # 子节点的列表
    print(soup.body.contents)

    # 遍历儿子节点
    for child in soup.body.children:
        print(child)

    # 遍历子孙节点
    for child in soup.body.descendants:
        print(child)


def s_traversal():
    """
    上行遍历
    :param demo:
    :return:
    """
    html = requests.get('https://python123.io/ws/demo.html')
    soup = BeautifulSoup(html.text, 'html.parser')
    # 父节点
    print(soup.title.parent)

    # 遍历先辈节点
    for parent in soup.a.parents:
        if parent is None:
            print(parent)
        else:
            print(parent.name)


def p_traversal():
    """
    平行遍历
    :param demo:
    :return:
    """
    html = requests.get('https://python123.io/ws/demo.html')
    soup = BeautifulSoup(html.text, 'html.parser')

    # 后一节点
    print(soup.a.next_sibling)

    # 前一节点
    print(soup.a.previous_sibling)

    # 遍历后续节点
    for sibling in soup.a.next_siblings:
        print(sibling)

    # 遍历前续节点
    for sibling in soup.a.previous_siblings:
        print(sibling)


def html_search():
    """
    检索 HTML 内容，提取信息
    :return:
    """
    html = requests.get('https://python123.io/ws/demo.html')
    soup = BeautifulSoup(html.text, 'html.parser')

    # 检索标签
    print(soup.find_all('a'))
    print(soup.find_all(['a', 'b']))

    # 检索标签属性
    print(soup.find_all('p', 'course'))
    print(soup.find_all(id='link1'))

    # 检索字符串
    print(soup.find_all(string='python'))


if __name__ == '__main__':
    print('running bs:')
    html_search()
