# -*- codeing = utf-8 -*-
# @Time : 2021/1/17 15:25
# @File : BZ.py
# @Software: PyCharm


import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.bilibili.com/v/popular/rank/all")

html = response.text

soup = BeautifulSoup(html,"lxml")

a = soup.find('a',class_="title")
res = soup.find_all('a',class_="title")

num = 0
text =''
for i in res:
    num += 1
    text += '{} {}\n'.format(num,i.string)

print(text)


with open("B站排行榜.txt",'w',encoding="utf8") as fout:
    fout.write(text)