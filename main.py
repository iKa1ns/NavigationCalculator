import requests


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
            print(r.text)
            return r
    except Exception as e:
        print(e)


print(get_response('uuee', 'urml'))


def get_points(response: requests.Response) -> list[str]:
    """
    Функция для парсинга html страницы и формирования массива точек
    :param response: полученный отклик
    :return: массив точек (fix)
    """
    pass


def main():
    departure = input()
    arrival = input()
    print(get_points(get_response(departure, arrival)))
