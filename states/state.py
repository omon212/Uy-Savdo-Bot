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
    remont_qancha = State()
    remont_narx = State()
    kanalga_yuborish = State()



class TaunHouse(StatesGroup):
    sotix = State()
    lokatsiya = State()
    xona = State()
    ha_yoki_yoq = State()
    remont = State()
    remont_qancha = State()
    remont_narx = State()
    kanalga_yuborish = State()



class AdminState(StatesGroup):
    admin = State()
    tuman = State()
    kategoriya = State()
    narx = State()
    change_language = State()

class EvroDom(StatesGroup):
    lokatsiya = State()
    xona = State()
    ha_yoki_yoq = State()
    remont = State()
    remont_qancha = State()
    remont_narx = State()
    kanalga_yuborish = State()

class PenHouse(StatesGroup):
    kvadratura = State()
    lokatsiya = State()
    xona = State()
    ha_yoki_yoq = State()
    remont = State()
    remont_qancha = State()
    remont_narx = State()
    kanalga_yuborish = State()

class Kvartira(StatesGroup):
    kvadratura = State()
    lokatsiya = State()
    xona = State()
    ha_yoki_yoq = State()
    remont = State()
    remont_qancha = State()
    remont_narx = State()
    kanalga_yuborish = State()