#conding :utf-8
import requests
import  os
from bs4 import BeautifulSoup

r = requests.get("http://699pic.com/sousuo-218808-13-1.html")
fengjing = r.content

soup = BeautifulSoup(fengjing,"html.parser")
#找出所有的标签
images = soup.find_all(class_= "lazy")
#print imagese #返回list对象

for i  in images:
    jpg_rl = i["data-original"]  #获取URL地址
    title = i["title"] #返回title名称
    print(title)
    print(jpg_rl)
    print("")
    with open(os.getcwd()+"\\jpg\\" + title + 'jpg','wb')as f:
        f.write(requests.get(jpg_rl).content)
