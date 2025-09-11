# Создать список (автосалон), состоящий из словарей (машина). Словари должны содержать как минимум 5 полей
# (например, номер, модель, год выпуска, ...). В список добавить хотя бы 10 словарей.
# Конструкция вида:
# cars = [{"id":123456, "model":"Mercedes-Benz", "year": 2019, ...} , {...}, {...}, ...].
# Реализовать функции:
# – вывода информации о всех машинах;
# – вывода информации о машине по введенному с клавиатуры номеру;
# – вывода количества машин, моложе введённого года;
# – обновлении всей информации о машине по введенному номеру;
# – удалении машины по номеру.
# Провести тестирование функций.

import traceback

cars = [{'id': '1', 'model': 'BMW 1 SERIES', 'year': '2008', 'generations': '5'},
        {'id': '2', 'model': 'BMW 2 SERIES', 'year': '2013', 'generations': '2'},
        {'id': '3', 'model': 'BMW 3 SERIES', 'year': '2003', 'generations': '6'},
        {'id': '4', 'model': 'BMW 4 SERIES', 'year': '2013', 'generations': '3'},
        {'id': '5', 'model': 'BMW I3', 'year': '2013', 'generations': '2'},
        {'id': '6', 'model': 'BMW I8', 'year': '2013', 'generations': '2'},
        {'id': '7', 'model': 'BMW M1', 'year': '2010', 'generations': '1'},
        {'id': '8', 'model': 'BMW M2', 'year': '2018', 'generations': '1'},
        {'id': '9', 'model': 'BMW X1', 'year': '2009', 'generations': '3'},
        {'id': '10', 'model': 'BMW X2', 'year': '2016', 'generations': '2'}]


def list_info():
    return cars


def get_info(id_num):
    for element in cars:
        if element['id'] == id_num:
            return element
            break


def get_special_info(year_num):
    count = 0
    for element in cars:
        if int(element['year']) < year_num:
            count = count + 1
    return count


def set_info(id_num):
    for element in cars:
        if element['id'] == id_num:
            element['model'] = 'BMW 5 SERIES'
            element['year'] = '1997'
            element['generations'] = '6'
            return element


def delete_info(id_num):
    for element in cars:
        if element['id'] == id_num:
            cars.remove(element)
            return cars
            break


# Тесты
try:
    assert list_info() == cars
    assert get_info('10') == {'id': '10', 'model': 'BMW X2', 'year': '2016', 'generations': '2'}
    assert get_special_info(2013) == 4
    assert set_info('1') == {'id': '1', 'model': 'BMW 5 SERIES', 'year': '1997', 'generations': '6'}
    assert delete_info('2') == \
           [{'id': '1', 'model': 'BMW 5 SERIES', 'year': '1997', 'generations': '6'},
            {'id': '3', 'model': 'BMW 3 SERIES', 'year': '2003', 'generations': '6'},
            {'id': '4', 'model': 'BMW 4 SERIES', 'year': '2013', 'generations': '3'},
            {'id': '5', 'model': 'BMW I3', 'year': '2013', 'generations': '2'},
            {'id': '6', 'model': 'BMW I8', 'year': '2013', 'generations': '2'},
            {'id': '7', 'model': 'BMW M1', 'year': '2010', 'generations': '1'},
            {'id': '8', 'model': 'BMW M2', 'year': '2018', 'generations': '1'},
            {'id': '9', 'model': 'BMW X1', 'year': '2009', 'generations': '3'},
            {'id': '10', 'model': 'BMW X2', 'year': '2016', 'generations': '2'}]
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
