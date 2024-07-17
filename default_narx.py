import sqlite3

# Ma'lumotlar bazasi ulanishi
conn = sqlite3.connect('uysavdo.db')
cursor = conn.cursor()

# Jadval yaratish
cursor.execute("""
    CREATE TABLE IF NOT EXISTS narxlar(
        id INTEGER PRIMARY KEY,
        tuman TEXT,
        category TEXT,
        narx INTEGER)
""")


# Tumandagi va kategoriyadagi qiymatlar
tumanlar = [
    "Bektemir", "Olmazor", "Uchtepa", "Chilonzor", "Sergeli",
    "Shayxontohur", "Yakkasaroy", "Yangihayot", "Yashnobod",
    "Mirobod", "MirzoUlugbek", "Yunusobod"
]

kategoriyalar = [
    "Uchastka", "Quruq Yer", "PenHouse", "TaunHouse",
    "Evro Dom", "Kvartira"
]

# Har bir tuman va kategoriya uchun dastlabki qiymat kiritish
for tuman in tumanlar:
    for kategoriya in kategoriyalar:
        cursor.execute("INSERT INTO narxlar (tuman, category, narx) VALUES (?, ?, ?)", (tuman, kategoriya, 100))

for tuman in tumanlar:
    for kategoriya in kategoriyalar:
        cursor.execute("INSERT INTO narxlar_xona (tuman, category, narx) VALUES (?, ?, ?)", (tuman, kategoriya, 10000))

# O'zgarishlarni saqlash
conn.commit()

# Ma'lumotlar bazasi ulanishini yopish
conn.close()
