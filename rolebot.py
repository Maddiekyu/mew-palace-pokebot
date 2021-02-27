import discord
from discord.ext import commands

#Token for Discord Bot
TOKEN = 'HsuNc7WBeJsgIBs9Vkz2ROO5q-e5WN4K'

#Prefix for Discord will be %
client = commands.Bot(command_prefix='%')

#run bot using specified token
client.run(TOKEN)