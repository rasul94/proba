import telebot
import parol

bot = telebot.TeleBot('622767171:AAHFB_dYl1I6SDBJ5hHO81WOkg9Yms6jV64')

bot.send_message(227754968, "sava")

@bot.message_handler(content_types=['text'])
def hadle_text(message):
    if message.text == "Sartoroshxona yopil":
		bot.send_message(227754968, "yov")
	elif:
	bot.send_message(227754968, "yov yov")
	
	
bot.polling(none_stop=True, interval=0)