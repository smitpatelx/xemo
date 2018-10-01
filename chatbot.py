#   Author:     Smit Patel
#   Date:       25/07/2018
#   File:       chatbot_trainer.py
#   Licence:    MIT

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

bot = ChatBot('Bot')
bot.set_trainer(ListTrainer)

while True:
        message = input('You:')
        if message.strip() != 'Bye':
            reply = bot.get_response(message)
            print('ChatBot :', reply)
        if message.strip() == 'Bye':
            print('ChatBot : Bye, see u again')
            break
