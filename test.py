#! /usr/local/bin/python3.7
# coding: UTF-8
import requests
import re
from bs4 import BeautifulSoup

url = 'https://www.biquge5200.cc/14_14621/'
response = requests.get(url)
html = response.text
title = re.findall('<title>(.*?)</title>', html, re.S)[0]#得到小说名
fb = open('%s.txt' % title, 'w', encoding='utf-8')#保存文件以小说名命名
list = re.findall('<dl>(.*?)</dl>' , html, re.S)[0]#得到整个列表
soup = BeautifulSoup(list, 'html.parser')#解析列表
print(soup)
chapter_list = soup.find_all('a')#找到列表里面所有的a标签，得到每个章节的连接和章节名
print(chapter_list)
'''
分别打印输出a标签的href和value
for link in links:
    print(link.name, link['href'], link.get_text())
'''
for chapter in chapter_list:
    chapter_url = chapter['href']
    chapter_title = chapter.get_text()
    chapter_response = requests.get(chapter_url)
    chapter_html = chapter_response.text
    chapter_soup = BeautifulSoup(chapter_html,'html.parser')
    chapter_content_list = chapter_soup.find_all('p')#小说的内容都放在p标签里面
    fb.write(chapter_title)#章节名
    fb.write('\n')
    for chapter_content in chapter_content_list:
        print(chapter_content.get_text())#打印到控制台
        fb.write(chapter_content.get_text())#写进文档里
        fb.write('\n')
    
    fb.write('\n')
    fb.write('\n')
    #exit()先打印一章，看是否出错，用exit来测试