from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

ru_tel_raqam = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📱 Отправьте номер телефона", request_contact=True)
        ],
    ],
    resize_keyboard=True
)

ru_til_tanlash = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🇺🇿 O'zbekcha"),
            KeyboardButton(text="🇷🇺 Русский")
        ],
        [
            KeyboardButton(text="Назад ◀️"),
        ]
    ],
    resize_keyboard=True
)

ru_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Стоимость вашего дома 💲"),
        ],
        [
            KeyboardButton(text="Настройки ⚙️"),
        ],
    ],
    resize_keyboard=True
)

ru_ortga = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Назад ◀️"),
        ],
    ],
    resize_keyboard=True
)


ru_settings = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Изменить язык 🌎"),
        ],
        [
            KeyboardButton(text="Изменить Ф.И.О. 📝"),
            KeyboardButton(text="Изменить номер телефона 📝"),
        ],
        [
            KeyboardButton(text="Назад ◀️"),
        ],
    ],
    resize_keyboard=True
)

ru_kategoriya = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Участок"),
            KeyboardButton(text="Сухая земля"),
        ],
        [
            KeyboardButton(text="Пентхаус"),
            KeyboardButton(text="Таунхаус"),
        ],
        [
            KeyboardButton(text="Евро Дом"),
            KeyboardButton(text="Квартира"),
        ],
        [
            KeyboardButton(text="Назад ◀️"),
        ]
    ],
    resize_keyboard=True
)

ru_tumanlar_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Бектемир"),
            KeyboardButton(text="Олмазор"),
        ],
        [
            KeyboardButton(text="Учтепа"),
            KeyboardButton(text="Чиланзар"),
        ],
        [
            KeyboardButton(text="Сергели"),
            KeyboardButton(text="Шайхонтохур"),
        ],
        [
            KeyboardButton(text="Яккасарай"),
            KeyboardButton(text="Янгиҳайот"),
        ],
        [
            KeyboardButton(text="Яшнобод"),
            KeyboardButton(text="Миробод"),
        ],
        [
            KeyboardButton(text="МирзоУлугбек"),
            KeyboardButton(text="Юнусобод"),
        ],
        [
            KeyboardButton(text="Назад ◀️"),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

ok_no_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Да ✅"),
            KeyboardButton(text="Нет ❌"),
        ],
        [
            KeyboardButton(text="Назад ◀️"),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
