import asyncio
import requests
from config import open_weather_token, tg_bot_token
from aiogram import Bot, types, Dispatcher
from aiogram.filters import CommandStart


dp = Dispatcher()

@dp.message(CommandStart())
async def main(message: types.Message):
await message.reply("Привет! Погоду в каком городе ты хочешь узнать?")


@dp.message()
async def get_weather(message: types.Message):
try:
r = requests.get(
f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric"
)
data = r.json()
# pprint(data)

city = data['name']
weather_now = data['main']['temp']
wind_speed = data['wind']['speed']
await message.reply(f'Погода в : {city}\nТемпература: {weather_now} C°\nСкорость ветра: {wind_speed} м/с')


except:
await message.reply('Проверьте название города')


async def main():
bot = Bot(token=tg_bot_token)
await dp.start_polling(bot)


if __name__ == "__main__":
asyncio.run(main())