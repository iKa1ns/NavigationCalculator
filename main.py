import requests
import re
from bs4 import BeautifulSoup as Bs


def get_response(departure, arrival) -> requests.Response:
    """
    Функция для запроса
    :param departure: ICAO отправления
    :param arrival:ICAO прибытия
    :return:
    """
    # Подсказка: для запроса использовать POST запрос на https://rfinder.asalink.net/free/autoroute_rtx.php
    # с параметрами, указанными в options.txt, в которых вместо uuee и urml использовать входные параметры этой функции
    # https://pythonru.com/biblioteki/kratkoe-rukovodstvo-po-biblioteke-python-requests, "Передача параметров в URL"
    url = 'https://rfinder.asalink.net/free/autoroute_rtx.php'
    try:
        r = requests.post(url, data={'dbid': '2410',
                                     'easet': 'Y',
                                     'ic1': '',
                                     'ic2': '',
                                     'id1': departure,
                                     'id2': arrival,
                                     'k': '1233505483',
                                     'lvl': 'B',
                                     'maxalt': 'FL330',
                                     'minalt': 'FL330',
                                     'nats': 'R',
                                     'rnav': 'Y',
                                     'usesid': 'Y',
                                     'usestar': 'Y'})
        if r.status_code == 200:
            return r




    except Exception as e:
        print(e)


get_response('uuee', 'urml')


def get_points(r) -> list[str]:
    """
    Функция для парсинга html страницы и формирования массива точек
    :param response: полученный отклик
    :return: массив точек (fix)

    """
    arr0 = []
    soup = Bs(r.text, 'html.parser')
    table = soup.findAll('pre')
    for i in range(len(table)):
        arr0.append(table[i].text)
    arr = []
    result = re.finditer(r'[A-Z]+(\s{2,})\d', r.text)
    for i in result:
        arr.append(i.group())
    arr2 = []
    for i in arr:
        arr2.append(re.findall('[A-Z]{1,}', i))
    arr3 = []
    for i in arr2:
        arr3.append(''.join(i))
    print(arr3)


r = get_response('uuee', 'urml')
arr = get_points(r)
print(arr)

# def main():
#     departure = input()
#     arrival = input()
#     print(get_points(get_response(departure, arrival)))
