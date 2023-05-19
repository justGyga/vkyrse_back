import json
import requests
from bs4 import BeautifulSoup as bs
from my_json_lib import *

def parser_news_data():
    result = []
    URL_TEMPLATE = "https://tusur.ru/ru/novosti-i-meropriyatiya/novosti"
    date = requests.get(URL_TEMPLATE)
    soup = bs(date.text, "html.parser")

    newsSours = soup.find_all('h1')
    for el in newsSours:
        r={}
        if el.find('a'):
            r['title'] = el.find('a').text
            r['href'] =  'https://tusur.ru' + el.a.get("href")
            result.append(r)

    imgSours = soup.find_all('div', class_='news-page-list-item-img')
    i=0
    for el in imgSours:
        r={}
        r['img'] = el.find('img').get('src')
        result[i].update(r)
        
    data_to_json(result,'news.json')
    
    return result

def parser_news():
    result = []
    URL_TEMPLATE = "https://tusur.ru/ru/novosti-i-meropriyatiya/novosti"
    date = requests.get(URL_TEMPLATE)
    soup = bs(date.text, "html.parser")

    newsSours = soup.find_all('h1')
    for el in newsSours:
        r={}
        if el.find('a'):
            r['title'] = el.find('a').text
            r['href'] =  'https://tusur.ru' + el.a.get("href")
            result.append(r)

    imgSours = soup.find_all('div', class_='news-page-list-item-img')
    i=0
    for el in imgSours:
        r={}
        r['img'] = el.find('img').get('src')
        result[i].update(r)
        
    data_to_json(result, 'news.json')