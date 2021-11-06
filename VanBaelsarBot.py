#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import discord
import os
import json
import random
from dotenv import load_dotenv

#tTODO: Turn into .env file

load_dotenv()
token = os.getenv("TOKEN")
json_path = os.getenv("JSON_PATH")

client = discord.Client()

def main():
    global quotes
    json_data = json.load(open(json_path))
    quotes = json_data["quotes"]

if __name__ == "__main__":
    main()

@client.event
async def on_ready():
    print('I have reached Eorzea!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if "gaius" in message.content.lower():
        await message.channel.send(random.choice(quotes))
        return

client.run(token)