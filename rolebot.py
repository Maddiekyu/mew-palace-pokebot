import discord
from discord.ext import commands

#Token for Discord Bot
TOKEN = 'HsuNc7WBeJsgIBs9Vkz2ROO5q-e5WN4K'

#Prefix for Discord will be %sh
#Format: %sh Mimikyu
client = commands.Bot(command_prefix='%')

#Pseudocode
#API call for Pokemon data.
#Run user input against map.
#Time Complexity: O(log N)

#If a match exists, then add role to user.
#If no match exists, then throw an error and
#prompt the user to try again, specifying
#the correct format.

#run bot using specified token
client.run(TOKEN)