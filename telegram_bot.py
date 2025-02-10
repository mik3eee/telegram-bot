import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

TOKEN = os.getenv("7831628827:AAHYub1aTFbk0U5MHX1UdBg6U5PxHDZ6pDA")  # Na Heroku použijeme environmentálnu premennú

async def start(update: Update, context):
    await update.message.reply_text("Ahoj! Som Telegram bot.")

async def echo(update: Update, context):
    await update.message.reply_text(update.message.text)

def main():
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    application.run_polling()

if __name__ == '__main__':
    main()