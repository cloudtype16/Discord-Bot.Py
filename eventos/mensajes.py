def run(bot):
    @bot.event
    async def on_message(m):
        
        print(list(bot.guilds))