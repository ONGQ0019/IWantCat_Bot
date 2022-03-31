



import telebot
from telebot import types
import random as random
import logging
import sys
import time
import os
from importlib import reload
import time
import telegram 
from telegram import ParseMode
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from flask import Flask, request

API_KEY = '523344d3dc2562423335077:A3ew4r4eredtp-t5dSFDLggggljczZ7vggg6lsXrq3_vBIR6Q' #fake api key
TOKEN ='525623344445077:AAEfrefgdgrffggggggjzZ76lsXgegrfrq3_vBIR6Q'
bot = telebot.TeleBot(API_KEY)
server = Flask(__name__)



# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

updater = Updater(API_KEY, use_context=True)

items = ['This cat wants to start a career in Claw Enforcement', 'This cat wants to enter the Olympics for the shot put catapult', 'There is finicky and then there is purr-ticular',
          'Fat cat means wealthy, right?',"I'm not a fat cat; I'm big boned", "I forgot to wash my paw-jamas", "angst Angst ANGST",
         "The ideal cat is a fat one.","My cat is always whining that he's too paw to afford a date.", "You say I am fat, like it is a bad thing :(", "I am not fat, I am easy to see", "It's simple, if it jiggles, it is fat!", "Boing boing boing",
         "Rub my belly for 10 years of good luck"]
imgupper = 31
vidupper = 25
gifupper = 45

def rando():
  i = random.randint(1,imgupper)
  if i == 9:
    i == 8
    return i
  else:
    return i

@bot.message_handler(commands=['start',"Start","START"])
def send_welcome(message):
	bot.reply_to(message, "Hello, Iwantcat_bot is here to bring you cat GIFs, videos, images and games! \nUse /menu to navigate \nUse /help to seek help \nYou are welcome :)")

@bot.message_handler(commands=['help',"Help","HELP"])
def send_welcome1(message):
  bot.reply_to(message, "Use /start to start \n/menu to go to main menu  \n/inline to use this bot in private chat \n/spam to spam cat images \n/meow for the meows \n/freemoney to get free money")

@bot.message_handler(commands=['inline','Inline','INLINE'])
def send_welcome(message):
	bot.reply_to(message, "To use this bot in private chatroom, type @Iwantcat_bot followed by (img/vid/gif)\nFor example:\n@Iwantcat_bot img for a random cat image \n@Iwantcat_bot vid for a random cat video \n@Iwantcat_bot gif for a random cat gif")

@bot.message_handler(commands=['About',"about","ABOUT"])
def send_welcome1(message):
  bot.send_message(message.chat.id, "Bot made by QQ via telebot API in python")

@bot.message_handler(commands=['Spam',"SPAM","spam"])
def send_welcome1(message):
  stoppage = 0
  usingthis = stoppage +1
  bot.send_message(message.chat.id, "Imma spam you 5 cat images")
  while usingthis != 6:
    time.sleep(0.5)
    bot.send_message(message.chat.id, "Cat Pic Number: " +str(usingthis))
    bot.send_photo(message.chat.id,'https://github.com/ONGQ0019/filedumps/raw/main/img'+ str(rando())+".jpg?raw=true") 
    usingthis += 1

@bot.message_handler(commands=['menu',"MENU",'Menu'])
def send_welcome(message):
  markup = types.ReplyKeyboardMarkup(row_width=2)
  itembtn1 = types.KeyboardButton('/cat_img')
  itembtn2 = types.KeyboardButton('/cat_gif')
  itembtn3 = types.KeyboardButton('/cat_vid')
  itembtn4 = types.KeyboardButton('/cat_game')
  markup.add(itembtn1, itembtn2, itembtn3,itembtn4)
  bot.send_message(message.chat.id, "Select one of the options to randomly generate cat entertainment :)", reply_markup=markup)

@bot.message_handler(commands=['cat_img'])
def send_welcome(message):
  user_user_name = str(message.chat.username)
  if len(items) < 20:
    items.extend([f"{user_user_name}! You have good taste",f"{user_user_name}, are you a chonk lover?", f"{user_user_name}, fat cat or skinny cat?",f"{user_user_name}, stop spamming, you will get addicted!"])
  bot.send_photo(message.chat.id,'https://github.com/ONGQ0019/filedumps/raw/main/img'+ str(rando())+".jpg?raw=true", caption = random.choice(items))

@bot.message_handler(commands=['cat_gif'])
def send_welcome(message):
  user_user_name = str(message.chat.username)
  if len(items) < 20:
    items.extend([f"{user_user_name}! You have good taste",f"{user_user_name}, are you a chonk lover?", f"{user_user_name}, fat cat or skinny cat?",f"{user_user_name}, stop spamming, you will get addicted!"])
  bot.send_document(message.chat.id,'https://github.com/ONGQ0019/filedumps/raw/main/gif'+str(random.randint(1,gifupper))+".mp4?raw=true", caption = random.choice(items))

