import sys, os
import mechanize
from bs4 import BeautifulSoup
import requests



search_url = "http://www.destroyshop.ru/deck/catalogue.html"

br = mechanize.Browser()
resp = br.open(search_url)


#br.select_form(search="submit")

#resp = br.submit()
html = resp.read()

print html

save = open('otchet.txt', 'wb+')
save.write('String')
save.close()