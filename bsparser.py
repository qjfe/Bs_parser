import mechanize
from bs4 import BeautifulSoup


search_url = "http://www.avito.ru/moskva/noutbuki"

br = mechanize.Browser()
resp = br.open(search_url)
#br.select_form(search="submit")

#resp = br.submit()
html = resp.read()
html = open("otchet.txt", "w,r")