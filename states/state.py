from aiogram.dispatcher.filters.state import State, StatesGroup


class UserState(StatesGroup):
    yer_kvadratura = State()
    contact = State()
    choose_language = State()
    change_language = State()
    change_fullname = State()
    change_phone_number = State()
    yer_kategoriya = State()
    yer_tuman = State()


class QuruqYerState(StatesGroup):
    sotix = State()
    lokatsiya = State()
    kanalga_yuborish = State()

class Uchastka(StatesGroup):
    sotix = State()
    lokatsiya = State()
    xona = State()
    ha_yoki_yoq = State()
    remont = State()


class AdminState(StatesGroup):
    admin = State()
    tuman = State()
    kategoriya = State()
    narx = State()
    change_language = State()
