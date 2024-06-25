class SearchError(Exception):
    pass

def search():
    s = input("Введите запрос: ")
    s = s.replace(' ', '')
    if s in ['1','2','3','4','5']:
        print('Запрос успешно обработан. Информация найдена!')
    else:
        raise SearchError('Запрос не найден. Ошибка 404.')

try:
    search()
except SearchError as e:
    print(e)


class TaskError(Exception):
    pass

def plus():
    a = int(input('Введите число не больше 10: '))
    if a < 10:
        c = int(a) + 10
        print('Операция выполнена успешно')
    else:
        raise TaskError('Перечитайте задание')

try:
    plus()
except TaskError as e:
    print(e)
