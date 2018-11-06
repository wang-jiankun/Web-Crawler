"""
网络爬虫 -- 正则表达式，re库
author: 王建坤
date: 2018-11-6
"""
import re


def re_func():
    """
    re 库函数使用
    :return:
    """
    string = 'HIT123456 SZ666666'
    # search函数
    match1 = re.search(r'[1-9]\d{5}', string)
    if match1:
        print('-'*20)
        # Match对象的属性和方法
        print(match1.group(0))
        print(match1.string)
        print(match1.re)
        print(match1.pos)
        print(match1.endpos)
        print(match1.start())
        print(match1.end())
        print(match1.span())
        print('-'*20)

    # match 函数
    match2 = re.match(r'[1-9]\d{5}', string)
    if match2:
        print(match2.group(0))

    # findall函数
    ls1 = re.findall(r'[1-9]\d{5}', string)
    print(ls1)

    # split函数
    ls2 = re.split(r'[1-9]\d{5}', string, maxsplit=1)
    print(ls2)

    # finditer函数
    for m in re.finditer(r'[1-9]\d{5}', string):
        if m:
            print(m.group(0))

    # sub函数
    res = re.sub(r'[1-9]\d{5}', 'number', string)
    print(res)

    # compile函数
    pat = re.compile(r'[1-9]\d{5}')
    print(pat.search(string).group(0))


if __name__ == '__main__':
    print('running regex')
    re_func()
