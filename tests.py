import unittest

import requests

from main import get_response, get_points


class Test(unittest.TestCase):
    def test_get_response_instance(self):
        r = get_response('uuee', 'urml')
        self.assertIsInstance(r, requests.models.Response, 'get_responce: Неверный тип выходных данных')

    def test_get_points_instance(self):
        r = get_response('uuee', 'urml')
        arr = get_points(r)
        self.assertIsInstance(arr, list, 'get_points: Неверный тип выходных данных')

    def test_get_points_objs_instance(self):
        r = get_response('uuee', 'urml')
        arr = get_points(r)
        arr = [isinstance(i, str) for i in arr]
        self.assertTrue(all(arr), 'get_points: Массив должен состоять только из строк')

    def test_fixes(self):
        self.assertListEqual(get_points(get_response('UUEE', 'UUDD')), ['UUEE', 'UUDD'],
                             'get_points: Неправильный набор точек')
        self.assertListEqual(get_points(get_response('UUDD', 'UUWW')), ['UUDD', 'UUWW'],
                             'get_points: Неправильный набор точек')
        self.assertListEqual(get_points(get_response('UUWW', 'UUBW')), ['UUWW', 'UUBW'],
                             'get_points: Неправильный набор точек')
