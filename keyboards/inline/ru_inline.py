from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ru_tasdiqlash_admin = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("Подтверждение ✅", callback_data="tasdiqlash_ru"),
            InlineKeyboardButton("Отказ ❌", callback_data="rad_etish_ru")
        ]
    ]
)
