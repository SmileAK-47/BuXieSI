# coding:utf-8
from bs4 import BeautifulSoup
import requests
r = requests.get("https://www.qiushibaike.com/")
qiubai = r.content
soup = BeautifulSoup(qiubai, "html.parser")
duanzi = soup.find_all(class_="content")
for i in duanzi:
# tag 的 .contents 属性可以将 tag 的子节点以列表的方式输出
    duan = i.span.contents # 取第一个
    # print(type(duan))
    # print(type(duan[1]))
    # filter(lambda x: x != '<br/>', duan)
    # print(''.join(duan))
    # print (duan)
    # print (duan)
    # break;
    res = list(filter(lambda x : isinstance(x, str), duan));
    print('\n'.join(res))

# def sas(x):
#     return isinstance(x, str);