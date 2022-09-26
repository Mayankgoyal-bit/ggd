import logging
import re
import json

from aiogram import *

import asyncio

import time

from aiogram.types import chat_permissions, inline_keyboard

import requests

from bs4 import BeautifulSoup

import random

import urllib.parse

from datetime import datetime, timedelta

import string

Admin = '@Naman1357'

BotName = 'Chegg unblur by MG'

mainGroupId = -1001745107278

adminGroupId = -1001179487467

logsGroupId = -1001664380876

adminId = 1703027575

botLink = "https://t.me/cheggcheapunblurbot"

username = urllib.parse.quote_plus('MAYANK')

password = urllib.parse.quote_plus('MAYANK')

# url = "mongodb+srv://%s:%s@premiumwarrior.jmt0s.mongodb.net/tgdata"

# cluster = MongoClient(url % (username, password))

# db = cluster["tgdata"]

# collection = db["tgusers"]

# API_TOKEN = '1834750087:AAFfudHVQ5vb-ZyiJr0errhBmUWanleTpo8'

API_TOKEN = '5521462967:AAEnpNpuuGbMpS447sZiGe0zv6mouTROgUs'

# Configure logging

logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher

bot = Bot(token=API_TOKEN)

client = Dispatcher(bot)

@client.message_handler(commands=['start', 'help'])

async def send_welcome(message: types.Message):

    print(message.chat.id)

    await message.reply(f"\n\n Hi!\n\n This is {BotName} \n\n want to buy premium contact {Admin} \n\n 4) /mydata to check your validity")

# @client.message_handler(commands=['price'])

# async def udata(message: types.Message):

#     price_message = "**PRICES AND PACKAGES LIST**\n\n=>285₹ or 4$ for 30days : Unlimited solutions.\n\n=>200₹ 0r 3$ for 15days : unlimited solutions\n\n=>100₹ or 2$ for 10days : unlimited solutions"

#     await message.reply(price_message)

# @client.message_handler(commands=['pay'])

# async def udata(message: types.Message):

#     price_message = "**HOW TO PAY?**\n\n**FOR INDIAN MEMBERS**\n\n1)Check Prices by using this command /price\n\n2)select your package and pay the money to this UPI Id : jaffa4321@apl\n\n3)After your payment completed send screen short to Owner {Admin}\n\nYour package will added as soon as owner sees the screenshort\n\nThat's it Thankyou."

#     await message.reply(price_message)

# @client.message_handler(commands=['tutorial'])

# async def udata(message: types.Message):

#     price_message = "**TUTORIAL**\n\nAfter Your payment completed check this video\n\n "

#     await message.reply(price_message)

all_genid = []

lock_permissions = {

    'can_send_messages': False,

    'can_send_media_messages': None,

    'can_send_polls': None,

    'can_send_other_messages': None,

    'can_add_web_page_previews': None,

    'can_change_info': None,

    'can_invite_users': None,

    'can_pin_messages': None

}

unlock_permissions = {

    'can_send_messages': True,

    'can_send_media_messages': None,

    'can_send_polls': None,

    'can_send_other_messages': None,

    'can_add_web_page_previews': None,

    'can_change_info': None,

    'can_invite_users': None,

    'can_pin_messages': None

}

s = requests.Session()

cookie_list = [{

    'user-agent':

    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',

    'cookie': 'cheata=gpv=7&ckp=tld&dm=chegg.com&apv_79_www33=7&cpv_79_www33=7',

    'origin': 'https://www.chegg.com',

    'accept': 'application/json',

    'content-type': 'application/json',

    "cache-control": "max-age=0",

    "deviceFingerPrintId": "web|A0oUFYO50M5NYadliOz5"

}]

@client.message_handler(commands=['statues', 's'])

async def account_statues(message: types.Message):

    for i, item in enumerate(cookie_list):

        req = requests.get("https://www.chegg.com/homework-help/questions-and-answers/simulate-following-circuit-qucs-save-simulation-file-results-pdf-file-submit-e-learning-sh-q50117215?trackid=ef79e9639575&strackid=2b896ff805f6", headers=item)

        soup = BeautifulSoup(req.content, 'html.parser')

        qution = soup.find(

            "div", {"class": "ugc-base question-body-text"}, 'html.parser')

        answer = soup.find(

            "div", {"class": "answer-given-body ugc-base"}, 'html.parser')

        if answer == None:

            await message.reply(f"{i} account Notworking")

        else:

            await message.reply(f"{i} account is working")

def remove_tags(html):

    # parse html content

    soup = BeautifulSoup(html, "html.parser")

    for data in soup(['style', 'script']):

        # Remove tags

        data.decompose()

    soup.find("h2", {"class": "guidance-header"}).decompose()

    soup.find("section", {"id": "general-guidance"}).decompose()

    soup.find("div", {"id": "select-view"}).decompose()

    # return data by retrieving the tag content

    return soup

@client.message_handler()

async def chegg(message: types.Message, amount=1):

       if message.chat.id == mainGroupId:

           if "https://www.chegg.com"in message.text:

               await bot.send_message(1703027575,f'{message.text}\nUsername : {message.from_user.username}\nId:{message.message_id}')

                                  

       if 'https://fanswer.me'in message.text:

          link =re.findall(r'(https:\/\/fanswer\.me\/.+)[\s\S]+Username\s?:\s?(\@\w+|\w+)[\s\S]+Id\s?:\s?(\d+)[\s\S]',message.text,re.MULTILINE)
          print(link)
          cl= requests.get(url=link[0][0])
          print('done')
          soup = BeautifulSoup(cl.content,'html.parser')

          img= soup.find_all('img')

          for tag in img:

              tag["src"]='https:'+tag["src"]

          c= open("answer.html",'w')

          c.write(str(soup))

          c.close()

          c= open('answer.html','rb')

          

          await bot.send_document(mainGroupId,c,caption=f'@{link[0][2]}-Your solution is here\nAnswer by @')

if __name__ == '__main__':

    executor.start_polling(client, skip_updates=True)
