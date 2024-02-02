import logging
from telegram import Update,  InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler
from telegram.constants import ParseMode

from scripts.meteo import *
from scripts.jokes import *
from scripts.starwars import *
from scripts.nasa import *

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
    await context.bot.send_message(chat_id=update.effective_chat.id, 
                                   text="¡Bienvenido a bordo del viaje virtual con Anémona de Mar! 🌊 \nSoy tu asistente virtual aquí para hacer que tu experiencia sea tan fluida como las olas del océano. \n¿Listo para sumergirte en un mundo de respuestas y asistencia?")

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, 
                                   text="¡Bienvenido a Anémona de Mar! 🌊 \nEste bot ha sido creado por @bamdab7. \n¿Listo para descubrir y aprender? Prueba con comandos como /starwars, /meteo o /jokes para ir conociendome.\n¡Estoy aquí para ayudarte! 😊👌")

async def nasa(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # await context.bot.send_message(chat_id=update.effective_chat.id, text=meteo_bot()) 
    img_url = daily_img()
    img_info = info_img()

    await context.bot.send_photo(chat_id=update.message.chat_id, photo=img_url, caption=img_info, parse_mode=ParseMode.MARKDOWN)


async def meteo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=meteo_bot()) 

async def jokes(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=jokes_bot()) 

#funcion que abre un menu despegable con mas consultas sobre star wars
async def starwars(update, context):
    keyboard = [
        [InlineKeyboardButton("Personajes 👽", callback_data='1'),
         InlineKeyboardButton("Planetas 🪐", callback_data='2'),
         InlineKeyboardButton("Naves 🛸", callback_data='3')],
        [InlineKeyboardButton("Especies 🧬", callback_data='4'),
        InlineKeyboardButton("Peliculas 📽️", callback_data='5')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("¡Bienvenido a la API de Star Wars! 🌌🚀 Explora la galaxia, descubre personajes, naves y planetas icónicos. Que la fuerza te acompañe en tu búsqueda de datos intergalácticos.", 
                                    reply_markup=reply_markup) 

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
    elif option_selected == '4':
        info = await species()
    elif option_selected == '5':
        info = await films()

    # await update.message.reply_text(info)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=info) 


if __name__ == '__main__':
    # Start the application to operate the bot
    application = ApplicationBuilder().token(TOKEN).build()

    # Handler to manage the start command
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    help_handler = CommandHandler('help', help)
    application.add_handler(CommandHandler("help", help))

    #handler to manage jokes api
    jokes_handler = CommandHandler('jokes', jokes)
    application.add_handler(jokes_handler)

    #handler to manage meteo api
    meteo_handler = CommandHandler('meteo', meteo)
    application.add_handler(meteo_handler)

    #handler to manage nasa img
    nasa_handler = CommandHandler('nasa', nasa)
    application.add_handler(nasa_handler)

    #handler to manage star wars
    starwars_handler = CommandHandler('starwars', starwars)
    application.add_handler(starwars_handler)

    application.add_handler(CallbackQueryHandler(button_click))


    # Keeps the application running
    application.run_polling()