import telegram
import var as V

def send_message(msg):
	bot = telegram.Bot(token=V.API_KEY)
	bot.send_message(chat_id=V.MY_ID, text=msg)

