import discord
import pokebase as pb
from discord.ext import commands
import json

#For testing purposes only:
# userInput = input("Enter the Pokemon you want to shiny hunt: ")
# print(userInput)

#convert JSON to dict
with open('pokemon.json') as json_file:
    pokemonData = json.load(json_file)

# print(type(pokemonData))
# print("\nPokemon 1:", pokemonData['bulbasaur']) 
# print("Length of pokemonData: ", len(pokemonData))
# print("\nPokemon 2:", pokemonData['ivysaur']) 

for key, value in pokemonData:
    userInput = input('Enter a Pokemon Name: ')
    if userInput == value
        print(userInput, "exists in dictionary")
    else
        print("INVALID INPUT, PLEASE TRY AGAIN")

# Validate User Input Function
def validate_user_input(userInput):
    return "hello world"
    
# Constants
# POKETWO_TOTAL = 898

# Token for Discord Bot
# TOKEN = 'HsuNc7WBeJsgIBs9Vkz2ROO5q-e5WN4K'

# Prefix for Discord will be %sh
# Format: %sh Mimikyu
# client = commands.Bot(command_prefix='%')

# Fill map with {pokedex #, pokemon} key value pairs
# API call for Pokemon data.
# pokemonNames = []
# index = 0
# #pokeName = pypokedex.pokemon.Pokemon()
# for i in range(1, POKETWO_TOTAL + 1):
#     pokemonNames.append(pb.pokemon(i))
#     print(pokemonNames[i - 1])

# print(type(pokemonNames[1]))
# print(pokemonNames[1])

# pokeName = pypokedex.pokemon.Pokemon.name
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

# if userInput in pokemonNames:
#     print("Yes, it exists")
# else:
#     print("No, it does not exist")

# @client.command(pass_context=True)
# async def loot(ctx,*,message):
#     await client.say(message)

# @client.event
# async def on_message(message):
#     if message.content.startswith(f"%sh"):
#         validate_user_input()
        





#run bot using specified token
#client.run(TOKEN)