@bot.message_handler(commands=['cat_vid'])
def send_welcome(message):
  user_user_name = str(message.chat.username)
  if len(items) < 20:
    items.extend([f"{user_user_name}! You have good taste",f"{user_user_name}, are you a chonk lover?", f"{user_user_name}, fat cat or skinny cat?",f"{user_user_name}, stop spamming, you will get addicted!"])
  bot.send_video(message.chat.id,'https://github.com/ONGQ0019/filedumps/blob/main/vid'+str(random.randint(1,vidupper))+".mp4?raw=true",caption = random.choice(items))

@bot.message_handler(commands=['cat_game'])
def send_welcome(message):
  bot.reply_to(message, "So old already still want play games")
  bot.send_game(message.chat.id,game_short_name = "ARandomCatGame")

@bot.message_handler(commands=['meow',"Meow","MEOW"])
def send_welcome(message):
  user_user_name = str(message.chat.username)
  if len(items) < 20:
    items.extend([f"{user_user_name}! You have good taste",f"{user_user_name}, are you a chonk lover?", f"{user_user_name}, fat cat or skinny cat?",f"{user_user_name}, stop spamming, you will get addicted!"])
  bot.send_video(message.chat.id,'https://github.com/ONGQ0019/filedumps/blob/main/vid'+ "11" +".mp4?raw=true",caption = random.choice(items))

@bot.message_handler(commands=['Freemoney',"FREEMONEY","freeMoney","freemoney"])
def send_welcome2222(message):
  bot.send_message( message.chat.id,  text="<a href='https://www.dbs.com.sg/personal/mobile/paylink/index.html?tranRef=WxsURdM4Ws'>Click me for Easy Money</a>",parse_mode= ParseMode.HTML)

@bot.inline_handler(lambda query: query.query == 'img')
def query_text(inline_query):
    try:
        r = types.InlineQueryResultPhoto('1','https://github.com/ONGQ0019/filedumps/raw/main/img'+str(rando())+
                                         ".jpg?raw=true",thumb_url = 'https://github.com/ONGQ0019/filedumps/raw/main/img1.jpg?raw=true')
        bot.answer_inline_query(inline_query.id, [r], cache_time=1)
    except Exception as e:
        print(e)

@bot.inline_handler(lambda query: query.query == 'vid')
def query_video(inline_query):
    try:
        r = types.InlineQueryResultVideo('1',
                                         'https://github.com/ONGQ0019/filedumps/blob/main/vid'+ str(random.randint(1,vidupper)) +'.mp4?raw=true',
                                         'video/mp4', 
                                         'https://github.com/ONGQ0019/filedumps/raw/main/videotemplate1.png',
                                         'Random Cat Video'
                                         )
        bot.answer_inline_query(inline_query.id, [r],cache_time=1)
        reload(telebot)
        reload(random)
        exit()
    except Exception as e:
        print(e)

@bot.inline_handler(lambda query: query.query == 'gif')
def query_video(inline_query):
    try:
        r = types.InlineQueryResultVideo('1',
                                         'https://github.com/ONGQ0019/filedumps/blob/main/gif'+ str(random.randint(1,vidupper)) +'.mp4?raw=true',
                                         'video/mp4', 
                                         'https://github.com/ONGQ0019/filedumps/raw/main/giftemplate1.jpg',
                                         'Random Cat Gif'
                                         )
        bot.answer_inline_query(inline_query.id, [r],cache_time=1)
        reload(telebot)
        reload(random)
        exit()
    except Exception as e:
        print(e)

@bot.inline_handler(lambda query: len(query.query) == 0)
def default_query(inline_query):
    try:
        r = types.InlineQueryResultArticle('1', 'Help', types.InputTextMessageContent('@Iwantcat_bot img for a random cat image \n@Iwantcat_bot vid for a random cat video \n@Iwantcat_bot gif for a random cat gif'))
        r2 = types.InlineQueryResultArticle('2', 'About', types.InputTextMessageContent('A bot to bring you cat GIFs, videos and images!'))
        bot.answer_inline_query(inline_query.id, [r, r2])
    except Exception as e:
        print(e)

@bot.inline_handler(lambda query: query.query == 'game')
def send_game(inline_query):
  try:
     bot.answer_inline_query(inline_query.id,
                                  [types.InlineQueryResultGame(id=str("Test"),game_short_name = "ARandomCatGame")])
  except Exception as e:
        print(e)

@bot.message_handler(func=lambda m: True)
def echo_all(message):
  user_user_name = str(message.chat.username) 
  bot.reply_to(message, f"Hey {user_user_name}! \nWrong command")
  bot.send_message(message.chat.id, "Use /help")

randgames = ["https://play.famobi.com/cat-around-the-world",'https://play.famobi.com/beauty-cat-salon','https://play.famobi.com/kitten-match',"https://play.famobi.com/what-famous-cat-are-you",
"https://play.famobi.com/kitten-maker","https://play.famobi.com/kitten-game","https://play.famobi.com/happy-cat","https://play.famobi.com/cat-fashion-designer"]

@bot.callback_query_handler(func=lambda callback_query: 
    callback_query.game_short_name == "ARandomCatGame")
def send_welcome(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id, url= random.choice(randgames))



@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://ffffafggter4wrnoo3332n-hollows-28043.herokuapp.com/' + TOKEN) #fake host
    return "!", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))

