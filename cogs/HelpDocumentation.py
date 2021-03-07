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
        await ctx.send("""```&help - Shows this message. 
&sha [Pokemon name] - Add shiny hunt. 
&shr [Pokemon name] - Remove shiny hunt.
&ping - Returns latency of MimiQT.```""")

def setup(client):
    client.add_cog(HelpDocumentation(client))

