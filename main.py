import discord
import os

client = discord.Client()

@client.event
async def on_ready():
   print("on ready event")

client.run(os.environ.get("DISCORD_TOKEN"))
