import discord
from discord.ext import commands

TOKEN = ''

client = commands.Bot(command_prefix='%')

@client.command(pass_context=True)
async def add_role(ctx):
    member = ctx.author
    role = discord.utils.get(member.guild.roles, name="Bots")
    await member.add_roles(role)

client.run(TOKEN)