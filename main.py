import requests
from bs4 import BeautifulSoup as Bs


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


def get_points(html_text: str) -> list[str]:
    """
    Функция для парсинга html страницы и формирования массива точек
    :param html_text: полученный код страницы
    :return: массив точек (fix)
    """
    soup = Bs(html_text, 'html.parser')
    table = soup.find('pre').text
    headers_split = table.split('\n')[1:-1]
    arr = [s.split()[0] for s in headers_split]
    return arr


# text = get_response('uuee', 'urml')
text = get_text_from_file()
arr = get_points(text)
print(arr)
