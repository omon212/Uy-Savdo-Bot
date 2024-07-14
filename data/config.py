from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("BOT_TOKEN")  # Bot toekn
ADMINS = env.list("ADMINS")  # adminlar ro'yxati
WORK_DIRECTORY = env.str("WORK_DIRECTORY")  # Sqlite3 fayl manzili
CHANNEL_USERNAME = env.str("CHANNEL_USERNAME")
CHANNEL_LINK = f"https://t.me/{CHANNEL_USERNAME}"
CHANNEL_ID = env.int("CHANNEL_ID")
IP = env.str("ip")  # Xosting ip manzili
