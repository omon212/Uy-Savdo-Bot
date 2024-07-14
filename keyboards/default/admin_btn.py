from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

admin_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Statistika 📊 "),
            KeyboardButton(text="Yer maydon narxlari 🏘")
        ],
        [
            KeyboardButton(text="Yer maydon narxlarni qo'shish 🏘"),
            KeyboardButton(text="Tilni o`zgartirish 🌎")
        ]
    ],
    resize_keyboard=True
)
ru_admin_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Статистика 📊"),
            KeyboardButton(text="Цены на земельные участки 🏘")
        ],
        [
            KeyboardButton(text="Добавить цены на земельные участки 🏘"),
            KeyboardButton(text="Изменить язык 🌎")
        ]
    ],
    resize_keyboard=True
)
