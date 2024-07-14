import sqlite3, asyncio
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.uz_default_btn import *
from keyboards.default.ru_default_btn import *
from keyboards.inline.uz_inline import *
from keyboards.inline.ru_inline import *
from loader import dp, bot
from utils.databace import *
from states.state import *
from collections import defaultdict
from aiogram.types import ReplyKeyboardRemove
from utils.databace import *
from ..admin.admin_panel import *
from data.config import *
from googletrans import Translator

translator = Translator()


async def translate_text(text, src='uz', dest='ru'):
    translation = translator.translate(text, src=src, dest=dest)
    return str(translation.text)


fake_data = defaultdict(dict)

uz_tumanlar_list = [
    "Bektemir",
    "Olmazor",
    "Uchtepa",
    "Chilonzor",
    "Sergeli",
    "Shayxontohur",
    "Yakkasaroy",
    "Yangihayot",
    "Yashnobod",
    "Mirobod",
    "MirzoUlugbek",
    "Yunusobod",
    "Бектемир",
    "Олмазор",
    "Учтепа",
    "Чиланзар",
    "Сергели",
    "Шайхонтохур",
    "Яккасарай",
    "Янгиҳайот",
    "Яшнобод",
    "Миробод",
    "МирзоУлугбек",
    "Юнусобод",
]


def generate_map_link(latitude, longitude):
    base_url = "https://www.google.com/maps?q="
    return f"{base_url}{latitude},{longitude}"


@dp.message_handler(CommandStart(), state="*")
async def bot_start(message: types.Message, state: FSMContext):
    global check
    await state.finish()
    check = await check_user(message.from_user.id)
    await record_stat(message.from_user.id)
    if check == None:
        fake_data[message.from_user.id]['user_id'] = message.from_user.id
        await message.answer("""
<b>Assalomu Aleykum UySavdoBot rasmiy botiga xush kelibsiz iltimos tilni tanlang!👇</b>

<b>Здравствуйте, добро пожаловать в официальный бот UySavdoBot!,Пожалуйста, выберите язык!</b>
    """, reply_markup=til_tanlash)
        await UserState.choose_language.set()
    else:
        if check[2] == "ru":
            await message.answer(f"""<b>
Добро пожаловать {check[4]} в главное меню!

Пожалуйста, выберите одну из категорий!           
           </b>""", reply_markup=ru_menu)
        else:
            await message.answer(f"""<b>
Bosh menyuga {check[4]} xush kelibsiz!

Iltimos, kategoriyalardan birini tanlang!
            </b>""", reply_markup=uz_menu)


@dp.message_handler(text="🇺🇿 O'zbekcha", state=UserState.choose_language)
async def uztil(message: types.Message, state: FSMContext):
    await record_stat(message.from_user.id)
    fake_data[message.from_user.id]['language'] = "uz"
    await message.answer("""
<b>Iltimos telefon raqamni yuborish tugmasini bosing ☎️</b>
    """, reply_markup=uz_tel_raqam)
    await state.finish()
    await UserState.contact.set()


@dp.message_handler(text="🇷🇺 Русский", state=UserState.choose_language)
async def rustil(message: types.Message, state: FSMContext):
    await record_stat(message.from_user.id)
    fake_data[message.from_user.id]['language'] = "ru"
    await message.answer("""
<b>Пожалуйста, нажмите кнопку отправить номер телефона ☎️</b>    
    """, reply_markup=ru_tel_raqam)
    await state.finish()
    await UserState.contact.set()


@dp.message_handler(content_types=types.ContentType.CONTACT, state=UserState.contact)
async def contact(message: types.Message, state: FSMContext):
    await record_stat(message.from_user.id)
    fake_data[message.from_user.id]['phone'] = str(message.contact.phone_number)
    fake_data[message.from_user.id]['fullname'] = str(message.contact.full_name)
    if fake_data[message.from_user.id]['language'] == "ru":
        await message.answer(f"""<b>
Добро пожаловать {message.from_user.full_name} в главное меню!

Пожалуйста, выберите одну из категорий!           
                   </b>""", reply_markup=ru_menu)
        await save_all_data(
            fake_data[message.from_user.id]['user_id'],
            fake_data[message.from_user.id]['language'],
            fake_data[message.from_user.id]['phone'],
            fake_data[message.from_user.id]['fullname'],
        )
        await state.finish()
    else:
        await message.answer(f"""<b>
Bosh menyuga {message.from_user.full_name} xush kelibsiz!

Iltimos, kategoriyalardan birini tanlang !
                    </b>""", reply_markup=uz_menu)
        await save_all_data(
            fake_data[message.from_user.id]['user_id'],
            fake_data[message.from_user.id]['language'],
            fake_data[message.from_user.id]['phone'],
            fake_data[message.from_user.id]['fullname'],
        )
        await state.finish()


