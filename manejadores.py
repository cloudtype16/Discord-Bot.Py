import discord
import json
from os import walk
import sys

def comandos_slash(bot):
    config = json.load(open('config.json'))
    folder_comandos = config['folder_comandos']

    sys.path.append(f'./{folder_comandos}')
    comandos = []
    informacion = []

    for (dirpath, dirname, filesnames) in walk(f'./{folder_comandos}'):
        for x in filesnames:
            if not x[-3:] == '.py':
                break
            comandos.append(x[:-3])
            util = __import__(x[:-3])
            if hasattr(util, 'info'):
                informacion.append(util.info)
            else: 
                print('El comando '+x+' no tiene el objeto de información.')
        break

    for c in informacion:
        @bot.tree.command(name=c['nombre'], description=c['descripcion'])
        async def ping(interaction: discord.Interaction):
            comando = interaction.command.name
            
            if comando in comandos:
                modulo = __import__(comando)
                await modulo.run(interaction, bot)