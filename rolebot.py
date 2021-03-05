import discord
import pokebase as pb
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
client = commands.Bot(command_prefix='%')

@client.event
async def on_ready():
        print('Bot is ready.')

# sh add role command
@client.command()
async def sha(ctx, message):
    #parse user's message
    @client.event
    async def on_message(message):
        channel = message.channel
        # split "%sh " from "[Pokemon Name]"
        pkmnName = message.content[5:].lower()
        #check if it is a valid pokemon name
        pkmnExists = pkmnName in pkmnSet
        def check(message): 
            return pkmnExists
        # if a role doesn't already exist, create it
        # otherwise, just add the role to the
        if pkmnExists:
            if not get(ctx.guild.roles, name = pkmnName):
                role = await ctx.guild.create_role(name=pkmnName)
            else:
                member = ctx.message.author
                role = discord.utils.get(member.guild.roles, name=pkmnName)
            await ctx.author.add_roles(role)
            
client.run(os.getenv('TOKEN'))