@dp.message_handler(text=['Sozlamalar ⚙️', 'Настройки ⚙️'])
async def settings(message: types.Message):
    global settings_data
    settings_data = await check_user(message.from_user.id)
    await record_stat(message.from_user.id)
    if settings_data[2] == "ru":
        await message.answer(f"""
<b>Выберите одну из категорий ниже!</b>        
        """, reply_markup=ru_settings)
    else:
        await message.answer(f"""
<b>Quyidagi kategoriyalardan birini tanlang!</b>        
        """, reply_markup=uz_settings)


@dp.message_handler(text=['Ortga ◀️', 'Назад ◀️'], state="*")
async def back(message: types.Message, state: FSMContext):
    await record_stat(message.from_user.id)
    a = await check_user(message.from_user.id)
    if a[2] == "ru":
        await message.answer(f"""<b>
Добро пожаловать {a[4]} в главное меню!


Пожалуйста, выберите одну из категорий!           
           </b>""", reply_markup=ru_menu)
        await state.finish()
    else:
        await message.answer(f"""<b>
Bosh menyuga {a[4]} xush kelibsiz!

Iltimos, kategoriyalardan birini tanlang!
            </b>""", reply_markup=uz_menu)
        await state.finish()


@dp.message_handler(text=['Tilni o`zgartirish 🌎', 'Изменить язык 🌎'])
async def change_language(message: types.Message, state: FSMContext):
    await record_stat(message.from_user.id)
    if settings_data[2] == "ru":
        await message.answer(f"""
<b>Выберите язык, который хотите изменить!</b>        
        """, reply_markup=ru_til_tanlash)
        await UserState.change_language.set()
    else:
        await message.answer(f"""
<b>O'zgartirmoqchi bo'lgan tilingizni tanlang !</b>        
        """, reply_markup=til_tanlash)
        await UserState.change_language.set()


@dp.message_handler(state=UserState.change_language)
async def change_languagee(message: types.Message, state: FSMContext):
    await record_stat(message.from_user.id)
    if message.text == "🇺🇿 O'zbekcha":
        await update_language(message.from_user.id, "uz")
        await message.answer(f"""
<b>Til o'zgardi ✅</b>        
        """, reply_markup=uz_settings)
        await state.finish()
    else:
        await update_language(message.from_user.id, "ru")
        await message.answer(f"""
<b>Язык изменен ✅</b>        
        """, reply_markup=ru_settings)
        await state.finish()


@dp.message_handler(text=['Изменить Ф.И.О. 📝', "F.I.Sh o'zgartirish 📝"])
async def change_fullname(message: types.Message):
    global change_fname
    change_fname = await check_user(message.from_user.id)
    await record_stat(message.from_user.id)
    if change_fname[2] == "ru":
        await message.answer(f"""
<b>Введите ваше Ф.И.О.!</b>        
        """)
        await UserState.change_fullname.set()
    else:
        await message.answer(f"""
<b>Ism Familiyangizni kiriting!</b>        
        """)
        await UserState.change_fullname.set()


@dp.message_handler(state=UserState.change_fullname)
async def change_fullnamee(message: types.Message, state: FSMContext):
    await record_stat(message.from_user.id)
    if change_fname[2] == "ru":
        await update_fullname(message.from_user.id, str(message.text))
        await message.answer(f"""
<b>Ф.И.О. изменено ✅</b>        
        """, reply_markup=ru_settings)
        await state.finish()
    else:
        await update_fullname(message.from_user.id, str(message.text))
        await message.answer(f"""
<b>Ism Familiyangiz o'zgartirildi ✅</b>        
        """, reply_markup=uz_settings)
        await state.finish()


@dp.message_handler(text=['Изменить номер телефона 📝', "Telefon raqamni o'zgartirish 📝"])
async def phone(message: types.Message):
    global change_phone
    await record_stat(message.from_user.id)
    change_phone = await check_user(message.from_user.id)
    if change_phone[2] == "ru":
        await message.answer("""
<b>Введите свой номер телефона!</b>        
Например: <b>+998999999999</b>  
        """)
        await UserState.change_phone_number.set()
    else:
        await message.answer("""
<b>Telefon raqamingizni kiriting!</b>      
Masalan: <b>+998999999999</b>  
        """)
        await UserState.change_phone_number.set()


