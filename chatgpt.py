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

FORMAT = "[VIKAS] %(message)s"
logging.basicConfig(
    level=logging.WARNING, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)


StartTime = time.time()
vikas = Client(
    "chat-gpt" ,
    api_id = API_ID,
    api_hash = API_HASH ,
    bot_token = BOT_TOKEN
)
START = f"""
๏ ʜᴇʏ, ɪ ᴀᴍ {BOT_NAME}
➻ ᴀɴ ᴏᴘᴇɴ-ᴀɪ-ʙᴀsᴇᴅ ᴄʜᴀᴛɢᴘᴛ.
──────────────────
ɪ ᴀᴍ ᴀᴅᴠᴀɴᴄᴇ ʙᴏᴛ ᴀɴᴅ ᴄᴀɴ 
ᴀɴsᴡᴇʀ ʏᴏᴜʀ ᴏ̨ᴜᴇʀɪᴇs ᴇᴀsʟɪʏ

Rᴇᴀᴅ Tʜᴇ ʜᴇʟᴘ sᴇᴄᴛɪᴏɴ ғᴏʀ ᴍᴏʀᴇ ɪɴғᴏ

๏ ᴛᴏ ɢᴇᴛ ʜᴇʟᴘ ᴜsᴇ /help
"""





x=["❤️","🎉","✨","🪸","🎉","🎈","🎯"]
g=choice(x)
MAIN = [
    [
        InlineKeyboardButton(text="ᴅᴇᴠᴇʟᴏᴘᴇʀ", url=f"https://t.me/{OWNER_USERNAME}"),
        InlineKeyboardButton(text=" ꜱᴜᴘᴘᴏʀᴛ ", url=f"https://t.me/{SUPPORT_GRP}"),
    ],
    [
        InlineKeyboardButton(
            text="ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="ʜᴇʟᴘ & ᴄᴍᴅs ", callback_data="HELP"),
    ],
    [
        
        InlineKeyboardButton(text=" ᴜᴘᴅᴀᴛᴇs ", url=f"https://t.me/{UPDATE_CHNL}"),
    ],
]
X = [
    [
        InlineKeyboardButton(text="ᴅᴇᴠᴇʟᴏᴘᴇʀ", url=f"https://t.me/{OWNER_USERNAME}"),
        
        InlineKeyboardButton(text=" ꜱᴜᴘᴘᴏʀᴛ ", url=f"https://t.me/{SUPPORT_GRP}"),
    ]
    ]
    
PNG_BTN = [
    [
         InlineKeyboardButton(
             text="ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ",
             url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
         ),
     ],
     [
         InlineKeyboardButton(text="sᴜᴘᴘᴏʀᴛ", 
                              url=f"https://t.me/{SUPPORT_GRP}",
         ),
     ],
]


HELP_READ = "**➻ ᴜsᴀɢᴇ** /chatgpt <prompt>\n\n ᴇxᴀᴍᴘʟᴇ: `/chatgpt write a simple flask app in python.`\n\n**➻ ᴜsᴀɢᴇ** : /generate <prompt> \nᴇxᴀᴍᴘʟᴇ: `/generate a cute girl photo`  \n\n➻ ᴜsᴀɢᴇ /lyrics : ʀᴇᴘʟʏ ᴛᴏ ᴀᴜᴅɪᴏ ꜰɪʟᴇ ᴛᴏ ᴅᴇᴛᴇᴄᴛ ʟʏʀɪᴄꜱ**➻ ᴜsᴀɢᴇ /ping ᴛᴏ ᴄʜᴇᴄᴋ ᴛʜᴇ ᴘɪɴɢ ᴏғ ᴛʜᴇ ʙᴏᴛ.**\n\n©️ @kira_developer**"
HELP_BACK = [
     [
           InlineKeyboardButton(text="Qᴜᴇꜱᴛɪᴏɴ ᴛʜᴀᴛ ᴄʜᴀᴛɢᴘᴛ ᴄᴀɴ ꜱᴏʟᴠᴇ ", url=f"https://t.me/kira_developer"),
           
     ],
    [
           InlineKeyboardButton(text="ʙᴀᴄᴋ ", callback_data="HELP_BACK"),
    ],
]

 #force sub

# Replace 'YOUR_CHANNEL_ID' with your actual channel ID (e.g., @your_channel)
CHANNEL_ID = '-1001875834087'

def start(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id

    # Check if the user is already in the channel
    if user_in_channel(user_id, context):
        update.message.reply_text('You are already subscribed. You can use the bot.')
    else:
        # Prompt the user to join the channel
        update.message.reply_text(
            f'Welcome! To use this bot, please join our channel: {CHANNEL_ID}',
            parse_mode=ParseMode.MARKDOWN,
            reply_markup={'inline_keyboard': [[{'text': 'Join Channel', 'url': f'https://t.me/{CHANNEL_ID}'}]]}
        )

def user_in_channel(user_id: int, context: CallbackContext) -> bool:
    # Implement logic to check if the user is in the channel using the Telegram Bot API
    try:
        # Get chat member information
        chat_member = context.bot.get_chat_member(chat_id=CHANNEL_ID, user_id=user_id)
        # Check if the user is a member of the channel
        return chat_member.status == 'member'
    except Exception as e:
        print(f"Error checking user in channel: {e}")
        return False
        

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
    
#         start
@vikas.on_message(filters.command(["start",f"start@{BOT_USERNAME}"]))
async def start(client, m: Message):
    try:
        accha = await m.reply_text(
                        text = f"{g}")
        await asyncio.sleep(0.2)
        await accha.edit("ᴘɪɴɢ ᴘᴏɴɢ ꜱᴛᴀʀᴛɪɴɢ..")
        await asyncio.sleep(0.2)
        await accha.delete()
        umm = await m.reply_sticker(
                  sticker = STKR,
        )
        await asyncio.sleep(0.3)
        await umm.delete()
        await m.reply_photo(
            photo = START_IMG,
            caption=START,
            reply_markup=InlineKeyboardMarkup(MAIN),
        )
    except Exception as y:
        await m.reply(y)
#  callback 
@vikas.on_callback_query()
async def cb_handler(Client, query: CallbackQuery):
    if query.data == "HELP":
     await query.message.edit_text(
                      text = HELP_READ,
                      reply_markup = InlineKeyboardMarkup(HELP_BACK),
     )
    elif query.data == "HELP_BACK":
            await query.message.edit(text = START,
                  reply_markup=InlineKeyboardMarkup(MAIN),
        )
    
@vikas.on_message(filters.command(["help", f"help@{BOT_USERNAME}"], prefixes=["","+", ".", "/", "-", "?", "$"]))
async def restart(client, message):
    hmm = await message.reply_photo(START_IMG,
                        caption=HELP_READ,
                        reply_markup= InlineKeyboardMarkup(HELP_BACK),
       )

    
    
#  alive
@vikas.on_message(filters.command(["ping","alive"], prefixes=["+", "/", "-", "?", "$", "&","."]))
async def ping(client, message: Message):
        start = datetime.now()
        t = "ριиgιиg..."
        txxt = await message.reply(t)
        await asyncio.sleep(0.25)
        await txxt.edit_text("ριиgιиg.....")
        await asyncio.sleep(0.35)
        await txxt.delete()
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await message.reply_photo(
                             photo=START_IMG,
                             caption=f"ʜᴇʏ ʙᴀʙʏ!!\n**[{BOT_NAME}](t.me/{BOT_USERNAME}) ɪꜱ ᴀʟɪᴠᴇ 🥀 ᴀɴᴅ ᴡᴏʀᴋɪɴɢ ꜰɪɴᴇ ᴡɪᴛʜ ᴘᴏɴɢ ᴏꜰ \n➥ `{ms}` ms\n\n**ᴍᴀᴅᴇ ᴡɪᴛʜ ❣️ ʙʏ || [Mrdaxx](https://t.me/kira_developer)||",
                             reply_markup=InlineKeyboardMarkup(PNG_BTN),
       )

#  main   
openai.api_key = OPENAI_KEY

@vikas.on_message(filters.private)  # Only respond to private messages
async def auto_reply_handler(client, message):
    try:
        start_time = time.time()
        await client.send_chat_action(message.chat.id, ChatAction.TYPING)

        # Extract the user's message
        user_message = message.text

        # Your logic to interact with OpenAI GPT goes here
        # For example, you can use OpenAI API to get a response
        model = "gpt-3.5-turbo"
        response = openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "user", "content": user_message}],
            temperature=0.2
        )
        answer = response['choices'][0]["message"]["content"]

        # Send the GPT-generated answer as a reply
        end_time = time.time()
        response_time = str(round((end_time - start_time) * 1000, 3)) + " ms"
        await message.reply_text(f"ChatGPT answered:\n\n{answer}\n\nResponse time: {response_time}")
    except Exception as e:
        await message.reply_text(f"Error: {e}")
        
