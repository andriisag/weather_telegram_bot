import telebot
from telebot import types
import requests
import json

bot = telebot.TeleBot("")
api_key = ""

@bot.message_handler(commands=['start'])
def start_message(message):
     bot.send_message(message.chat.id, text="Hello, " + message.chat.first_name)
     bot.send_message(message.chat.id, text="To get weather write a command and after one space write name of your city")

@bot.message_handler(commands=['local_weather'])
def message(message):
     input_mex = message.text
     city = input_mex.split('/local_weather ')[1]
     url = "https://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s&units=metric" % (city, api_key)
     response = requests.get(url)
     data = json.loads(response.text)
     bot.send_message(message.chat.id, "Weather in your city: " + data['weather'][0]['main'] + ", Temp: " + str(data['main']['temp']))
     
@bot.message_handler(commands=['local_forecast'])
def message(message):
     input_mex = message.text
     city = input_mex.split('/local_forecast ')[1]
     url = "https://api.openweathermap.org/data/2.5/forecast?q=%s&appid=%s&units=metric" % (city, api_key)
     response = requests.get(url)
     data = json.loads(response.text)
     for i in range(len(data['list'])):
         bot.send_message(message.chat.id, data['list'][i]['dt_txt'] + ": " + data['list'][i]['weather'][0]['main'] + ", Temp: " +  str(data['list'][i]['main']['temp']))
bot.infinity_polling()