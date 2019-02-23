import requests,time
import sys,io
from bs4 import BeautifulSoup
 #bu kod olmasa yerli saytlari karakter tanimir: https://stackoverflow.com/questions/14887829/parsing-errors-with-beautifulsoup4-python-3-3 ve https://stackoverflow.com/questions/20205455/how-to-correctly-parse-utf-8-encoded-html-to-unicode-strings-with-beautifulsoup
while True:
    print("Oxu.az Saytindan xeberler yuklenir... ")
    url="http://oxu.az"
    istek=requests.get(url)
    icerik=istek.content
    soup=BeautifulSoup(icerik,"html5lib",from_encoding="azeri") #
    #a=soup.prettify()#.encode("utf-8",'ignore')
    haberler2=soup.find_all("div",{"class":"title"})
    haberler=soup.find_all("div",{"class":"stats-i-container stats_views"})#.get("href") #list kimi verir butun a/p/div taglarini html-deki {"class":"haberler-title"}
    linkler=soup.find_all("a",{"class":"news-i-inner"})
    sayi=1
    stat=[int(i.text) for i in haberler]    #i.text string verdiyi ucun sort() olmur ona gore int edirem
    #stat.sort(reverse=True)
    print ('#',' Stat','   Baslig')
    for x,y in zip(stat,haberler2):         #listi iterate edirik
        print(sayi,"-",x,"-",y.text)           #a/p tag-in icindeki textleri goturur
        sayi+=1
    #for i in haberler,stat:
      #  print(i)
    #print(zip(stat,haberler2))
    sayigir=input("Haber sayisini girin: ")
    #print (haberler[str(sayigir-1)])
    topnews=requests.get(url+linkler[int(sayigir)-1].get('href')).content
    soup2=BeautifulSoup(topnews, "html.parser")
    print(soup2.script.clear())
    newstext=soup2.find('div', class_= 'news-inner') #soup2.find('div', {'class': 'news-inner'})
    newstext.script.clear()
    print(newstext.text)
    time.sleep(0.5)
input("nese yaz")
