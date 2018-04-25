import requests,bs4,webbrowser

import binwrite

inputstr = input("enter book name: ")
i = inputstr.strip().split()
ans = '+'.join(i)
print(ans)

#SEARCH FOR BOOK
res = requests.get("https://www.gutenberg.org/ebooks/search/?query=" +ans)

#webbrowser.open("https://www.gutenberg.org/ebooks/search/?query=" +ans)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'lxml')
eles = soup.select('li.booklink > a.link')
lnk = 0
m = 9999
for e in eles:
    n = e.get("accesskey")
    n = int(n[0])
    print(n, end = " ")
    lnk = e.get("href")
    no = lnk.split('/')
    print(no[2])
lnk = eles[0].get("href")
print("reached")
no = lnk.split('/')
res2 = requests.get("http://www.gutenberg.org/files/"+no[2]+"/"+no[2]+"-0.txt")

#webbrowser.open("http://www.gutenberg.org/files/"+no[2]+"/"+no[2]+"-0.txt")

with open("t1.txt","wb") as fp:
    fp.write(res2.content)

binwrite.main()

import os
orig = os.path.getsize("t1.txt")
print(" Original size : ", orig , "bytes")
compr = os.path.getsize("comp.bin")
print(" Compressed size : ", compr , "bytes")
print("\n Compression ratio : ", orig/compr , "\n")