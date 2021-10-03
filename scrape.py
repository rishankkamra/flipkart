import requests
import pandas as pd
import sys
from bs4 import BeautifulSoup
r = requests.get('https://www.flipkart.com/search?q=laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off')
content = r.content.decode(encoding='UTF-8')
soup = BeautifulSoup(r.content.decode(encoding='UTF-8'), "lxml")
reviews = soup.find_all('div', {"class": "_4rR01T"})
box = []
for item in reviews:
    box.append(item)
df = pd.DataFrame({'Product Name': box})
df.to_csv('products.csv', index=False, encoding='utf-8')