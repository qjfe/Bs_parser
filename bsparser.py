#-*-coding:utf-8-*-
import sys, os
import mechanize
from bs4 import BeautifulSoup

br = mechanize.Browser()
br.set_handle_robots(False)
resp = br.open("http://shop.skvot.com/catalog/summer/skateboarding/?SHOWALL_1=1")
html = resp.read()

soupn = BeautifulSoup(html)


name = soupn.findAll("div", { "class" : "daydeal-title" })
price = soupn.findAll("div", { "class" : "price" })

print_zn = (name, price)


save = open('otchet.txt', 'w+')
save.write(str(print_zn))
save.close()