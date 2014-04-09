#-*-coding:utf-8-*-
import sys, os
import mechanize
from bs4 import BeautifulSoup
import requests


br = mechanize.Browser()
resp = br.open("http://www.destroyshop.ru/deck/catalogue.html")
html = resp.read()

#soup.findAll('div',{'itemprop':"name"})

soupn = BeautifulSoup(html)
desc = soupn.findAll(attrs={"class":"vi"})
desc = [0]

#print html

save = open('otchet.txt', 'w+')
save.write(str(html))
save.close()