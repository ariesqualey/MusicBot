# bot.py

#import os
import discord
#from dotenv import load_dotenv

#load_dotenv()
#TOKEN = os.getenv('DISCORD_TOKEN')
TOKEN = 'OTQxNDA3MDg1OTYxMzA2MTIz.YgVfqw.6dVo3x96SqIrwWDSgQ9zXTdPr7E'
GUILD = 'Dio Fan Club (ENLARGED)'

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    
client.run(TOKEN)
