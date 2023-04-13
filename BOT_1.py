import requests
import random
#import telebot
from bs4 import BeautifulSoup as b

URL = ''
#API_KEY  = '' для подключения бота. Набрать в телеграмм: botfather, задать имя боту и получить ключ.
"""
проверка подключения:

r = requests.get(URL)
print(r.status_code)
print(r.text)
"""
def parser(url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    any_1 = soup.find_all('div', class_='text')
    #print(any_1) отображение данных
    return [c.text for c in any_1]

list_1=parser(URL)
#random.shuffle(list_1)

"""
bot = telebot.TeleBot(API_KEY)
@bot.message_handler(command=['начать'])

"""

