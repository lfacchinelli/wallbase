from bs4 import BeautifulSoup
import requests
import urllib

r = requests.get("http://wallbase.cc/collection/29053")

data = r.text

soup = BeautifulSoup(data)

for link in soup.find_all('a', target="_blank"):
    url = link.get('href')
    cortado = url.split("/")
    urlf = "http://wallpapers.wallbase.cc/rozne/wallpaper-" +cortado[4] + ".jpg"
    urllib.urlretrieve(urlf, "/Users/usuario/Pictures/wallpapers-mac/wallpaper" +cortado[4] + ".jpg")
    
    