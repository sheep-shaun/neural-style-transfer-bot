from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Список команд: ",
            "/start - Начать диалог",
            "/help - Получить справку",
            "/change_style - Изменить стиль своего изображения",
            "Если вы столкнулись с какими-то ошибками или у вас возникли какие-то вопросы, обращайтесь сюда: @Sheep_the_Shaunn")

    await message.answer("\n".join(text))
