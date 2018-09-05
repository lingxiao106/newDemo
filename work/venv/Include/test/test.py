import requests

from PIL import Image

from bs4 import BeautifulSoup

from io import BytesIO

import os

response = requests.get("http://www.jj20.com/bz/zrfg/xsxj/23498.html").text

con = BeautifulSoup(response,"html.parser");
b = 1;
for i in con.find_all("img"):

    try:
        # res = requests.get(,timeout=0)
        image = Image.open(BytesIO(i.get("src")))
        image = image.convert("RGB")
        image.save('D:/9.jpg')
    except:
        print()
    # try:
    #     file = i.get("src")
    #     if (not file):
    #         continue
    #     if (".jpg" in file):
    #         urllib.request.urlretrieve(file, 'D:\\file\\2\%s.jpg' % b)
    #     if (".png" in file):
    #         urllib.request.urlretrieve(file, 'D:\\file\\2\%s.png' % b)
    # except:
    #     print()
    b += 1
    print(i.get("src"))



