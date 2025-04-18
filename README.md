import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

BOT_TOKEN = '7815105138:AAFI4vb5jeX1FIvi9VhGNn1DaewZOt_vLhU'
CHANNEL = '@https://t.me/+LkwqC4aEWTsxNDdi'  # kanal username, masalan: @animeuzbchannel
OWNER_ID = 6966360718  # o'z Telegram ID'ingiz

bot = telebot.TeleBot(BOT_TOKEN)

# RAM ichida vaqtincha saqlash (xohlasangiz keyin SQLite qo‘shamiz)
video_store = {}

@bot.message_handler(commands=['start'])
def start_handler(message):
    args = message.text.split()
    if len(args) > 1:
        video_id = args[1]
        if video_id in video_store:
            file_id = video_store[video_id]
            bot.send_video(message.chat.id, file_id, caption="Mana siz so‘ragan anime!")
        else:
            bot.send_message(message.chat.id, "Kechirasiz, video topilmadi.")
    else:
        bot.send_message(message.chat.id, "Salom! Kanaldagi tugmani bosib anime ko‘rishingiz mumkin.")

@bot.message_handler(content_types=['video'])
def handle_video(message):
    if message.from_user.id == OWNER_ID:
        file_id = message.video.file_id
        unique_id = str(message.message_id)  # Har bir video uchun unikal ID
        video_store[unique_id] = file_id

        # Kanal uchun tugma
        markup = InlineKeyboardMarkup()
        btn = InlineKeyboardButton("Animeni ko‘rish", url=f"https://t.me/{bot.get_me().username}?start={unique_id}")
        markup.add(btn)

        # Kanalga yuboriladigan xabar (siz qo‘lda nusxa olasiz yoki avtomatik bot yuboradi)
        bot.send_message(CHANNEL, "Yangi anime yuklandi!", reply_markup=markup)

        # Sizga tasdiq yuboriladi
        bot.send_message(message.chat.id, "Kanalga tugma joylandi.")
    else:
        bot.send_message(message.chat.id, "Kechirasiz, sizga ruxsat yo‘q.")

bot.infinity_polling()# my-telegram
