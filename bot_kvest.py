from flask import Flask, request, jsonify
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
import os
import asyncio
TOKEN = '6429416800:AAGmnFMhkbD8XagsGCgIROmbM2wgwo7ApFE'
WEBHOOK_URL = 'https://yourdomain.com/webhook'  # заменить на ваш фактический URL

app = Flask(__name__)

# # Установка вебхука
# async def set_webhook():
#     application = ApplicationBuilder().token(TOKEN).build()
#     await application.bot.set_webhook(WEBHOOK_URL)
#     return application

# @app.route('/webhook', methods=['POST'])
# def webhook():
#     json_update = request.get_json()
#     update = Update.de_json(json_update, application.bot)
#     application = ApplicationBuilder().token(TOKEN).build()
#     application.process_update(update)
#     return jsonify(success=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Открыть Web App", url="http://localhost:5000/kvest_app")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Привет! Нажми на кнопку ниже, чтобы открыть Web App.', reply_markup=reply_markup)

def main():
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler('start', start))
    await application.run_polling()
# Запуск Telegram бота

asyncio.run(main())

# Основной маршрут для веб-приложения
@app.route('/kvest_app', methods=['GET'])
def webapp():
    return render_template('kvest.html')

if __name__ == '__main__':
    app.run()