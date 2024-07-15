import sqlite3
from data.config import WORK_DIRECTORY

connect = sqlite3.connect(f'{WORK_DIRECTORY}/uysavdo.db')
cursor = connect.cursor()

cursor.execute(
    "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY,user_id INTEGER,language TEXT,phone TEXT,fullname TEXT)")

cursor.execute("""CREATE TABLE IF NOT EXISTS narxlar(
                id INTEGER PRIMARY KEY,
                tuman TEXT,
                category TEXT,
                narx INTEGER)""")

cursor.execute("""DROP TABLE IF EXISTS kategory""")

connect.commit()

async def check_user(user_id):
    result = cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,)).fetchone()
    return result


async def save_all_data(user_id, language, phone, fullname):
    save = cursor.execute("INSERT INTO users (user_id, language, phone, fullname) VALUES (?, ?, ?, ?)",
                          (user_id, language, phone, fullname))
    connect.commit()
    if save:
        return True
    else:
        return False


async def update_language(user_id, language):
    update = cursor.execute("UPDATE users SET language = ? WHERE user_id = ?", (language, user_id))
    connect.commit()


async def update_fullname(user_id, fullname):
    update = cursor.execute("UPDATE users SET fullname = ? WHERE user_id = ?", (fullname, user_id))
    connect.commit()


async def update_phone(user_id, phone):
    cursor.execute("UPDATE users SET phone = ? WHERE user_id = ?", (phone, user_id))
    connect.commit()


async def narx_qoshish(tuman, category, narx):
    bormi_yoqmi = cursor.execute("SELECT * FROM narxlar WHERE tuman = ? AND category = ?", (tuman, category)).fetchone()
    print(bormi_yoqmi)
    if bormi_yoqmi == None:
        print(True)
        cursor.execute("INSERT INTO narxlar(tuman, category, narx) VALUES (?, ?, ?)", (tuman, category, narx))
        connect.commit()
    else:
        print(False)
        cursor.execute("UPDATE narxlar SET narx = ? WHERE tuman = ? AND category = ?", (narx, tuman, category))
        connect.commit()


async def narx_qidirish(tuman, category):
    result = cursor.execute("SELECT * FROM narxlar WHERE tuman = ? AND category = ?", (tuman, category)).fetchone()
    return result
