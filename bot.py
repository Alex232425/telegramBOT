from aiogram import Bot, Dispatcher, executor, types
import python_weather


#bot init

bot = Bot(token="5410421425:AAGv_w0Yo9cCdEwIM6TkxO_oQTmv0nkNADM")
dp = Dispatcher(bot)
client = python_weather.Client(format=python_weather.IMPERIAL, locale="ru-ru")

#echo

@dp.message_handler()
async def echo(message: types.Message):
    weather = await client.find(message.text)

    celsius = round((weather.current.temperature - 32) / 1.8)


    resp_msg = weather.location_name + "\n"
    resp_msg += f"Текущая температура: {celsius} \n"
    resp_msg += f"Состояние погоды: {weather.current.sky_text}"

    await message.answer(resp_msg)

    await client.close()



#run long-polling

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)


