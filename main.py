import discord
from discord.ext import commands

description = """
An example bot to showcase the discord.ext.commands extension module.
There are a number of utility commands being showcased here.
"""
bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"))
intents = discord.Intents.default()
intents.members = True
bot = discord.Bot(intents=intents)

# List all Cogs
initial_extensions = [
                      'cogs.misc'
                      ] 

# # Load the Cogs into the Bot
if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("------")

with open('c:\\tools\\token.txt', 'r') as f:
    token = f.read().strip()
bot.run(token)