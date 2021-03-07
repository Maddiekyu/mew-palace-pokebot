import discord
from discord.ext import commands
import discord.utils
from discord.utils import get
import json
from pokebase.loaders import pokemon
from dotenv import load_dotenv
import os

# Cog for the Raid Host Private Room feature.
class RaidHost(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Raid Host Commands Loaded.')

    @commands.command(pass_context=True)
    async def host(self, ctx):
        guild = ctx.message.guild
        # Parse user's message.
        message = ctx.message
        print("message: ", message)
        # Split "&host " from "[Desired Channel Name]".
        raidChannelName = message.content[6:].lower()
        print("Raid Name: ", raidChannelName)
        await guild.create_text_channel(raidChannelName)

def setup(client):
    client.add_cog(RaidHost(client))