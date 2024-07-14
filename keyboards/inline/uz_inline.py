from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import callback_data

uz_remont_narx = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1000$ 💵", callback_data="1000"),
            InlineKeyboardButton(text="10.000$ 💵", callback_data="10000"),
        ],
        [
            InlineKeyboardButton(text="20.000$ 💵", callback_data="20000"),
            InlineKeyboardButton(text="30.000$ 💵", callback_data="30000"),
        ],
        [
            InlineKeyboardButton(text="40.000$ 💵", callback_data="40000"),
            InlineKeyboardButton(text="50.000$ 💵", callback_data="50000"),
        ],
        [
            InlineKeyboardButton(text="60.000$ 💵", callback_data="60000"),
            InlineKeyboardButton(text="70.000$ 💵", callback_data="70000"),
        ],
        [
            InlineKeyboardButton(text="80.000$ 💵", callback_data="80000"),
            InlineKeyboardButton(text="90.000$ 💵", callback_data="90000"),
        ],
        [
            InlineKeyboardButton(text="100.000$ 💵", callback_data="100000"),
        ]
    ]
)

tasdiqlash_admin = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("Tasdiqlash ✅", callback_data="tasdiqlash"),
            InlineKeyboardButton("Отказ ❌", callback_data="rad_etish")
        ]
    ]
)
