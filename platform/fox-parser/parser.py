import requests
from bs4 import BeautifulSoup
#from flask import Flask
#from flask_restful import Api, Resource

url = "https://www.foxnews.com/politics/biden-lowering-mask-cough-in-his-hand"

request = requests.get(url)
coverpage = request.content
soup1 = BeautifulSoup(coverpage, 'html.parser')
coverpage_news = soup1.find_all('p')
text = ""
for p in coverpage_news:
    text += p.get_text()
print(text)
