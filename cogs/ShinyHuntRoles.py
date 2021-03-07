import discord
import pokebase as pb
from discord.ext import commands
import discord.utils
from discord.utils import get
import json
from pokemon_set import pokemonData, pkmnSet
from pokebase.loaders import pokemon
from dotenv import load_dotenv
import os

# Cog for managing the Poketwo Shiny Hunt commands.
class ShinyHuntRoles(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Shiny Hunt Commands loaded.')

    # sh add role command
    @commands.command(pass_context=True)
    async def sha(self, ctx):
        # parse user's message
        message = ctx.message
        # split "%sha " from "[Pokemon Name]"
        pkmnName = message.content[5:].capitalize()
        # check if it is a valid pokemon name
        pkmnExists = pkmnName in pkmnSet

        def check(message):
            return pkmnExists
        # if a role doesn't already exist, create it
        # otherwise, just add the role to the
        if pkmnExists:
            if not get(ctx.guild.roles, name=pkmnName):
                role = await ctx.guild.create_role(name=pkmnName, mentionable=True)
            member = ctx.message.author
            role = discord.utils.get(member.guild.roles, name=pkmnName)
            roleSet = {get(member.roles, name=n) for n in pkmnSet}
            # limit users to 1 shiny hunt
            if role not in member.roles and len(roleSet) < 3:
                await ctx.author.add_roles(role)
                await ctx.send(f"{member.mention} is now hunting **{role}**.")
            else:
                await ctx.send("You may only shiny hunt two Pokemon at a time.")

    #remove shiny hunt
    @commands.command(pass_context=True)
    async def shr(self, ctx):
        # parse user's message
        message = ctx.message
        # split "%shr " from "[Pokemon Name]"
        pkmnName = message.content[5:].capitalize()
        # check if it is a valid pokemon name
        pkmnExists = pkmnName in pkmnSet

        def check(message):
            return pkmnExists
        # if a role doesn't already exist, create it
        # otherwise, just add the role to the
        if pkmnExists:
            member = ctx.message.author
            role = discord.utils.get(member.guild.roles, name=pkmnName)

            if role in member.roles:
                await ctx.send(f"{member.mention} is no longer hunting **{role}**.")
                await ctx.author.remove_roles(role)

            if len(role.members) == 0:
                await role.delete()

    @sha.error
    async def sha_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please specify a Pokemon to shiny hunt.")

    @shr.error
    async def shr_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please specify a Pokemon to shiny hunt.")


def setup(client):
    client.add_cog(ShinyHuntRoles(client))

