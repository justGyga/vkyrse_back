import requests
from bs4 import BeautifulSoup
from constants import *
from my_json_lib import *

def date_to_normal(string_data):
    string_data = string_data.split(" ")[-2:]

    # Преобразуй месяц в число
    return [int(string_data[0]), string_data[1], 2023]


def get_timetable(url):
    session = requests.session()
    response = session.get(url, headers=headers)

    soup = BeautifulSoup(response.text, 'html.parser')

    all_tables = soup.find('div', class_='table-responsive')

    # Удаляем две управляющие сайтом таблицы
    all_tables.select_one('table').decompose()
    all_tables.select_one('table').decompose()

    all_days = []

    for day in all_tables.find_all('table'):

        # Извлекаем дату
        day.select_one('th').decompose()
        date = date_to_normal(day.find('th').text.strip())

        day.select_one('th').decompose()
        day.select_one('th').decompose()
        day.select_one('tr').decompose()

        _Lessons = []
        _lessonID = 1
        for lesson in day.find_all('tr'):

            try:
                # Извлечение информации о паре
                # Начало пары
                time = lesson.find('th', class_='time').text.strip()[:5]

                AllLabels = lesson.find('div', class_='hidden for_print')
                # Предмет, род, аудитория, преподаватель
                discipline = AllLabels.find(
                    'span', class_='discipline').text.strip()
                kind = AllLabels.find('span', class_='kind').text.strip()
                auditoriums = AllLabels.find(
                    'span', class_='auditoriums').text.strip()
                group = AllLabels.find('span', class_='group').text.strip()

                # Сохранение объекта в массив
                _Lessons.append({'lessonID': _lessonID, 'time': time, 'discipline': discipline,
                                'kind': kind, 'auditoriums': auditoriums, 'group': group})
            except:
                _Lessons.append(None)
            _lessonID += 1
        all_days.append({'date': date, 'lessons': _Lessons})
    
    return all_days

def timetables_scrapper(filename):
    all_timetables = json_to_data(filename)
    result = {}
    for group_name, url_ in all_timetables.items():
        try:
            print(f"I'm trying to get: {group_name}")
            result[group_name] = get_timetable(url_)
        except:
            pass
    return result
