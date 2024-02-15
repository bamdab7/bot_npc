import logging
from telegram import Update,  InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler
from telegram.constants import ParseMode

from scripts.meteo import *
from scripts.jokes import *
from scripts.starwars import *
from scripts.nasa import *
from scripts.noticias import *
from scripts.bbdd import *
from scripts.fichero import *

from dotenv import load_dotenv
import os

wait = "Obteniendo datos ... ⌛"
# Authentication to manage the bot
load_dotenv()
TOKEN = os.getenv("TOKEN")
if TOKEN == None:
    print("Recuerda indicar la variable TOKEN") 
    print("P.ex: docker run --rm --e TOKEN= o_teu_token nomebot")
    exit(1)

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

async def fichero(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = await context.bot.get_file(update.message.document)
    filename = update.message.document.file_name
    
    nombre_fichero = filename.split(".")[0]
    
    await file.download_to_drive(filename)
    current_directory = os.getcwd()
    path = f"{current_directory}/{filename}"
    
    if filename.endswith(".csv"):
        fichero = csv_to_json(nombre_fichero,path)
        await context.bot.send_document(update._effective_chat.id, document=fichero)
        
        informacion = str(info_fichero_csv(path))

        await context.bot.send_message(chat_id=update.effective_chat.id, text=informacion, parse_mode=ParseMode.MARKDOWN) 
        
        os.remove(path)
        os.remove(f"{nombre_fichero}.json")
    
    elif filename.endswith(".json"):
        fichero = json_to_csv(nombre_fichero)
        await context.bot.send_document(update._effective_chat.id, document=fichero)
        
        informacion = str(info_fichero_json(path))
        await context.bot.send_message(chat_id=update.effective_chat.id, text=informacion, parse_mode=ParseMode.MARKDOWN) 
        os.remove(path)
        os.remove(f"{nombre_fichero}.csv") 
    
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Fichero no valido", parse_mode=ParseMode.MARKDOWN)


async def nasa(update: Update, context: ContextTypes.DEFAULT_TYPE):
    waiting = await context.bot.send_message(chat_id=update.effective_chat.id, text=wait, parse_mode=ParseMode.MARKDOWN)
    
    # await context.bot.send_message(chat_id=update.effective_chat.id, text=meteo_bot()) 
    img_url = daily_img()
    texto = info_img()

    if len(texto) <= 1024:  # Adjust the limit as needed
       await context.bot.send_photo(chat_id=update.message.chat_id, photo=img_url, caption=texto, parse_mode=ParseMode.MARKDOWN)
    else:
        await context.bot.send_photo(chat_id=update.message.chat_id, photo=img_url)
        await context.bot.send_message(chat_id=update.message.chat_id, text=texto, parse_mode=ParseMode.MARKDOWN)
    #mensaje de espera    
    await context.bot.delete_message(chat_id=update.effective_chat.id, message_id=waiting.message_id)
    
async def meteo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=meteo_bot(), parse_mode=ParseMode.MARKDOWN) 

async def jokes(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=jokes_bot()) 
    
async def get_inferno(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["user"] = "waiting_user"
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Infroduce tu nombre para saber con qué pecados irás al infierno 🔥👺") 
    
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.user_data:
        pass
    elif context.user_data["user"] == "waiting_user":
        user = update.message.text
        await context.bot.send_message(chat_id=update.effective_chat.id, text=inferno(user),parse_mode=ParseMode.MARKDOWN)
        
        context.user_data["user"] = None

#---------------------------------------------------------------------------------------
#funcion que abre un menu despegable con mas consultas sobre star wars
async def starwars(update, context):
    keyboard1 = [
        [InlineKeyboardButton("Personajes 👽", callback_data='1'),
         InlineKeyboardButton("Planetas 🪐", callback_data='2'),
         InlineKeyboardButton("Naves 🛸", callback_data='3')],
        [InlineKeyboardButton("Especies 🧬", callback_data='4'),
        InlineKeyboardButton("Peliculas 📽️", callback_data='5')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard1)
    await update.message.reply_text("¡Bienvenido a la API de Star Wars! 🌌🚀 Explora la galaxia, descubre personajes, naves y planetas icónicos. Que la fuerza te acompañe en tu búsqueda de datos intergalácticos.", 
                                    reply_markup=reply_markup) 

#funcion que abre un menu despegable con mas consultas sobre star wars
async def scrapp(update, context):
    keyboard2 = [
        [InlineKeyboardButton("La Voz de Galicia 📰", callback_data='6'),
         InlineKeyboardButton("Baloncesto 🏀", callback_data='7'),
         InlineKeyboardButton("Cartelera 🎬", callback_data='8')],
        [InlineKeyboardButton("Palabras más buscada 📖", callback_data='9')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard2)
    await update.message.reply_text("¡Bienvenido a nuestro bot informativo! 📰🎬 \n Explora las últimas noticias de los periódicos más destacados y descubre los eventos más emocionantes en tu ciudad. \n¡Disfruta de la información fresca y el entretenimiento en un solo lugar! 🤖", 
                                    reply_markup=reply_markup) 
    
#-----------------------------------------------------------------------------------
async def button_click(update, context):
    waiting = await context.bot.send_message(chat_id=update.effective_chat.id, text=wait, parse_mode=ParseMode.MARKDOWN)
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
    elif option_selected == '6':
        info = await voz_galicia()
    elif option_selected == '7':
        info = await basket()
    elif option_selected == '8':
        info = await cartelera()
    elif option_selected == '9':
        info = await palabra()
    
    await context.bot.send_message(chat_id=update.effective_chat.id, text=info, parse_mode=ParseMode.MARKDOWN) 
    
    #mensaje de espera
    await context.bot.delete_message(chat_id=update.effective_chat.id, message_id=waiting.message_id)
#----------------------------------------------------------------------------------

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
    
    #handler to manage inferno bbdd
    inferno_handler = CommandHandler('inferno', get_inferno)
    application.add_handler(inferno_handler)
    
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    application.add_handler(echo_handler)

    #handler to manage star wars
    starwars_handler = CommandHandler('starwars', starwars)
    application.add_handler(starwars_handler)
    
    #handler to manage scrapping
    scrapping_handler = CommandHandler('scrapp', scrapp)
    application.add_handler(scrapping_handler)

    #handle to manage files
    application.add_handler(MessageHandler(filters.Document.ALL, fichero))
    
    application.add_handler(CallbackQueryHandler(button_click))



    # Keeps the application running
    application.run_polling()