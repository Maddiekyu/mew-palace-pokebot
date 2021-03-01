import discord
import pokebase as pb
from discord.ext import commands
import json
from pokemon_set import pokemonData
from pokebase.loaders import pokemon

TOKEN = ''

pkmnList = list(pokemonData)

pkmnList = [element.lower() for element in pkmnList]

pkmnSet = set(pkmnList)

userInput = input('Discord command: ').lower()
def validate_user_input(userInput):
    if userInput in pkmnSet:
        print("found", userInput)
    else:
        raise ValueError('INVALID INPUT')

validate_user_input(userInput)

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
#client.run(TOKEN)