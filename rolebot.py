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
client = commands.Bot(command_prefix='%', intents = discord.Intents.all())

client.remove_command('help')

# custom help command
@client.command(pass_context=True)
async def help(ctx):
   await ctx.send("""```%help - Shows this message. 
%sha [Pokemon name] - Add shiny hunt. 
%shr [Pokemon name] - Remove shiny hunt.```""")

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
        roleSet = {get(member.roles, name = n) for n in pkmnSet}
        # limit users to 1 shiny hunt
        if role not in member.roles:
            if len(roleSet) < 2:
                await ctx.send(f"{member.mention} is now hunting **{role}**.")
                await ctx.author.add_roles(role)
            else:
                await ctx.send("You may only shiny hunt one Pokemon at a time.") 
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
        # if not get(ctx.guild.roles, name = pkmnName):
        #     role = await ctx.guild.create_role(name=pkmnName)
        member = ctx.message.author
        role = discord.utils.get(member.guild.roles, name=pkmnName)

        if role in member.roles:
            await ctx.send(f"{member.mention} is no longer hunting **{role}**.")
            await ctx.author.remove_roles(role)
        print("which role got deleted?", role)
        print("how many users have this role? ", len(role.members))
        if len(role.members) == 0:
            print("which role is getting deleted?", role)
            await role.delete()

@sha.error
async def sha_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please specify a Pokemon to shiny hunt.")

@shr.error
async def shr_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please specify a Pokemon to shiny hunt.")
            
client.run(os.getenv('TOKEN'))