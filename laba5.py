#Котуранова Мария Сергеевна 408879
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