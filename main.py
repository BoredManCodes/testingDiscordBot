import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    activity = discord.Game(name="Python")
    await client.change_presence(status=discord.Status.online, activity=activity)
    print(f'{client.user} has connected to Discord!')

# @client.event
# async def on_message(message):
#     if message.content == 'What is the server IP?':
#         response = 'Server is currently in updating mode, so there is no IP for now.'
#         await message.channel.send(response)

@client.event
async def on_message(ctx, message):
    if message.content == ',testing':
        embed = discord.Embed(title="Server is in Update mode", description="Server is currently in update mode so there is no IP published.", color=0x5dc60b)
        embed.set_footer(text="Bot is by Endas#4959")
        await ctx.send(embed=embed)


client.run("TOKEN")
