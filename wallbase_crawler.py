from bs4 import BeautifulSoup
import requests
import urllib
import random
from os import path
USER_AGENTS = [
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
    'Opera/9.25 (Windows NT 5.1; U; en)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.142 Safari/535.19',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:11.0) Gecko/20100101 Firefox/11.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:8.0.1) Gecko/20100101 Firefox/8.0.1',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.151 Safari/535.19'
]

# Wallbase's URL to crawl and download Wallpaper
HEADERS = { 'User-Agent' : random.choice(USER_AGENTS) }
folder = "/Users/lucianofacchinelli/Documents/wallbase/" #Local folder to store images

#Based in an Url , get the data
def get_data(baseurl):
    r = requests.get(baseurl, headers=HEADERS)
    data = r.text
    soup = BeautifulSoup(data,features="html.parser")
    return soup

#Crawl the previous data and download each wallpaper (if not exist previosluy)
def crawl_data (soup):
    for link in soup.find_all('a', target="_blank"):
        url = link.get('href')
        cortado = url.split("/")
        if cortado[2] == "wallhaven.cc":
            urla = "http://w.wallhaven.cc/full/" + cortado[4][:2] + "/wallhaven-" + cortado[4] +".jpg"
            with open(folder + cortado[4] + ".jpg", 'wb') as f:
                f.write(requests.get(urla).content)
    
for urls in baseurls:    
    origen = get_data(urls)
    crawl_data(origen)    
