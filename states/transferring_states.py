from aiogram.dispatcher.filters.state import StatesGroup, State


class TransferringState(StatesGroup):
    Q1 = State()
    Q2 = State()


class TransferringWithMyStyle(StatesGroup):
    Q1 = State()