# group main
@vikas.on_message(filters.command(["chatgpt","ai","ask"],  prefixes=["+", ".", "/", "-", "?", "$","#","&"]))
async def chat(bot, message):
    
    try:
        start_time = time.time()
        await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
        if len(message.command) < 2:
            await message.reply_text(
            "Example:**\n\n`/chatgpt Where is TajMahal?`")
        else:
            a = message.text.split(' ', 1)[1]
            MODEL = "gpt-3.5-turbo"
            resp = openai.ChatCompletion.create(model=MODEL,messages=[{"role": "user", "content": a}],
    temperature=0.2)
            x=resp['choices'][0]["message"]["content"]
            end_time = time.time()
            telegram_ping = str(round((end_time - start_time) * 1000, 3)) + " ᴍs"
            await message.reply_text(f"{message.from_user.first_name} ᴀꜱᴋᴇᴅ:\n\n {a} \n\n {BOT_NAME} ᴀɴꜱᴡᴇʀᴇᴅ:-\n\n {x}\n\n✨ᴛɪᴍᴇ ᴛᴀᴋᴇɴ  {telegram_ping} \n\n🎉ᴘᴏᴡᴇʀᴇᴅ ʙʏ @{BOT_USERNAME} ", parse_mode=ParseMode.MARKDOWN,reply_markup=InlineKeyboardMarkup(X))     
    except Exception as e:
        await message.reply_text(f"**ᴇʀʀᴏʀ: {e} ")
        


            
