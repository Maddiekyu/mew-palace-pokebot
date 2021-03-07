import discord
from discord.ext import commands
import discord.utils
from discord.utils import get
import json
from pokebase.loaders import pokemon
from dotenv import load_dotenv
import os

# Cog for managing the help command and all of our documentation needs.
class HelpDocumentation(commands.Cog):
    def __init__(self, client):
        self.client = client
        client.remove_command('help')

    @commands.Cog.listener()
    async def on_ready(self):
        print('Help Documentation Loaded.')

    # custom help command
    @commands.command(pass_context=True)
    async def help(self, ctx):
        embed = discord.Embed(colour = discord.Colour.blue())
        embed.set_author(name='Help Page')
        embed.set_author(name="MimiQT", icon_url='https://cdn.discordapp.com/attachments/817278897862213642/818012928162398228/darkmimi.jpg')
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/817278897862213642/818012928162398228/darkmimi.jpg')
        embed.add_field(name='&help', value='Displays this embed.', inline=False)
        embed.add_field(name='&sha', value='Add Shiny Hunt.', inline=False)
        embed.add_field(name='&shr', value='Remove Shiny Hunt.', inline=False)
        embed.add_field(name='&ping', value='Displays bot latency.', inline=False)
        embed.add_field(name='&host', value='[Raid Hosts Only] Creates a private channel for Pokemon Max Raid Battles.', inline=False)
        await ctx.author.send(embed = embed)
#         await ctx.send("""```&help - Shows this message. 
# &sha [Pokemon name] - Add shiny hunt. 
# &shr [Pokemon name] - Remove shiny hunt.
# &ping - Returns latency of MimiQT.```""")

def setup(client):
    client.add_cog(HelpDocumentation(client))

