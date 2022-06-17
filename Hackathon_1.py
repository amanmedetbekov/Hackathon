from settings import settings
import requests
import json


class Car:
    headers={"Authorization": settings.TOKEN, "Content-Type": "application/json"}



    def create(self):  #для создания записей
        print('Создание записи')
        data =  {'fields': {
            'марка': input('Введите марку '),
            'модель': input('Укажите модель: '),
            'год выпуска': input('Укажите год выпуска: '),
            'объем двигателя': (input('Укажите объем двигателя: ')),
            'цвет': input('Укажите цвет: '),
            'тип кузова': input('Укажите тип кузова: '),
            'пробег': input('Укажите пробег: '),
            'цена': input('Укажите цену: '),
        },
            "typecast": True

        }
        data = json.dumps(data)
        req = requests.post(url=settings.get_url(), headers=Car.headers, data=data)
        print('Запись создана')
        return req.text
    

    def listing(self):   #для получения списка записей
        print('\nПолучение списка записей')
        req = requests.get(url = settings.get_url(), headers=Car.headers)
        return req.text


    
    def retrieve(self):   #для получения одной 
        print('\nПолучение одной записи')
        id_ = input('Введите ID записи: ')
        obj = requests.get(f'{settings.get_url()}', headers=Car.headers).json()
        for i in obj['records']:
            if id_ == i['id']:
                req = requests.get(f'{settings.get_url()}{id_}', headers=Car.headers)
                return req.text
        return 'Такого ID нет'


    def update(self):    #для обновления записей
        print('\nОбновление записи')
        id_ = input('Введите ID изменяемой записи: ')
        obj = requests.get(settings.get_url(), headers=Car.headers).json()
        for i in obj['records']:
            if id_ == i['id']:
                data =  {'fields': {
                    'марка': input('Введите марку: ') or obj['fields']['марка'],
                    'модель': input('Укажите модель: ') or obj['fields']['модель'],
                    'год выпуска': input('Укажите год выпуска: ') or obj['fields']['год выпуска'],
                    'объем двигателя': (input('Укажите объем двигателя: ')) or obj['fields']['объем двигателя'],
                    'цвет': input('Укажите цвет: ') or obj['fields']['цвет'],
                    'тип кузова': input('Укажите тип кузова: ') or obj['fields']['тип кузова'],
                    'пробег': input('Укажите пробег: ') or obj['fields']['пробег'],
                    'цена': input('Укажите цену: ') or obj['fields']['цена'],
                },
                    "typecast": True

                }
                data = json.dumps(data)
                req = requests.patch(settings.get_url()+id_, headers=Car.headers, data=data)
                return req.text
        return 'ID не найден.'


    def delete(self):    #для удаления записей
        print('\nУдаление записи')
        id_ = input('Введите ID удаляемой записи: ')
        obj = requests.get(settings.get_url(), headers=Car.headers).json()
        for i in obj['records']:
            if id_ == i['id']:
                confirmation = input('Подтвердите действие (Д/Н): ').upper()
                if confirmation == 'Д' or confirmation == 'ДА':
                    req = requests.delete(settings.get_url()+id_, headers=Car.headers)
                    return f'Удалена запись по ID {id_}'
                else:
                    return 'Отмена операции'


car = Car()

while True:
    print(f'\nC - создать запись\nG - получить по одной записи\nA - получить список записей\nU - Изменить запись\nD - Удалить запись\nS - команда стоп.')
    my_choice = input('\nВыберите метод: ').upper()

    if my_choice == 'C':  #Создание записи
        try:
            number_create = int(input('Сколько записей хотите создать? Введите количество цифрами: '))
            for i in range(number_create):                
                print(car.create())
            print(f'Успешно создано продуктов: {number_create}')
        except ValueError:
            print('Вы ввели не правильное значение')
            continue

    elif my_choice == 'G': #Получение одной записи
        number_get = int(input('Сколько записей хотите получить? Введите цифру: '))
        for i in range(number_get):
            print(car.retrieve())
        
            

    elif my_choice == 'U':  #Обновление записи
        try:
            number_update = int(input('Сколько записей хотите изменить? Введите количество цифрами: '))
            for i in range(number_update):
                print(car.update())
            print('Записи успешно изменены')
        except ValueError:
            print('Вы ввели не правильное значение')
            continue  

    elif my_choice == 'D':  #Удаление записи
        try:
            number_delete = int(input('Введите цифрами количеству удаляемых записей: '))
            for i in range(number_delete):
                print(car.delete())
            print('Записи успешно удалены')
        except ValueError:
            print('Вы ввели не правильное значение')
            continue

    elif my_choice == 'A':   #Получение списка записей
        print(car.listing())

    elif my_choice == 'S':   #Команда стоп
        break

    else:
        print(f'\ngВы ввели не правильное значение. Попробуйте еще раз.')
        continue    



