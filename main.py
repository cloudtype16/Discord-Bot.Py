import discord
from discord.ext import commands
import json
from os import walk
import sys
import manejadores 

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

config = json.load(open('config.json'))

token_bot = config['token_bot']

@bot.event
async def on_ready():
    print(f'Se a iniciado correctamente {bot.user.name}')
    await bot.tree.sync()
        
manejadores.comandos_slash(bot)

bot.run(token_bot)

