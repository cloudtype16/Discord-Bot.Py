import discord
from discord.ext import commands
import json
import manejadores 

intents = discord.Intents.default().all()
# intents.message_content = True
# intents.members = True


bot = commands.Bot(command_prefix='!', intents=intents)

config = json.load(open('config.json'))

token_bot = config['token_bot']

manejadores.comandos_slash(bot)
manejadores.eventos(bot)

bot.run(token_bot)