import discord
import asyncio
import chalk
import aiohttp
import pyaudio
import speech_recognition as sr 
from discord.ext import commands
from discord.ext.commands import Bot

client = discord.Client()
r = sr.Recognizer()

async def backgroundprocess() :
    channelnum = 'ChannelNumber'
    await client.wait_until_ready()
    while not client.is_closed:
        with sr.Microphone() as source:
            print("Say something");
            audio = r.listen(source)
            #await client.send_message(client.get_channel('ChannelNumber'), r.recognize_google(audio))
            try:
                await client.send_message(client.get_channel('ChannelNumber'), r.recognize_google(audio))
            except:
                pass;

@client.event
async def on_ready():
    client.loop.create_task(backgroundprocess())

client.run('BotTokenHere')
