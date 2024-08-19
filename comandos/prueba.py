info = {
    'nombre': 'prueba',
    'descripcion': 'Comando de prueba!',
}

async def run(interaccion, bot):
    await interaccion.response.send_message('Prueba!')