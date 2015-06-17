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
