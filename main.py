from time import sleep
from urllib import request

image_urls = []
with open("data/data.txt",'r') as f:
    image_urls = f.readlines()

i = 1
for url in image_urls:
    print(i)
    downloaded_img = request.urlopen(url)
    path = "images/"+str(i + 1)+".png"
    f = open(path, mode='wb')
    f.write(downloaded_img.read())
    downloaded_img.close()
    f.close()
    i = i + 1
    sleep(1)
