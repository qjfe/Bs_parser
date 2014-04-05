import mechanize
from bs4 import BeautifulSoup

br = mechanize.Browser()

resp = br.open("http://ebay.com")
html = resp.read()
print html