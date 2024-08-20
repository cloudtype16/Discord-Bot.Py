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
        async def comando(interaction: discord.Interaction):
            comando = interaction.command.name
            
            if comando in comandos:
                modulo = __import__(comando)
                await modulo.run(interaction, bot)

def eventos(bot):
    config = json.load(open('config.json'))
    folder_eventos = config['folder_eventos']

    sys.path.append(f'./{folder_eventos}')
    eventos = []
    informacion = []

    for (dirpath, dirname, filesnames) in walk(f'./{folder_eventos}'):
        for x in filesnames:
            if not x[-3:] == '.py':
                break
            eventos.append(x[:-3])

    for e in eventos:
        evento = __import__(e)
        evento.run(bot)