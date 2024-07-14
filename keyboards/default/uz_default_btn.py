from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

til_tanlash = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🇺🇿 O'zbekcha"),
            KeyboardButton(text="🇷🇺 Русский")
        ],
        [
            KeyboardButton(text="Ortga ◀️"),
        ]
    ],
    resize_keyboard=True
)

uz_tel_raqam = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📱 Telefon raqamni yuborish", request_contact=True)
        ],
    ],
    resize_keyboard=True
)
uz_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Uyingizni narxlash 💲"),
        ],
        [
            KeyboardButton(text="Sozlamalar ⚙️"),
        ],
    ],
    resize_keyboard=True
)

uz_settings = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Tilni o`zgartirish 🌎"),
        ],
        [
            KeyboardButton(text="F.I.Sh o'zgartirish 📝"),
            KeyboardButton(text="Telefon raqamni o'zgartirish 📝"),
        ],
        [
            KeyboardButton(text="Ortga ◀️"),
        ],
    ],
    resize_keyboard=True
)

uz_kategoriya = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Uchastka"),
            KeyboardButton(text="Quruq Yer"),
        ],
        [
            KeyboardButton(text="PenHouse"),
            KeyboardButton(text="TaunHouse"),
        ],
        [
            KeyboardButton(text="Evro Dom"),
            KeyboardButton(text="Kvartira"),
        ],
        [
            KeyboardButton(text="Ortga ◀️"),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

uz_ortga = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Ortga ◀️")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

uz_tumanlar_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Bektemir"),
            KeyboardButton(text="Olmazor"),
        ],
        [
            KeyboardButton(text="Uchtepa"),
            KeyboardButton(text="Chilonzor"),
        ],
        [
            KeyboardButton(text="Sergeli"),
            KeyboardButton(text="Shayxontohur"),
        ],
        [
            KeyboardButton(text="Yakkasaroy"),
            KeyboardButton(text="Yangihayot"),
        ],
        [
            KeyboardButton(text="Yashnobod"),
            KeyboardButton(text="Mirobod"),
        ],
        [
            KeyboardButton(text="MirzoUlugbek"),
            KeyboardButton(text="Yunusobod"),
        ],
        [
            KeyboardButton(text="Ortga ◀️"),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

ok_no = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Ha ✅"),
            KeyboardButton(text="Yoq ❌"),
        ],
        [
            KeyboardButton(text="Ortga ◀️"),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

ok_no = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Ha ✅"),
            KeyboardButton(text="Yoq ❌"),
        ],
        [
            KeyboardButton(text="Ortga ◀️"),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
