import json
import requests
from bs4 import BeautifulSoup as bs    

def parser_whith_data():
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
        
    with open('data.json', 'w') as outfile:
        json.dump(result, outfile)
    
    return result

def parser_without_data():
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
        
    with open('data.json', 'w') as outfile:
        json.dump(result, outfile)
    
def data_from_json():
    with open('data.json') as json_file:
        data = json.load(json_file)
    return data