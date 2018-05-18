#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author:lz 
@file: start.py 
@time: 2018/05/18   17：48 
"""
#启动命令行
from scrapy import cmdline
#执行终端语言
cmdline.execute("scrapy crawl qsbk_spider".split())