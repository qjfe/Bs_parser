#-*-coding:utf-8-*-
import sys, os
import mechanize
from bs4 import BeautifulSoup

#soupn = BeautifulSoup(html)
#desc = soupn.findAll("a", { "class" : "name" })

br = mechanize.Browser()
br.set_handle_robots(False)
resp = br.open("http://www.destroyshop.ru/deck/catalogue.html")
html = resp.read()

soupn = BeautifulSoup(html)


name = soupn.findAll("div", { "class" : "name" })
price = soupn.findAll("span", { "class" : "price" })

print_zn = (name, price)


save = open('otchet.txt', 'w+')
save.write(str(print_zn))
save.close()