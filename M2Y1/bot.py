import discord
from discord.ext import commands
import os
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

#Мемы про программистов

@bot.command('programem')
async def cmd_programem(ctx):
    lst = os.listdir('programmem')
    with open(f'programmem/{random.choice(lst)}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


#Мемы с Хазяевами

@bot.command('hazz')
async def cmd_hazz(ctx):
    lst = os.listdir('hazz')
    with open(f'hazz/{random.choice(lst)}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


#Мемы с котиками

@bot.command('kitten')
async def cmd_kitten(ctx):
    lst = os.listdir('kittensu')
    with open(f'kittensu/{random.choice(lst)}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

bot.run('')
