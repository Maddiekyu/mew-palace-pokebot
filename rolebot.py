import discord
from discord.ext import commands
import discord.utils
from discord.utils import get
import json
from pokemon_set import pokemonData, pkmnSet
from pokebase.loaders import pokemon
from dotenv import load_dotenv
import os

#Discord Bot Token
#Credentials
load_dotenv('.env')

# prefix will be %
client = commands.Bot(command_prefix='^', intents = discord.Intents.all())

client.remove_command('help')

# custom help command
@client.command(pass_context=True)
async def help(ctx):
   await ctx.send("""```^help - Shows this message. 
^sha [Pokemon name] - Add shiny hunt. 
^shr [Pokemon name] - Remove shiny hunt.
^ping - Returns latency of MimiQT.```""")

#load cog
@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

#unload cog
@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(os.getenv('TOKEN'))