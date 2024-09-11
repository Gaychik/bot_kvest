from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
import asyncio

TOKEN = '6429416800:AAGmnFMhkbD8XagsGCgIROmbM2wgwo7ApFE'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Открыть Web App", url="http://localhost:5000/kvest_app")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Привет! Нажми на кнопку ниже, чтобы открыть Web App.', reply_markup=reply_markup)

def main():
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler('start', start))
    application.run_polling()

if __name__ == '__main__':
       main() 