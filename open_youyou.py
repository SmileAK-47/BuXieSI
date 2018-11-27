#coding:utf-8
from bs4 import BeautifulSoup
import os
yoyo = open("youyou.html",encoding="utf-8")
# print(yoyo.read())
soup =  BeautifulSoup(yoyo,"html.parser")
#print(soup.prettify())

tag1 = soup.head
print(tag1.name)

#<title tag
tag2 = soup.title
print(tag2.name)

#如果有多个相同的标签  返回是第一个
tag3 = soup.a
print(tag3)
