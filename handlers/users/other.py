from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp


# Эхо хендлер, куда летят текстовые сообщения без указанного состояния
@dp.message_handler(state=None)
async def other_things(message: types.Message):
    await message.answer("Я тебя не понимаю 😢")


# Эхо хендлер, куда летят ВСЕ сообщения с указанным состоянием
@dp.message_handler(state="*", content_types=types.ContentTypes.ANY)
async def other_things_state(message: types.Message, state: FSMContext):
    state = await state.get_state()
    await message.answer("Я тебя не понимаю 😢")
