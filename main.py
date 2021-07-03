from telegram.bot import Bot
from telegram.user import User
from telegram.ext import Updater, Dispatcher, CommandHandler, CallbackContext
from telegram.update import Update
from settings import settings
bot = Bot(token=settings.TELEGRAM_TOKEN)

user: User = bot.get_me()


updater = Updater(token=settings.TELEGRAM_TOKEN)



def start(update: Update, context:CallbackContext):
	update.message.reply_text('Salom!')
	context.bot.send_message(
							chat_id=update.message.chat_id,
							 text='Salom yana bir bor!')# chat_id orqali kimga text ni jo'natishni aytib o'tdik

dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))
updater.start_polling()

updater.idle()
