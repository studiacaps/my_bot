import requests
from pprint import pprint
from config import open_weather_token


def get_weather(city, open_weather_token):
try:
r = requests.get(
f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
)
data = r.json()
#pprint(data)

city = data['name']
weather_now = data['main']['temp']
wind_speed = data['wind']['speed']
print(f'Погода в : {city}\nТемпература: {weather_now} C°\nСкорость ветра: {wind_speed} м/с')


except Exception as ex:
print(ex)
print('Проверьте название города')

def main():
city = input('Введите город: ')
get_weather(city, open_weather_token)

if __name__ == '__main__':
main()