import sqlite3, logging
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.admin_btn import admin_btn
from loader import dp
from utils.databace import narx_qoshish
from states.state import AdminState
from data.config import WORK_DIRECTORY
from collections import defaultdict
from aiogram.types import ReplyKeyboardRemove
from data.config import ADMINS
from keyboards.default.uz_default_btn import uz_tumanlar_btn, uz_kategoriya

con = sqlite3.connect(f'{WORK_DIRECTORY}/stats.db')
cur = con.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS stats
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   user_id INTEGER,
                   date DATE)''')

con.commit()


async def record_stat(user_id):
    cur.execute("INSERT INTO stats (user_id, date) VALUES (?, DATE('now'))", (user_id,))
    con.commit()


@dp.message_handler(commands="admin", state="*")
async def admin_panel(message: types.Message):
    await record_stat(message.from_user.id)
    user = message.from_user.id
    if str(user) in ADMINS:
        await message.answer("<b>Siz bu botda adminsiz 📌️️️️️️</b>", reply_markup=admin_btn)
        await AdminState.admin.set()
    else:
        pass


@dp.message_handler(text="Statistika 📊", state=AdminState.admin)
async def show_stats(message: types.Message):
    await record_stat(message.from_user.id)
    cur.execute("SELECT COUNT(DISTINCT user_id) FROM stats")
    total_users = cur.fetchone()[0]
    cur.execute("SELECT COUNT(DISTINCT user_id) FROM stats WHERE date = DATE('now')")
    today_users = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM stats")
    total_requests = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM stats WHERE date = DATE('now')")
    today_requests = cur.fetchone()[0]
    text = f"📊 Botdan foydalanish statistikasi:\n" \
           f" ├ Jami foydalanuvchilar: {total_users}\n" \
           f" ├ Bugungi foydalanuvchilar: {today_users}\n" \
           f" ├ Jami so'rovlar: {total_requests}\n" \
           f" └ Bugungi so'rovlar: {today_requests}"
    await message.reply(text)


@dp.message_handler(text="Yer maydon narxlarni qo'shish 🏘", state=AdminState.admin)
async def yer_maydon_narx_qoshish(message: types.Message):
    await record_stat(message.from_user.id)
    await message.answer("<b>Qaysi tuman uchun ?</b>", reply_markup=uz_tumanlar_btn)
    await AdminState.tuman.set()


@dp.message_handler(content_types=types.ContentType.TEXT, state=AdminState.tuman)
async def tumann(message: types.Message, state: FSMContext):
    global tuman
    tuman = message.text
    await record_stat(message.from_user.id)
    await message.answer("<b>Qaysi kategoriyaga uchun ?</b>", reply_markup=uz_kategoriya)
    await state.finish()
    await AdminState.kategoriya.set()


@dp.message_handler(content_types=types.ContentType.TEXT, state=AdminState.kategoriya)
async def kategoriya(message: types.Message, state: FSMContext):
    global kategoriya
    kategoriya = message.text
    await record_stat(message.from_user.id)
    await message.answer(f"""
<b>{tuman} uchun {kategoriya} kategoriyasiga narxni kiriting</b>

<b>Faqat dollarda kiriting</b>
<b>Masalan:</b> <code>1000</code>
    """)
    await AdminState.narx.set()


@dp.message_handler(content_types=types.ContentType.TEXT, state=AdminState.narx)
async def quruqyrlok(message: types.Message, state: FSMContext):
    narx = message.text.isdigit()
    await record_stat(message.from_user.id)
    print(f"{message.from_user.id} admin panelga malumot qoshildi")
    if narx == True:
        await message.answer("<b>Muvaffaqiyatli qo'shildi ✅</b>", reply_markup=admin_btn)
        await state.finish()
        await AdminState.admin.set()
        await narx_qoshish(tuman, kategoriya, message.text)
    else:
        await message.answer("<b>Faqat raqam kiriting ❌</b>")
