#! /usr/bin/env python
# -*- coding:utf-8 -*-

import requests


def clear_browser():
    html_url = "http://wufazhuce.com"
    html_get = requests.get(html_url)
    html_text = html_get.text
    print html_text

if __name__ == "__main__":
    clear_browser()




    """
    bs4 demo in iPython

    In [10]: type(soup)
    Out[10]: bs4.BeautifulSoup

    In [11]: for link in soup.find_all("a"):
       ....:     print(link.get("href"))
          ....:
          http://wufazhuce.com/
          http://wufazhuce.com/one
          http://wufazhuce.com/noticias
    """
