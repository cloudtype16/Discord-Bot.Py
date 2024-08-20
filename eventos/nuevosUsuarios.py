def run(bot):
    @bot.event
    async def on_memeber_join(m):
        print(m)