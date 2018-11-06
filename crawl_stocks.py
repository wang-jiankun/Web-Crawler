"""
网络爬虫 -- 实战：股票数据定向爬虫
author: 王建坤
date: 2018-11-6
"""
"""
网络爬虫 -- Scrapy 框架基础
author: 王建坤
date: 2018-11-6
"""
import requests
from bs4 import BeautifulSoup
import re


def get_html_text(url, code='utf-8'):
    """
    获取 HTML 页面内容
    :param url:
    :param code:
    :return:
    """
    try:
        r = requests.get(url)
        r.raise_for_status()
        # r.encoding = r.apparent_encoding
        # 如果事先知道编码，就不用从内容中分析编码格式，提高运行速度
        r.encoding = code
        return r.text
    except:
        return ""


def get_stocks_list(stock_list, stock_url):
    """
    东方财富接口，爬取上证、深证所有上市公司的股票代码
    :param stock_list:
    :param stock_url:
    :return:
    """
    html = get_html_text(stock_url, 'GB2312')
    soup = BeautifulSoup(html, 'html.parser')
    a = soup.find_all('a')
    for i in a:
        try:
            href = i.attrs['href']
            stock_list.append(re.findall(r's[hz]\d{6}', href)[0])
        except:
            continue


def get_stock_info(stock_list, stock_url, file_path):
    """
    百度股票接口，根据股票的代码爬取详细信息
    :param stock_list:
    :param stock_url:
    :param file_path:
    :return:
    """
    count = 0
    for stock in stock_list:
        url = stock_url + stock + ".html"
        html = get_html_text(url)
        try:
            if html == "":
                continue
            info_dict = {}
            soup = BeautifulSoup(html, 'html.parser')
            # 找到股票信息的标签
            stock_info = soup.find('div', attrs={'class': 'stock-bets'})
            # 股票信息的标签中找到股票名字
            name = stock_info.find_all(attrs={'class': 'bets-name'})[0]
            info_dict.update({'股票名称': name.text.split()[0]})
            # 股票的各种详细信息
            key_list = stock_info.find_all('dt')
            value_list = stock_info.find_all('dd')
            for i in range(len(key_list)):
                key = key_list[i].text.strip()
                val = value_list[i].text.strip()
                info_dict[key] = val
            with open(file_path, 'a', encoding='utf-8') as f:
                f.write(str(info_dict) + '\n')
                # 显示当前进度
                count = count + 1
                print("\r当前进度: {:.2f}%".format(count*100/len(stock_list)),end="")
        except:
            count = count + 1
            print("\r当前进度: {:.2f}%".format(count * 100 / len(stock_list)), end="")
            continue


def main():
    """
    爬取上市公司列表，根据列表爬取具体的信息，保存在文件中
    :return:
    """
    stock_list_url = 'http://quote.eastmoney.com/stocklist.html'
    stock_info_url = 'https://gupiao.baidu.com/stock/'
    output_file = 'E:/stocks.txt'
    stock_list = []
    get_stocks_list(stock_list, stock_list_url)
    get_stock_info(stock_list, stock_info_url, output_file)


if __name__ == '__main__':
    print('running crawl_stocks')
    main()
