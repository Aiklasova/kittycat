import telebot
import argparse
import os
import random

# Open cmd. Then write CD and path to bot folder.
# Run echo_bot with command 'python echo_bot.py --p "path\to\folder\"'
# Path to images folder should look like this
# "C:\Users\WINDOWS 10\PycharmProjects\tgbot\kittens\\"

# To get the path from the command line
parser = argparse.ArgumentParser()
# Set one required argument
parser.add_argument("--p", default=1, type=str, help="Path", required=True)
# Adding arguments to args
args = parser.parse_args()
# The path variable is responsible for the path to the desired folder
path = args.p
# Get the full list of photos from the folder
files = os.listdir(path)

# We initialize our bot using a unique token
bot = telebot.TeleBot("1214708503:AAHqVuGoG4XvUDxy2kO9FgNGob0x7U3KZZM")


# At the command '/start', the bot will send a message "Hi, want a picture?"
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Hi, want a picture?")


# The command '/get' will execute the following function
@bot.message_handler(commands=['getcat'])
def send_photo(message):
    # We inform the user that the photo will be sent now
    bot.send_chat_action(message.chat.id, 'upload_photo')
    random.seed()
    # To get a random photo number
    rand_num = random.randint(0, len(files) - 1)
    # Open photo
    img = open(path + files[rand_num], 'rb')
    # We respond to the command with a random photo of a cat
    bot.send_photo(message.chat.id, img,
                   reply_to_message_id=message.message_id)
    # Close photo
    img.close()


bot.polling()
