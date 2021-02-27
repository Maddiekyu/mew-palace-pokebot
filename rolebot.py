import discord
from discord.ext import commands

#Token for Discord Bot
TOKEN = ''

#Prefix for Discord will be %
client = commands.Bot(command_prefix='%')

#run bot using specified token
client.run(TOKEN)