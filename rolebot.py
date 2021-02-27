import discord
import pypokedex
import constant
from discord.ext import commands

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

# Run user input against map.
# If a match exists, then add role to user.
# If no match exists, then throw an error and
# prompt the user to try again, specifying
# the correct format.
# @client.event
# async def on_message(message):
#     if message.content.startswith(f"%sh"):
        





#run bot using specified token
client.run(TOKEN)