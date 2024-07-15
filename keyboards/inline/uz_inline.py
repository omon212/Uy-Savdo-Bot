from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import callback_data

tasdiqlash_admin = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("Tasdiqlash ✅", callback_data="tasdiqlash"),
            InlineKeyboardButton("Отказ ❌", callback_data="rad_etish")
        ]
    ]
)
