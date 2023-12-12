#Котуранова Мария Сергеевна 408879

#1 Задание
import requests
import json

city = 'Санкт-Петербург'

url = ('https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347')

weather_data = requests.get(url).json()
weather_data_structure = json.dumps(weather_data, indent=2)

temperature = round(weather_data['main']['temp'])
humidity=round(weather_data['main']['humidity'])
pressure=round(weather_data["main"]["pressure"])

print('Сейчас в городе', city, str(temperature), 'градусов')
print('Влажность в городе',  str(humidity), '%')
print('Давление в городе',  str(pressure), 'hPa')

#2 Задание
#сайт: https://rickandmortyapi.com/

import requests
import json

while True:
    fact = input('1 - characters, 2 - locations, 3 - episodes, 0 - exit: ')
    match fact:
        case '1':
            idi = input('Enter the id: ')
            response = requests.get(f'https://rickandmortyapi.com/api/character/{idi}')
            data = dict(response.json())
            ind = ['id','name', 'status','gender','url','image', "episode"]
            for x in range (len(ind)):
                print(ind[x],':', data[ind[x]])
        case '2':
            idi = input('Enter the id: ')
            response = requests.get(f'https://rickandmortyapi.com/api/location/{idi}')
            data = dict(response.json())
            ind = ['id', 'name', 'type', 'dimension', 'url']
            for x in range (len(ind)):
                print(ind[x],':', data[ind[x]])
        case '3':
            idi = input('Enter the id: ')
            response = requests.get(f'https://rickandmortyapi.com/api/episode/{idi}')
            data = dict(response.json())
            ind = ['id', 'name', 'air_date', 'episode', 'url']
            for x in range(len(ind)):
                print(ind[x], ':', data[ind[x]])
        case '0':
            break
        case _:
            print("Wrong type")
