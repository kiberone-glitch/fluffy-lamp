import telebot
bot = telebot.TeleBot("8857752048:AAE3gcmTuYm9KXzJ8h68aXyjnNVprmHUZbM")
@bot.message_handler([commands='start'])
def start(message)
  chat_id=message.chat.id
  bot.send_message(chat_id,"hello")
if __name__ in "__main__":
  print("yes")
  bot.infinity_polling()
