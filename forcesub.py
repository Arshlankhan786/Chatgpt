from pyrogram import Client, filters,enums,idle
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.enums import ChatAction, ParseMode
import openai
from pyrogram.types import CallbackQuery
from config import *
import os,sys,re,requests
import asyncio,time
from random import choice
from bardapi import Bard
from datetime import datetime
import logging

# Define your bot token
bot_token = "BOT_TOKEN"
# Define the command handler for the /start command
def start(update: Update, context: CallbackContext) -> None:
    # Check if the user is already subscribed
    if update.effective_user.is_bot:
        return

    user_id = update.effective_user.id
    chat_id = update.effective_chat.id

    # Check if the user is already subscribed
    if not is_subscribed(user_id):
        # Send a message asking the user to subscribe
        context.bot.send_message(chat_id=chat_id, text='Please subscribe to use this bot.')
        return

    # Continue with the normal functionality of the /start command
    context.bot.send_message(chat_id=chat_id, text='Welcome to the bot!')

# Define the message handler for all messages
def message_handler(update: Update, context: CallbackContext) -> None:
    # Check if the user is already subscribed
    if update.effective_user.is_bot:
        return

    user_id = update.effective_user.id
    chat_id = update.effective_chat.id

    # Check if the user is already subscribed
    if not is_subscribed(user_id):
        # Send a message asking the user to subscribe
        context.bot.send_message(chat_id=chat_id, text='Please subscribe to use this bot.')
        return

    # Continue with the normal functionality of the bot
    # ...

# Function to check if a user is subscribed
def is_subscribed(user_id: int) -> bool:
    # Implement your logic to check if the user is subscribed
    # Return True if subscribed, False otherwise
    return True

# Create an instance of the Updater class
updater = Updater(TOKEN)

# Get the dispatcher to register handlers
dispatcher = updater.dispatcher

# Register the command handler for the /start command
dispatcher.add_handler(CommandHandler('start', start))

# Register the message handler for all messages
dispatcher.add_handler(MessageHandler(Filters.all, message_handler))

# Start the bot
updater.start_polling()
