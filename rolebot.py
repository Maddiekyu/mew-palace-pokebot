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

@client.command()
async def role(ctx, * role: discord.Role):
    user = ctx.message.author
    await user.add_roles(role)

@client.event
async def on_message(message):
    if message.content.startswith('%sh'):
        channel = message.channel
        #await channel.send('Hello there!')

        def check(message):
            pkmnName = message.content[4:].lower()
            #print("Pokemon is:", pkmnName) 
            return pkmnName in pkmnSet    
        
        msg = await client.wait_for('message', check=check)
        if(check):
            await channel.send('Hello {.author}! Your input is valid! :)'.format(msg))
        else:
            await channel.send('Sorry {.author}! Your input is invalid! :('.format(msg))

        

# check if the user's input is a valid Pokemon name.
# def validate_user_input(userInput): 
#     #userInput = input('Discord command: ').lower()
#     #print("UserInput:", userInput)
#     pkmnName = userInput[4:].lower() #!sh Mimikyu
#     #print(pkmnName)
#     if pkmnName in pkmnSet:
#         return "found " + pkmnName
#     else:
#         raise ValueError("Invalid Name")

#print("Result of validate:", validate_user_input(userInput))

# Pseudocode
# if message starts with "%sh"
#   validate_user_input()
#   Run user input against map.
#   If a match exists, 
#       if role doesn't exist
#           create role
#       else
#           add role to user
# If no match exists
#   throw an error 
#   prompt the user to try again: correct format.  

#run bot using specified token
client.run(os.getenv('TOKEN'))