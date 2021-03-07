import discord
from discord.ext import commands
import discord.utils
from discord.utils import get
import json
from pokebase.loaders import pokemon
from dotenv import load_dotenv
import os


class GeneralCommands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Pokemon Data Loaded.')

    @commands.command
    async def ping(self, ctx):
        await ctx.send(f'Ping: {round(self.client.latency * 1000)} ms')

    @commands.command(pass_context=True)
    async def say(self, ctx, message=None): 
        await ctx.send(message)

def setup(client):
    client.add_cog(GeneralCommands(client))
