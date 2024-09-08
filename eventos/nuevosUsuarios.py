def run(bot):
    @bot.event
    async def on_member_join(m):
        guild = list(bot.guilds)
        print(guild['id'])
        
        if guild == '924395185343971358':
            print('ey')