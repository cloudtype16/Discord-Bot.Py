def run(bot):
    @bot.event
    async def on_ready():
            
        print(f'Se a iniciado correctamente {bot.user.name}')
        await bot.tree.sync()