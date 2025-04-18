from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("Animeni yuklash", callback_data='download')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Quyidagi tugmani bosing:", reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    # Bu yerga videolarni yuborish kodini yozasiz
    await query.message.reply_text("Bu yerga videolar yuboriladi (hozircha test)")

app = ApplicationBuilder().token("7815105138:AAFI4vb5jeX1FIvi9VhGNn1DaewZOt_vLhU").build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))

app.run_polling()
