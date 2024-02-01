import logging
from telegram import Update,  InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler


from scripts.meteo import *
from scripts.jokes import *
from scripts.starwars import *

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

async def jokes(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=jokes_bot()) 

#funcion que abre un menu despegable con mas consultas sobre star wars
async def starwars(update, context):
    keyboard = [
        [InlineKeyboardButton("Personas", callback_data='1'),
         InlineKeyboardButton("Planetas", callback_data='2'),
         InlineKeyboardButton("Naves", callback_data='3')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Por favor, elige una opción:', reply_markup=reply_markup) 

async def button_click(update, context):
    query = update.callback_query

    if query is None:
        return
    
    await query.answer()

    option_selected = query.data

      # Llamar a diferentes funciones según la opción seleccionada
    if option_selected == '1':
        info = await people()
    elif option_selected == '2':
        info = await planets()
    elif option_selected == '3':
        info = await starships()

    # await update.message.reply_text(info)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=info) 


if __name__ == '__main__':
    # Start the application to operate the bot
    application = ApplicationBuilder().token(TOKEN).build()

    # Handler to manage the start command
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    #handler to manage jokes api
    jokes_handler = CommandHandler('jokes', jokes)
    application.add_handler(jokes_handler)

    #handler to manage meteo api
    meteo_handler = CommandHandler('meteo', meteo)
    application.add_handler(meteo_handler)

    #handler to manage star wars
    starwars_handler = CommandHandler('starwars', starwars)
    application.add_handler(starwars_handler)

    application.add_handler(CallbackQueryHandler(button_click))


    # Keeps the application running
    application.run_polling()