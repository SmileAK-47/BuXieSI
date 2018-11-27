#coding :utf - 8
import requests
from bs4 import BeautifulSoup

r = requests.get("http://www.cnblogs.com/yoyoketang/")
#
blog = r.content
# print(blog.decode())

soup = BeautifulSoup(blog,"html.parser")

times = soup.find_all(class_= "dayTitle")
title  = soup.find_all(class_="postTitle")
descs = soup.find_all(class_="postCon")
for i, j , k in zip(times,title,descs):
    print(i.a.string)
    print(j.a.string)
    print(k.div.contents[0])
    print("")
