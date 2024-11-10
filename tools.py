from models.models import Fix


def icao_is_available(icao) -> bool:
    """
    Функция для проверки существования икао - кода
    :param icao: проверяемый икао код
    :return:
    """
    with open('data/ufmc_approach.dat', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        str_lines = '\n'.join(lines)
        if icao in str_lines:
            return True
        else:
            return False


#############################################################
# Функции для хэширования и работы с БД

def path_is_available(departure, arrival) -> bool:
    """
    Функция для проверки наличия пути в БД
    :param departure: icao - код
    :param arrival: icao - код
    :return:
    """
    # TODO проверка в data/paths/paths.txt
    ...


def save_to_file(file_name, data):
    """
    Функция сохранения массива в файл .csv
    :param file_name:
    :param data: массив
    :return:
    """
    with open(file_name, mode='w') as file:
        file.write('ID,FREQ,TRK,DIST,CoordsX,CoordsY,Name/Remarks\n')
        for i in data:
            file.write(f'{i.id},{i.freq},{i.trk},{i.dist},{i.xCoord},{i.yCoord},{i.name}\n')
    # TODO добавить добавление в файл paths.txt


def import_from_file(file_name) -> list[Fix]:
    """
    Функция для импорта пути из файла
    :param file_name: имя файла из которого вычленяется информация вида 'UUEE-URML.csv'
    :return: Массив из точек Fix # как в функции get_points
    """
    # TODO Добавить импортирование
    ...
