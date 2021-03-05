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
    pkmnName = message.content[5:].lower()
    #check if it is a valid pokemon name
    pkmnExists = pkmnName in pkmnSet
    def check(message): 
        return pkmnExists
    # if a role doesn't already exist, create it
    # otherwise, just add the role to the
    if pkmnExists:
        if not get(ctx.guild.roles, name = pkmnName):
            new_role = await ctx.guild.create_role(name=pkmnName)
        member = ctx.message.author
        new_role = discord.utils.get(member.guild.roles, name=pkmnName)
        old_role = (get(ctx.guild.roles, name = n) for n in pkmnSet)
        await ctx.send(f"{member.mention} is now hunting {new_role.mention}.")
        if old_role in member.roles:
            await ctx.author.remove_roles(member,*old_role)
            await ctx.send(f"{member.mention} is no longer hunting {new_role.mention}.")
        await member.add_roles(new_role)

# sh remove role command
@client.command(pass_context=True)
async def shr(ctx):
    #parse user's message
    message = ctx.message
    # split "%shr " from "[Pokemon Name]"
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
        member = ctx.message.author
        role = discord.utils.get(member.guild.roles, name=pkmnName)
        await ctx.send(f"{member.mention} is no longer hunting {role.mention}.")
        await member.remove_roles(role)
            
client.run(os.getenv('TOKEN'))