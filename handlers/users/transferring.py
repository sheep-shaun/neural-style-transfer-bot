from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text, Command

from loader import dp, bot

from states.transferring_states import TransferringState, TransferringWithMyStyle

from keyboards.default import menu, image_selection

from nst import transferring


@dp.message_handler(Command("change_style"), state=None)
async def start_transferring(message: types.Message):
    await message.answer("Выбери источник изображения стиля\n\n"
                         "Ты можешь отправить свою фотографию стиля "
                         "или выбрать фотографию стиля из тех, которые я тебе предложу",
                         reply_markup=menu.selection_menu)


@dp.message_handler(Text(equals=["Отправить свой стиль"]), state=None)
async def transferring_with_your_photo(message: types.Message):
    await message.answer("Отправь фото стиля", reply_markup=types.ReplyKeyboardRemove())
    await TransferringState.Q1.set()


@dp.message_handler(content_types=["photo"], state=TransferringState.Q1)
async def get_style_photo(message: types.Message):
    await message.photo[-1].download('data/images/style.jpg')
    await message.answer("Отправь фото, на которое хочешь перенести свой стиль")

    await TransferringState.next()


@dp.message_handler(content_types=["photo"], state=TransferringState.Q2)
async def get_content_photo(message: types.Message, state: FSMContext):
    await message.photo[-1].download('data/images/content.jpg')
    await message.answer(
        "Спасибо, остлось подождать несколько минут, пока нейронная сеть переносит стиль на твою фотографию")

    await transferring("data/images/content.jpg", "data/images/style.jpg", "data/images/output.jpg")

    await message.answer_photo(photo=open('data/images/output.jpg', 'rb').read(), reply_markup=menu.start_menu)

    await state.finish()


@dp.message_handler(Text(equals=["Выбрать стиль из предложенных"]), state=None)
async def transferring_with_suggested_photo(message: types.Message):
    media = types.MediaGroup()
    media.attach_photo(types.InputFile('data/images/Van_Gogh.jpg'), 'Винсент ван Гог - "Звездная ночь"')
    media.attach_photo(types.InputFile('data/images/Picasso.jpg'), 'Пабло Пикассо - "Сидящая обнаженная"')
    media.attach_photo(types.InputFile('data/images/autumn.jpg'), '"Осеннее одиночество"')

    await bot.send_media_group(chat_id=message.chat.id, media=media)

    await message.answer("Выбирай стиль, который тебе по душе", reply_markup=image_selection.image_selection)


@dp.message_handler(Text(equals=['1 - "Звездная ночь"']), state=None)
async def transferring_style1(message: types.Message, state: FSMContext):
    await message.answer("Отправь фото, на которое хочешь перенести стиль", reply_markup=types.ReplyKeyboardRemove())

    await TransferringWithMyStyle.Q1.set()

    await state.update_data(q1=1)


@dp.message_handler(Text(equals=['2 - "Сидящая обнаженная"']), state=None)
async def transferring_style2(message: types.Message, state: FSMContext):
    await message.answer("Отправь фото, на которое хочешь перенести стиль", reply_markup=types.ReplyKeyboardRemove())

    await TransferringWithMyStyle.Q1.set()

    await state.update_data(q1=2)


@dp.message_handler(Text(equals=['3 - "Осеннее одиночество"']), state=None)
async def transferring_style3(message: types.Message, state: FSMContext):
    await message.answer("Отправь фото, на которое хочешь перенести стиль", reply_markup=types.ReplyKeyboardRemove())

    await TransferringWithMyStyle.Q1.set()

    await state.update_data(q1=3)


@dp.message_handler(content_types=["photo"], state=TransferringWithMyStyle.Q1)
async def get_content_photo_style1(message: types.Message, state: FSMContext):
    await message.photo[-1].download('data/images/content_mystyle.jpg')
    await message.answer(
        "Спасибо, остлось подождать несколько минут, пока нейронная сеть переносит стиль на твою фотографию")

    data = await state.get_data()
    q1 = data.get("q1")

    if q1 == 1:
        await transferring("data/images/content_mystyle.jpg", "data/images/Van_Gogh.jpg",
                           "data/images/output_mystyle.jpg")
    elif q1 == 2:
        await transferring("data/images/content_mystyle.jpg", "data/images/Picasso.jpg",
                           "data/images/output_mystyle.jpg")
    elif q1 == 3:
        await transferring("data/images/content_mystyle.jpg", "data/images/autumn.jpg",
                           "data/images/output_mystyle.jpg")

    await message.answer_photo(photo=open('data/images/output_mystyle.jpg', 'rb').read(), reply_markup=menu.start_menu)

    await state.finish()
