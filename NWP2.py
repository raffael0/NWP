import subprocess
from datetime import date
from bs4 import BeautifulSoup 
import urllib.request as urllib2 
import re
import wget
reference_date=date(2020, 3, 8)
reference_number=200308
actual_number=(date.today()-reference_date).days


html_page=urllib2.urlopen("https://apod.nasa.gov/apod/astropix.html")
soup=BeautifulSoup(html_page)
for link in soup.findAll('a'):
    if  link.get('href').endswith('.png'):
        wget.download("https://apod.nasa.gov/apod/"+link.get('href'),"test.png")
        print("asdfaf")
