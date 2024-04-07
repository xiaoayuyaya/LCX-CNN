#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import os
import glob


def spiderweb(start_url, filepath):
    os.system('scrapy crawl superspider -a start_url=\'%s\' -a output_file=\'%s\'' % (start_url, filepath))


def main(webset):
    standard_webset = []
    for url in webset:
        url = re.sub('\s', '', url)
        if not url.startswith('http://') and not url.startswith('https://'):
            url = 'http://' + url
        standard_webset.append(url)
    download_path = {};
    noconnet_web = []
    for numb, web in enumerate(standard_webset):
        filepath = '../Download/%d.html' % numb
        spiderweb(web, filepath)
        if os.path.exists(filepath):
            print 'filepath=%s' % filepath
            download_path[web] = filepath[3:]
        else:
            noconnet_web.append(web)
    return download_path, noconnet_web


def check_linked():
    return True if os.system('ping -c www.baidu.com') else False

# 清理下载文件夹
def clear_download():
    dirpath = 'Download/.'  # 指定下载文件夹路径
    files = glob.glob(os.path.join(dirpath, '*.*'))
    for file in files:
        os.remove(file)
