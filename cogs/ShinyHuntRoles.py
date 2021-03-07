import discord
from discord.ext import commands

class ShinyHuntRoles(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is online.')
    
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Ping: {round(self.client.latency * 1000)} ms')
    
def setup(client):
    client.add_cog(ShinyHuntRoles(client))