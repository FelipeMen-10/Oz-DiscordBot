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
    "https://media.giphy.com/media/xT5LMHxhOfscxPfIfm/giphy.gif",
    "https://tenor.com/view/cat-tired-sleepy-coffee-coffee-cup-gif-16510344054637063999",
    "https://tenor.com/view/love-quotes-for-him-gif-16167903662682316231",
    "https://tenor.com/view/good-morning-bom-dia-erss-ednastochi-gato-gif-13884175848341330513"
]

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members         = True
bot     = commands.Bot(command_prefix='$', intents=intents)

horario = time(hour=8, minute=0)

@tasks.loop(time=horario)
async def bom_dia():
    canal_id = 1482196299918086287
    canal = bot.get_channel(canal_id)
    if canal:
        gif = random.choice(gifs)
        await canal.send("Bom dia, pessoal ☀️")
        await canal.send(gif)

@bot.event
async def on_member_join(member):
    await member.send(f"Bem-Vindo(a) ao servidor, {member.name}")

@bot.command()
async def ola(ctx):
    await ctx.send(f"Fala trutinha, {ctx.author.mention} <3")

@bot.command()
async def morre(ctx):
    try:
        await ctx.author.send("AQUI É OZ PORRA, MORRE NUNCA!!!")
        await ctx.author.send("https://tenor.com/view/joo-jew-jewl-s4j78-gif-5651286586900019647")
        await ctx.send("Fala, maninho... mandei uma dm pra você rsrs")
    except discord.Forbidden:
        await ctx.send("Da pra me desbloquear seu bosta, arruma essas config ai")

@bot.command()
async def pedro(ctx):
    pedro_user = await bot.fetch_user(273253850104856576)

    await ctx.send(f"O {pedro_user.mention} quis o meu pior, ou seja, busquem o pior pra ele...")
    await ctx.send(file=discord.File('img/pedro_morre.png'))
    await ctx.send(file=discord.File('img/casa_pedro.png'))

@bot.event
async def on_ready():
    print(f"Bora trabalhar, {bot.user.name}!")
    if not bom_dia.is_running():
        bom_dia.start()

bot.run(token, log_handler=handler, log_level=logging.DEBUG)