#  bard 

'''bard = Bard(token=BARD_TOKEN)   
@vikas.on_message(filters.command("bard"))
async def bard_bot(bot, message):
    try:
        start_time = time.time()
        await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
        if len(message.command) < 2:
            await message.reply_text(
            "Example:**\n\n` /bard How r u? `")
        else:
            a = message.text.split(' ', 1)[1]
            response=bard.get_answer(f"{a}")["content"]
            await message.reply_text(f"{response}\n\n🎉ᴘᴏᴡᴇʀᴇᴅ ʙʏ @{BOT_USERNAME} ", parse_mode=ParseMode.MARKDOWN,reply_markup=InlineKeyboardMarkup(X))     
    except Exception as e:
        await message.reply_text(f"**ᴇʀʀᴏʀ:  {e} ")

    '''
openai.api_key = OPENAI_KEY
@vikas.on_message(filters.command(["image","photo","img","generate"],  prefixes=["+", ".", "/", "-", "?", "$","#","&"] ))
async def chat(bot, message):
    try:
        start_time = time.time()
        await bot.send_chat_action(message.chat.id, ChatAction.UPLOAD_PHOTO)
        if len(message.command) < 2:
            await message.reply_text(
            "**Example:**\n\n`/generate a white siamese cat`")
        else:
            a = message.text.split(' ', 1)[1]
            response= openai.Image.create(prompt=a ,n=1,size="1024x1024")
            image_url = response['data'][0]['url']
            end_time = time.time()
            telegram_ping = str(round((end_time - start_time) * 1000, 3)) + " ᴍs"
            await message.reply_photo(image_url,caption=f"✨ᴛɪᴍᴇ ᴛᴀᴋᴇɴ {telegram_ping} ",parse_mode=ParseMode.DISABLED,reply_markup=InlineKeyboardMarkup(X)) 
    except Exception as e:
            await message.reply_text(f"**ᴇʀʀᴏʀ: **  ` {e} `")
openai.api_key = OPENAI_KEY
@vikas.on_message(filters.command(["text","audiototext","lyrics"],  prefixes=["","+", ".", "/", "-", "?", "$","#","&"]))
async def chat(bot, message):
    
    try:
        start_time = time.time()
        await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
        if message.reply_to_message and message.reply_to_message.media:
            
            m = await message.reply_to_message.download(file_name="DAXX.mp3")
            audio_file = open(m, "rb")
            transcript = openai.Audio.transcribe("whisper-1", audio_file)
            x=transcript["text"]
            end_time = time.time()
            telegram_ping = str(round((end_time - start_time) * 1000, 3)) + " ᴍs"
            await message.reply_text(f"`{x}` \n ✨ᴛɪᴍᴇ ᴛᴀᴋᴇɴ {telegram_ping}")     
    except Exception as e:
        await message.reply_text(f"**ᴇʀʀᴏʀ: **  ` {e} `")



s = bytearray.fromhex("68747470733a2f2f6769746875622e636f6d2f56472d5445414d2f434841542d4750542f").decode()

  


if __name__ == "__main__":
    print(f""" {BOT_NAME} ɪs ᴀʟɪᴠᴇ!
    """)
    try:
        vikas.start()
        
        
    except (ApiIdInvalid, ApiIdPublishedFlood):
        raise Exception("Your API_ID/API_HASH is not valid.")
    except AccessTokenInvalid:
        raise Exception("Your BOT_TOKEN is not valid.")
    print(f"""JOIN [ 𝗬𝗢𝗨𝗥 𝗖𝗛𝗔𝗧𝗚𝗣𝗧 𝗕𝗢𝗧 𝗦𝗧𝗔𝗥𝗧]
    𝗧𝗛𝗜𝗦 𝗥𝗘𝗣𝗢 𝗠𝗔𝗗𝗘 𝗕𝗬 crazy 𝗧𝗘𝗔𝗠🥳
 {BOT_NAME} ɪs ᴀʟɪᴠᴇ!  
    """)
    idle()
    vikas.stop()
    print("vikas 𝗖𝗛𝗔𝗧𝗚𝗣𝗧 𝗕𝗢𝗧 𝗦𝗧𝗢𝗣 !")
