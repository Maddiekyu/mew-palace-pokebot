import discord
import pypokedex
import constant
from discord.ext import commands
from pypokedex import pokemon

# For testing purposes only:
userInput = input("Enter the Pokemon you want to shiny hunt: ")
print(userInput)

# # Validate User Input Function
# def validate_user_input():
#     userInput = message




# Constants
POKETWO_TOTAL = 809

# Token for Discord Bot
TOKEN = 'HsuNc7WBeJsgIBs9Vkz2ROO5q-e5WN4K'

# Prefix for Discord will be %sh
# Format: %sh Mimikyu
client = commands.Bot(command_prefix='%')

# Fill map with {pokedex #, pokemon} key value pairs
# API call for Pokemon data.
# https://pypi.org/project/pypokedex/
pokemonNames = []
index = 0
for i in range(1, POKETWO_TOTAL):
    pokemonNames.append(pypokedex.get(dex = i))

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

if userInput in pokemonNames:
    print("Yes, it exists")
else:
    print("No, it does not exist")

# @client.command(pass_context=True)
# async def loot(ctx,*,message):
#     await client.say(message)

# @client.event
# async def on_message(message):
#     if message.content.startswith(f"%sh"):
#         validate_user_input()
        





#run bot using specified token
client.run(TOKEN)