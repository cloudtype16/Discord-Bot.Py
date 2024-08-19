info = {
    'nombre': 'ping',
    'descripcion': 'Ping pong!',
}

async def run(interaccion, bot):
    await interaccion.response.send_message('Pong! 🏓')