from telegram.bot import Bot
from telegram.user import User
from telegram.ext import Updater, Dispatcher, CommandHandler, CallbackContext, MessageHandler
from telegram.ext.filters import Filters
from telegram.update import Update
from settings import settings
import requests
bot = Bot(token=settings.TELEGRAM_TOKEN)

user: User = bot.get_me()


updater = Updater(token=settings.TELEGRAM_TOKEN)



def start(update: Update, context:CallbackContext):
	update.message\
					.reply_text('Assalomu alaykum! Vikipediadan ma\'lumot qidiruvchi'
								' botga xush kelibsiz! Biron nima izlash uchun /search'
								' va so\'rovingizni yuboring. Misol uchun /search Amir Temur kabi.')
	

def search(update:Update, context: CallbackContext):
	args = context.args
	if len(args) == 0:
		update.message.reply_text("Hech bo'lmasa, biron narsa kiriting ! Masalan, /search Amir Temur")
	else:
		
		search_text = ' '.join(args)
		response = requests.get('https://uz.wikipedia.org/w/api.php', {
			'action' : 'opensearch',
			'search' : search_text,
			'limit': 1,
			'namespace' : 0,
			'format': 'json',
			})
		result = response.json()
		link = result[3]
		if len(link):
			update.message\
					.reply_text("Sizning so'rovingiz bo'yicha havola: " + link[0])
		else:
			update.message\
				.reply_text("Sizning so'rovingiz bo'yicha hech qanday havola topilmadi!  :(")	
	

dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('search', search))
dispatcher.add_handler(MessageHandler(Filters.all, start))
updater.start_polling()

updater.idle()
