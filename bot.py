import logging
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes
from scripts.meteo import *
from dotenv import load_dotenv
import os

# Authentication to manage the bot
load_dotenv()
TOKEN = os.getenv("TOKEN")
# if TOKEN == None:
#     print("Recuerda indicar la variable TOKEN") 
#     print("P.ex: docker run --rm --e TOKEN= o_teu_token nomebot")
#     exit(1)

# Show logs in terminal
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# This function responds to start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Soy un hermoso bot, que necesitas?")


async def meteo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=meteo_bot()) 

if __name__ == '__main__':
    # Start the application to operate the bot
    application = ApplicationBuilder().token(TOKEN).build()

    # Handler to manage the start command
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    #handler to manage meteo api
    meteo_handler = CommandHandler('meteo', meteo)
    application.add_handler(meteo_handler)
    
    # Keeps the application running
    application.run_polling()