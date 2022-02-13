from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default import menu

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.first_name}!\n\n"
                         f"Я - Neural Style Transfer бот\n\n"
                         f"Я умею менять стиль фотографии с помощью нейронных сетей\n\n"
                         f"Я могу перенести стиль с фотографии, которую ты мне отправишь\n"
                         f"Если у тебя возникнут проблемы с выбором стиля, то я могу предложить несколько стилей на выбор\n\n"
                         f"Напиши /change_style, чтобы изменить стиль своей фотографии!",
                         reply_markup=menu.start_menu)
