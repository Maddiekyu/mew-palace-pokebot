import discord
import pokebase as pb
from discord.ext import commands
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