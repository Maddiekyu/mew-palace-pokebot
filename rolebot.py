import discord
from discord.ext import commands
import discord.utils
from discord.utils import get
import json
from dotenv import load_dotenv
import os

#Discord Bot Token
#Credentials
load_dotenv('.env')

# prefix will be %
client = commands.Bot(command_prefix='&', intents = discord.Intents.all())

# Load cog.
@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

# Unload cog.
@ client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

# Execute all cogs in cogs folder.
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(os.getenv('TOKEN'))