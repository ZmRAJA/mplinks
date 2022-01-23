from os import environ
import aiohttp
import re
import requests
from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler

API_ID = environ.get('API_ID')
API_HASH = environ.get('API_HASH')
BOT_TOKEN = environ.get('BOT_TOKEN')
API_KEY = environ.get('API_KEY', '4lZuNhed0dhdpG414MWn')

bot = Client(' ModsApkRoBot',
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
             workers=50,
             sleep_threshold=10)


@bot.on_message(filters.command('start') & filters.private)
async def start(bot, message):
    await message.reply(
        f"**Hi {message.chat.first_name}!**\n\n"
        "I'm Mdisk link converter bot. Just send me link and get converted link of mdisk.\n\n Created By @steallootdeal")

@bot.on_message(filters.command('help') & filters.private)
async def help(bot, message):
    await message.reply(
        f"**This is our Help Page {message.chat.first_name}!**\n\n"
        "If your had **deployed bot** succesfully then you have to do nothing to use this bot\n\n **Just Simply send Any mdisk Link in Any Format**\n -Shortend Url\n -Cofile url\n\n __Both url are accepted__ \n\n"
        "**Demo Of Urls**\n **Bit.ly Shortened Url**\n https://bit.ly/38NEpVu \n\n **Mdisk Official Shorten Link** \n https://mdisk.me/convertor/2x3/MZdAES \n\n"
        "**Long Url** - https://mypowerdisk.com/mybox/share?id=9053ccdb11daeffdb34471c44cc086ee30b5")

@bot.on_message(filters.private)
async def link_handler(bot, message):
    stringliteral = message.text
    Link = (re.search("(?P<url>https?://[^\s]+)", stringliteral).group("url"))
    session = requests.Session()
    resp = session.head(Link, allow_redirects=True)
    short_link = await post_shortlink(resp.url)
    shortlink = ('https://mdisk.me/convertor/'+short_link)
    txt = stringliteral.replace(Link, shortlink)
    try:
        await message.reply(f'{txt}', quote=True)
    except Exception as e:
        await message.reply(f'Error: {e}', quote=True)


async def post_shortlink(Link):
    url = 'https://diskuploader.mypowerdisk.com/v1/tp/cp'
    param = {'token': '4lZuNhed0dhdpG414MWn','link':'https://mdisk.me/convertor/2x3/MZdAES'
} 
res = requests.post(url, json = param)
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params, raise_for_status=True) as response:
            data = await response.json()
            print(data["data"].get("item_id"))
            return data["data"].get("item_id")
 

bot.run()
