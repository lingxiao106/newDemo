import requests
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import xlwt

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'
}
c = 1
f = xlwt.Workbook()
sheet1 = f.add_sheet('3D', cell_overwrite_ok=True)
row0 = ["人气排名","人气值","游戏名称"]

for j in range(0, len(row0)):
    sheet1.write(0, j, row0[j])

for b in range(256):
    if b == 0 :
        continue;
    response = requests.get("http://www.doyo.cn/danji/list/100/3?p= %d" % b,headers).text
    con = BeautifulSoup(response, "html.parser");
    for i in con.find_all("a"):

        try:
            if i.img != None:
                a = i.find(class_="info").string
                sheet1.write(c,0,c)
                sheet1.write(c,1,a)
                sheet1.write(c,2,i.get("title"))
                # print(a + "\t\t游戏名称：" + i.get("title"))
                print(c)
                c += 1
        except:
            print()
        b += 1
f.save("Game.xls")