@dp.message_handler(state=UserState.change_phone_number)
async def change_phonee(message: types.Message, state: FSMContext):
    language = change_phone[2]
    phone_number = message.text
    await record_stat(message.from_user.id)
    if phone_number[0] == "+" and len(phone_number) == 13:
        number = phone_number[1:]
        await update_phone(message.from_user.id, number)
        if language == "ru":
            await message.answer("<b>Номер телефона изменен ✅</b>", reply_markup=ru_settings)
        else:
            await message.answer("<b>Telefon raqam o'zgartirildi ✅</b>", reply_markup=uz_settings)

        await state.finish()
    else:
        error_message = "<b>Номер телефона введен неверно!</b>" if language == "ru" else "<b>Telefon raqam xato kiritildi!</b>"
        await message.answer(error_message)


@dp.message_handler(text=["Uyingizni narxlash 💲", "Стоимость вашего дома 💲"])
async def narxlash(message: types.Message, state: FSMContext):
    global til
    await record_stat(message.from_user.id)
    til = await check_user(message.from_user.id)
    if til[2] == "ru":
        await message.answer(f"<b>Пожалуйста, выберите одну из следующих категорий:</b>", reply_markup=uz_tumanlar_btn)
    elif til[2] == "uz":
        await message.answer(f"<b>Iltimos, quyidagi tumanlardan birini tanlang:</b>", reply_markup=uz_tumanlar_btn)
    await UserState.yer_tuman.set()


