from models.models import Fix
import csv


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
    with open('data/paths/paths.txt', 'r') as file:
        if departure in file.read() and arrival in file.read():
            return True
        else:
            return False


def save_to_file(file_name, data, departure, arrival):
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
        with open('data/paths/paths.txt', mode='w') as f:
            f.write(f'Departure: {departure}, Arrival: {arrival}\n')


def import_from_file(file_name) -> list[Fix]:
    """
    Функция для импорта пути из файла
    :param file_name: имя файла из которого вычленяется информация вида 'UUEE-URML.csv'
    :return: Массив из точек Fix # как в функции get_points
    """


    fixes = []

    with open(file_name, mode='r', newline='', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        for i in csv_reader:
            if len(i) == 7:
                id_ = i[0]
                freq = i[1]
                trk = i[2]
                dist = i[3]
                xCoord = i[4]
                yCoord = i[5]
                name = i[6]
                fix = Fix(id_, freq, trk, dist, xCoord, yCoord, name)
                fixes.append(fix)

    return fixes
