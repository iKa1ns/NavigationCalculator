import requests
from bs4 import BeautifulSoup as Bs

from models.models import Fix
from tools import icao_is_avaiable, save_to_file


def get_text_from_file():
    return open('test.html', 'r').read()


def get_response(departure: str, arrival: str) -> str:
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
            return r.text
        else:
            print(r.status_code)
    except Exception as e:
        print(e)


def get_points(html_text: str) -> list:
    """
    Функция для парсинга html страницы и формирования массива точек
    :param html_text: полученный код страницы
    :return: массив точек (fix)
    """
    soup = Bs(html_text, 'html.parser')
    table = soup.find('pre').text
    headers_split = table.split('\n')[1:-1]
    fix_arr = []
    for i in headers_split:
        i = i.split()
        if len(i) == 7:
            fix = Fix(i[0], i[1], i[2], i[3], i[4], i[5], i[6])
        else:
            fix = Fix(i[0], None, i[1], i[2], i[3], i[4], i[5])
        fix_arr.append(fix)
    return fix_arr


# TODO Сделать проверку на существование ICAO кода
def main():
    departure = input()
    if icao_is_avaiable(departure):
        arrival = input()
        if icao_is_avaiable(arrival):
            # html = get_text_from_file()
            html = get_response(departure, arrival)
            points = get_points(html)
            save_to_file('test.csv', points)
            print(points)


if __name__ == "__main__":
    main()