@dp.message_handler(state=UserState.yer_tuman)
async def yer_tumanlar(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    await record_stat(user_id)
    if message.text in uz_tumanlar_list:
        text_uz = "Iltimos, quyidagi kategoriyalardan birini tanlang:"
        text_ru = await translate_text(text_uz)
        fake_data[user_id]['tuman'] = str(message.text)
        if til[2] == "ru":
            await message.answer(f"<b>{text_ru}</b>", reply_markup=uz_kategoriya)
        else:
            await message.answer(f"<b>{text_uz}</b>", reply_markup=uz_kategoriya)
        await state.finish()
        await UserState.yer_kategoriya.set()
    else:
        if til[2] == "ru":
            await message.answer(f"<b>Такого района нет ❌</b>", reply_markup=uz_tumanlar_btn)
        else:
            await message.answer(f"<b>Bunaqa tuman mavjud emas ❌/b>", reply_markup=uz_tumanlar_btn)


# --------------------QURUQ YER--------------------#

@dp.message_handler(text='Quruq Yer', state=UserState.yer_kategoriya)
async def quruq_yer(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    await record_stat(user_id)
    fake_data[user_id]['kategoriya'] = "Quruq Yer"
    if til[2] == "ru":
        await message.answer(f"<b>Отправьте пожалуйста площадь вашего {message.text}</b>")
    else:
        await message.answer(f"<b>Iltimos, {message.text}ingizning sotixini yuboring</b>")
    await state.finish()
    await QuruqYerState.sotix.set()


@dp.message_handler(state=QuruqYerState.sotix)
async def quruqyersotix(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    await record_stat(user_id)
    isnumber = message.text.isdigit()
    if isnumber == True:
        fake_data[user_id]['sotix'] = message.text
        if til[2] == "ru":
            await message.answer(f"<b>Отправьте пожалуйста геолокацию вашего {fake_data[user_id]['kategoriya']}:</b>")
        else:
            await message.answer(f"<b>Iltimos, {fake_data[user_id]['kategoriya']}ingizning joylashuvini yuboring:</b>")
        await state.finish()
        await QuruqYerState.lokatsiya.set()
    else:
        if til[2] == "ru":
            await message.answer(f"<b>Только введите номер ❌</b>")
        else:
            await message.answer(f"<b>Faqat son kiriting ❌</b>")


@dp.message_handler(content_types=types.ContentType.LOCATION, state=QuruqYerState.lokatsiya)
async def quruqyerlokatsiya(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    await record_stat(user_id)
    fake_data[user_id]['latitude'] = message.location.latitude
    fake_data[user_id]['longitude'] = message.location.longitude
    sotix_narx = await narx_qidirish(fake_data[user_id]['tuman'], fake_data[user_id]['kategoriya'])
    narx = int(sotix_narx[3]) * int(fake_data[user_id]['sotix'])
    rayon_ru = await translate_text(f"{fake_data[user_id]['tuman']}")
    link = generate_map_link(fake_data[user_id]['latitude'], fake_data[user_id]['longitude'])
    if til[2] == "ru":
        await message.answer(f"""
<b>Сухая земля 🚩</b>

<b>Район 🚩</b> {rayon_ru}
<b>Сотка 📏</b> {fake_data[user_id]['sotix']}
<b>Геолокация 📍</b> <a href="{link}">Местоположение земли</a>

<b>Цена 💰</b> <code>{narx}$</code>

<b>Хотите рекламировать этот товар на нашем канале 📣</b>
        """, reply_markup=ok_no_ru)
        await state.finish()
        await QuruqYerState.kanalga_yuborish.set()
    else:

        await message.answer(f"""
<b>Quruq Yer 🚩</b>

<b>Tuman 🚩</b> {fake_data[user_id]['tuman']}
<b>Sotix 📏</b> {fake_data[user_id]['sotix']}
<b>Geolokatsiya 📍</b> <a href="{link}">Quruq yerning joylashuvi</a>

<b>Narx 💰</b> <code>{narx}$</code>

<b>Siz ushbu mahsulotingizni bizning kanalimizga elon berishni xohlaysizmi 📣</b>
        """, reply_markup=ok_no)
        await state.finish()
        await QuruqYerState.kanalga_yuborish.set()

    @dp.message_handler(text=["Ha ✅", "Да ✅"], state=QuruqYerState.kanalga_yuborish)
    async def check_ok_no(message: types.Message, state: FSMContext):
        user_id = message.from_user.id
        chat_member = await bot.get_chat_member(CHANNEL_USERNAME, user_id)
        if chat_member.status in ['member', 'administrator', 'creator']:
            if til[2] == "ru":
                await message.answer(
                    "<b>Ваше объявление принято ✅\n\nВаше объявление будет проверено администратором в течение 24 часов</b>")
                caption_ru = f"""
<b>Сухая земля 🚩</b>

<b>Район 🚩</b> {rayon_ru}
<b>Сотка 📏</b> {fake_data[user_id]['sotix']}
<b>Геолокация 📍</b> <a href="{link}">Местоположение земли</a>

<b>Цена 💰</b> <code>{narx}$</code>                    
                """
                for admin in ADMINS:
                    await bot.send_message(admin, caption_ru, reply_markup=ru_tasdiqlash_admin)

                @dp.callback_query_handler(text="tasdiqlash_ru")
                async def tasdiqlassh(call: types.CallbackQuery):
                    await call.message.delete()
                    await bot.send_message(user_id,
                                           "<b>Ваше объявление одобрено ✅\n\nСкоро будет отправлено на канал</b>")
                    await call.bot.send_message(CHANNEL_ID, caption_ru)

                @dp.callback_query_handler(text="rad_etish_ru")
                async def rad_etishh(call: types.CallbackQuery):
                    await call.message.delete()
                    await bot.send_message(user_id,
                                           "<b>Ваше объявление отклонено ❌\n\nСпасибо за использование бота ☺</b>")
            else:
                await message.answer(
                    "<b>Sizning eloningiz qabul qilindi ✅\n\n24 soat ichida sizning eloningiz admin tomonidan tekshiriladi</b>")
                caption = f"""
<b>Quruq Yer 🚩</b>

<b>Tuman 🚩</b> {fake_data[user_id]['tuman']}
<b>Sotix 📏</b> {fake_data[user_id]['sotix']}
<b>Geolokatsiya 📍</b> <a href="{link}">Quruq yerning joylashuvi</a>

<b>Narx 💰</b> <code>{narx}$</code>                    
                """
                for admin in ADMINS:
                    await bot.send_message(admin, caption, reply_markup=tasdiqlash_admin)

                @dp.callback_query_handler(text="tasdiqlash")
                async def tasdiqlassh(call: types.CallbackQuery):
                    await call.message.delete()
                    await bot.send_message(user_id,
                                           "<b>Sizning eloningiz tasdiqlandi ✅\n\nYaqin orada kanalga yuboriladi</b>")
                    await call.bot.send_message(CHANNEL_ID, caption)

                @dp.callback_query_handler(text="rad_etish")
                async def rad_etishh(call: types.CallbackQuery):
                    await call.message.delete()
                    await bot.send_message(user_id,
                                           "<b>Sizning eloningiz tasdiqlanmadi ❌\n\nBotdan foydalananganingiz uchun rahmat ☺️</b>")
        else:
            if til[2] == "ru":
                await message.answer(f"Сначала подпишитесь на наш канал и попробуйте снова\n\n{CHANNEL_LINK}",
                                     reply_markup=ok_no_ru)
            else:
                await message.answer(
                    f"Avvalam bor bizning kanalga obuna bo'ling va qayta urinib ko'ring\n\n{CHANNEL_LINK}",
                    reply_markup=ok_no)

    @dp.message_handler(text=["Yoq ❌", "Нет ❌"], state=QuruqYerState.kanalga_yuborish)
    async def check_ok_no(message: types.Message, state: FSMContext):
        user_id = message.from_user.id
        await record_stat(user_id)
        if til[2] == "ru":
            await message.answer(f"<b>Спасибо за использование бота ☺️</b>", reply_markup=ru_menu)
        else:
            await message.answer(f"<b>Botdan foydalanganingiz uchun rahmat ☺️</b>",
                                 reply_markup=uz_menu)
