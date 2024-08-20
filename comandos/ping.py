info = {
    'nombre': 'ping',
    'descripcion': 'Ping Pong!',
}

async def run(interaccion, bot):
    await interaccion.response.send_message('Pong! 🏓')