from my_json_lib import *
import requests
from bs4 import BeautifulSoup
from constants import *


def get_all_urls(headers: map = headers, _facs=facs):
    session = requests.session()
    group_urls = {}
    for fac_name in _facs:
        response = session.get(
            f"https://timetable.tusur.ru/faculties/{fac_name}", headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        for group_numes in soup.find_all('ul', class_='list-inline'):
            for a in group_numes.find_all('a', href=True):
                url = a['href'][(11+len(fac_name)):]
                group_urls[url[8:]
                           ] = f"https://timetable.tusur.ru/faculties/{fac_name}{url}"
    return group_urls
