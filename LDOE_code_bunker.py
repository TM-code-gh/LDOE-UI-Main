# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 18:21:15 2021

@author: theom
"""

import os
import discord
import nest_asyncio #utile pour running event loop

from dotenv import load_dotenv

nest_asyncio.apply()
client = discord.Client()

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

@client.event #decorateur
async def on_ready(): #async == co routine
    print("Le bot est prêt !")

@client.event
async def on_message(message):
    if message.content == "Ping":
        await message.channel.send("code bunker") #await == co routine

client.run(TOKEN)