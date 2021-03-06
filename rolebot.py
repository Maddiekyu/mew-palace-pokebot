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
@client.command(pass_context=True)
async def sha(ctx):
    #parse user's message
    message = ctx.message
    # split "%sha " from "[Pokemon Name]"
    pkmnName = message.content[5:].capitalize()
    #check if it is a valid pokemon name
    pkmnExists = pkmnName in pkmnSet
    def check(message): 
        return pkmnExists
    # if a role doesn't already exist, create it
    # otherwise, just add the role to the
    if pkmnExists:
        if not get(ctx.guild.roles, name = pkmnName):
            role = await ctx.guild.create_role(name=pkmnName)
        member = ctx.message.author
        role = discord.utils.get(member.guild.roles, name=pkmnName)
        # keep track of # of pokemon shiny hunted
        #hasRole = False
        #print("roleCount: ", roleCount)
        if role not in member.roles:
                await ctx.send(f"{member.mention} is now hunting **{role}**.")
                await ctx.author.add_roles(role)
                #hasRole = True

# sh remove role command
@client.command(pass_context=True)
async def shr(ctx):
    #parse user's message
    message = ctx.message
    # split "%shr " from "[Pokemon Name]"
    pkmnName = message.content[5:].capitalize()
    #check if it is a valid pokemon name
    pkmnExists = pkmnName in pkmnSet
    def check(message): 
        return pkmnExists
    # if a role doesn't already exist, create it
    # otherwise, just add the role to the
    if pkmnExists:
        if not get(ctx.guild.roles, name = pkmnName):
            role = await ctx.guild.create_role(name=pkmnName)
        member = ctx.message.author
        role = discord.utils.get(member.guild.roles, name=pkmnName)
        await ctx.send(f"{member.mention} is no longer hunting **{role}**.")
        await ctx.author.remove_roles(role)
            
client.run(os.getenv('TOKEN'))