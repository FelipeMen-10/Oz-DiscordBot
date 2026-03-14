import discord
from discord.ext import commands, tasks
import logging
from dotenv import load_dotenv
import os
import random
from datetime import time

load_dotenv()

token = os.getenv('DISCORD_TOKEN')

gifs = [
    "https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif",
    "https://media.giphy.com/media/3oriO0OEd9QIDdllqo/giphy.gif",
    "https://media.giphy.com/media/26BRv0ThflsHCqDrG/giphy.gif",
    "https://media.giphy.com/media/xT5LMHxhOfscxPfIfm/giphy.gif"
]

handler                 = logging.FileHandler( filename = 'discord.log', encoding = 'utf-8', mode = 'w' )
intents                 = discord.Intents.default()
intents.message_content = True
intents.members         = True

bot = commands.Bot( command_prefix = '$', intents = intents )

horario = time(hour=6, minute=0)

@tasks.loop(time=horario)
async def bom_dia():
    canal_id = 1482196299918086287
    canal = bot.get_channel(canal_id)

    gif = random.choice(gifs)

    await canal.send("Bom dia, @everyone ☀️")
    await canal.send(gif)

@bot.event
async def on_member_join(member):
    await member.send(f"Bem-Vindo(a) ao servidor, {member.name}")

@bot.command()
async def ola(ctx):
    await ctx.send(f"Fala trutinha, {ctx.author.mention} <3")

@bot.event
async def on_ready():
    print(f"Bora trabalhar, {bot.user.name}!")
    bom_dia.start()

bot.run(token, log_handler = handler, log_level = logging.DEBUG )