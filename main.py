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
    pass


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
