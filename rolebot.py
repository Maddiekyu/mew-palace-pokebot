import discord
import pokebase as pb
from discord.ext import commands
import json
from pokemon_set import pokemonData
from pokebase.loaders import pokemon

TOKEN = 'HsuNc7WBeJsgIBs9Vkz2ROO5q-e5WN4K'

# Convert set to all lowercase
pkmnList = list(pokemonData)

pkmnList = [element.lower() for element in pkmnList]

pkmnSet = set(pkmnList)

def validate_user_input(userInput): 
    #userInput = input('Discord command: ').lower()
    print("UserInput:", userInput)
    pkmnName = userInput[4:].lower() #!sh Mimikyu
    print(pkmnName)
    if pkmnName in pkmnSet:
        return "found " + pkmnName
    else:
        raise ValueError("Invalid Name")

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
#client.run(TOKEN)