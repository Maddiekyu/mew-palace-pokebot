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

    @commands.command(name = 'host', pass_context = True, invoke_without_command = True)
    @commands.has_role("🌟Raid Host🌟")
    async def host(self, ctx):
        guild = ctx.message.guild
        # Parse user's message.
        message = ctx.message
        # Split "&host " from "[Desired Channel Name]".
        raidChannelName = message.content[6:].lower()
        # Overwrite permissions.
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(read_messages=False),
            guild.me: discord.PermissionOverwrite(read_messages=True)
        }

        # Create private channel.
        hostChannel = await guild.create_text_channel(raidChannelName, overwrites = overwrites, category = ctx.guild.categories[1])

        # Welcome to shiny mimikyu
        # Following are the available bot commands that you can use. Please note that all commands must be executed from this channel.
        # &mute @username
        # Revokes the user's right to speak in this channel.
        # &unmute @username
        # Allows the user to speak in this channel again.
        # &ban @username
        # Removes the user from this channel.
        # &unban @username
        # Allows the user to join this channel again.
        # &lock
        # Locks the channel which blocks further users from joining. Keep in mind that you can't unlock it and hosting hours will not be tracked after.
        # &delete
        # Removes this room permanently along with all the messages/users.
        # Don't forget to delete this channel once you are finished hosting!
    @host.error
    async def host_error(self, ctx, error):
        if isinstance(error, commands.MissingRole):
            await ctx.send("Sorry, only Raid Hosts are allowed to use this command.")
    
    # Mute users in raid channel.
    @commands.command(name = 'mute', pass_context = True)
    async def mute(self, ctx, member: discord.Member):
        await ctx.channel.set_permissions(member, send_messages=False, view_channel=True)
        embed = discord.Embed(title=f"*{member} was muted!*", description=f"{member.mention} was muted. ", colour=discord.Colour.red())
        await ctx.send(embed = embed)

    # Unmute users in raid channel.
    @commands.command(name = 'unmute', pass_context = True)
    async def unmute(self, ctx, member: discord.Member):
        await ctx.channel.set_permissions(member, send_messages=True, view_channel=True)
        embed = discord.Embed(title=f"*{member} was unmuted!*", description=f"{member.mention} was unmuted. ", colour=discord.Colour.green())
        await ctx.send(embed = embed)

    # Bans users in raid channel.
    @commands.command(name = 'ban', pass_context = True)
    async def ban(self, ctx, member: discord.Member):
        await ctx.channel.set_permissions(member, send_messages=False, view_channel=False)
        embed = discord.Embed(title=f"*{member} was banned!*", description=f"{member.mention} was banned. ", colour=discord.Colour.red())
        await ctx.send(embed = embed)

    # Bans users in raid channel.
    @commands.command(name = 'unban', pass_context = True)
    async def unban(self, ctx, member: discord.Member):
        await ctx.channel.set_permissions(member, send_messages=True, view_channel=True)
        embed = discord.Embed(title=f"*{member} was unbanned!*", description=f"{member.mention} was unbanned. ", colour=discord.Colour.green())
        await ctx.send(embed = embed)

    # Delete raid channel and all of its messages.
    @commands.command(name = 'delete', pass_context = True)
    async def delete(self, ctx):
        channelName = ctx.message.channel
        embed = discord.Embed(title=f"*{channelName} was deleted!*", description=f"{channelName} was deleted. ", colour=discord.Colour.gold())
        await ctx.author.send(embed = embed)
        await channelName.delete()

def setup(client):
    client.add_cog(RaidHost(client))