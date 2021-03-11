import discord
from discord.ext import commands
import discord.utils
from discord.utils import get
import json
from dotenv import load_dotenv
import os
import re

# Cog for the Raid Host Private Room feature.
class RaidHost(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Raid Host Commands Loaded.')

    @commands.command(name = 'host', aliases=['raid'], pass_context = True, invoke_without_command = True)
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
        
        # Prompt for Den Name.
        embedOverview = discord.Embed(title=f"Den Overview", description=f"What den are you hosting? Ex: Den 69", colour=discord.Colour.red())
        sendOverview = await hostChannel.send(embed = embedOverview)

        def check(m):
            msgInHostChannel = m.channel == hostChannel
            print("Check true or false? ", msgInHostChannel)
            return msgInHostChannel
        msgOverview = await self.client.wait_for('message', check = check)

        # Confirm if the user has desired input.
        embedConfirm = discord.Embed(title=f"Are you Sure [Y/N]?", description=f"Please type Y/N.", colour=discord.Colour.red())
        await hostChannel.send(embed = embedConfirm)

        def check_yn(m):
            is_yn = m.content.upper() in ('Y', 'N')
            print("is yn? ", is_yn)
            return is_yn
        msgConfirm = await self.client.wait_for('message', check = check_yn)
        
        # Keep prompting for den name until they get it right.
        while(msgConfirm.content != 'Y'):
            await hostChannel.send(embed = embedOverview)
            await self.client.wait_for('message', check = check)
            await hostChannel.send(embed = embedConfirm)
            msgConfirm = await self.client.wait_for('message', check = check_yn)

        # Prompt for nature
        embedNature = discord.Embed(title=f"What is the Nature of your Den?", description=f"Type the nature of your den.", colour=discord.Colour.orange())
        await hostChannel.send(embed = embedNature)
        msgNature = await self.client.wait_for('message', check = check)
        await hostChannel.send(embed = embedConfirm)
        msgConfirm = await self.client.wait_for('message', check = check_yn)

        # Keep prompting for nature until they get it right.
        while(msgConfirm.content != 'Y'):
            await hostChannel.send(embed = embedNature)
            await self.client.wait_for('message', check = check)
            await hostChannel.send(embed = embedConfirm)
            msgConfirm = await self.client.wait_for('message', check = check_yn)
        
        # Prompt for IVs: 3 Star 4 Star 5 Star
        embedIV = discord.Embed(title=f"What are the IVs of your Pokemon?", description=f"You can find your raid seed here: https://github.com/Admiral-Fish/RaidFinder", colour=discord.Colour.green())
        await hostChannel.send(embed = embedIV)
        msgIV = await self.client.wait_for('message', check = check)
        print("message content: ", msgIV.content)
        # Only accept input in the format XX/XX/XX/XX/XX/XX
        # where XX is 0-31.
        parsedIV = re.match("([0-2][0-9]|[3][0-1])/([0-2][0-9]|[3][0-1])/([0-2][0-9]|[3][0-1])/([0-2][0-9]|[3][0-1])/([0-2][0-9]|[3][0-1])/([0-2][0-9]|[3][0-1])", msgIV.content)

        embedIV = discord.Embed(title=f"BRUH", description=f"This ain't Cooly's server... PLEASE enter a value 0-31 in format XX/XX/XX/XX/XX/XX.", colour=discord.Colour.green())
        while(not parsedIV):
            await hostChannel.send(embed = embedIV)
            msg = await self.client.wait_for('message', check = check)
            parsedIV = re.match("([0-2][0-9]|[3][0-1])/([0-2][0-9]|[3][0-1])/([0-2][0-9]|[3][0-1])/([0-2][0-9]|[3][0-1])/([0-2][0-9]|[3][0-1])/([0-2][0-9]|[3][0-1])", msg.content)

        # Prompt for Gender
        embedGender = discord.Embed(title=f"What is the Gender of your Den?", description=f"Type the gender of your den.", colour=discord.Colour.blue())
        await hostChannel.send(embed = embedGender)
        msgGender = await self.client.wait_for('message', check = check)
        await hostChannel.send(embed = embedConfirm)
        msgConfirm = await self.client.wait_for('message', check = check_yn)

        # Keep prompting for gender until they get it right.
        while(msgConfirm.content != 'Y'):
            await hostChannel.send(embed = embedGender)
            await self.client.wait_for('message', check = check)
            await hostChannel.send(embed = embedConfirm)
            msgConfirm = await self.client.wait_for('message', check = check_yn)

        # Prompt for Shiny Type
        embedRarity = discord.Embed(title=f"What is the Shiny Type of your Den?", description=f"Type the shiny type of your den (Square or Star).", colour=discord.Colour.purple())
        await hostChannel.send(embed = embedRarity)
        msgRarity = await self.client.wait_for('message', check = check)
        await hostChannel.send(embed = embedConfirm)
        msgConfirm = await self.client.wait_for('message', check = check_yn)

        # Keep prompting for shiny type until they get it right.
        while(msgConfirm.content != 'Y'):
            await hostChannel.send(embed = embedRarity)
            await self.client.wait_for('message', check = check)
            await hostChannel.send(embed = embedConfirm)
            msgConfirm = await self.client.wait_for('message', check = check_yn)
        # Prompt for Rules (limit 200 characters)
        embedRules = discord.Embed(title=f"Write your Ruleset", description=f"Keep it within 200 characters.", colour=discord.Colour.dark_purple())
        await hostChannel.send(embed = embedRules)
        msgRules = await self.client.wait_for('message', check = check) 
        msgRules
        embedRulesResult = discord.Embed(title=f"Results", description= msgRules.content, colour=discord.Colour.dark_purple())   
        await hostChannel.send(embed = embedRulesResult)
        await hostChannel.send(embed = embedConfirm)
        msgConfirm = await self.client.wait_for('message', check = check_yn)
        
        # Keep prompting for rules until they get it right.
        while(msgConfirm.content != 'Y'):
            await hostChannel.send(embed = embedRules)
            await self.client.wait_for('message', check = check)
            await hostChannel.send(embed = embedConfirm)
            msgConfirm = await self.client.wait_for('message', check = check_yn)

        # Send output of the results to the shiny raid channel.
        # Here, members can react to the embed in order to enter the room.
        shinyRaidsChannel = self.client.get_channel(819344708722884608)
        embedDisplay = discord.Embed(colour = discord.Colour.blue())

        # Display output of results in shiny-raids.
        member = message.author
        embedDisplay.set_author(name=f"{member}'s Raid", icon_url='https://cdn.discordapp.com/attachments/817278897862213642/818012928162398228/darkmimi.jpg')
        embedDisplay.set_thumbnail(url='https://cdn.discordapp.com/attachments/817278897862213642/818012928162398228/darkmimi.jpg')
        embedDisplay.add_field(name='Den', value= msgOverview.content, inline=False)
        embedDisplay.add_field(name='Nature', value= msgNature.content, inline=False)
        embedDisplay.add_field(name='IVs', value= msgIV.content, inline=False)
        embedDisplay.add_field(name='Gender', value= msgGender.content, inline=False)
        embedDisplay.add_field(name='Shiny Type', value= msgRarity.content, inline=False)
        embedDisplay.add_field(name='Rules', value= msgRules.content, inline=False)

        await shinyRaidsChannel.send(embed = embedDisplay);
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
            await ctx.send("Sorry, only users with 🌟Raid Host🌟 role are allowed to use this command.")
    
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

    # Unbans users in raid channel.
    @commands.command(name = 'unban', pass_context = True)
    async def unban(self, ctx, member: discord.Member):
        await ctx.channel.set_permissions(member, send_messages=True, view_channel=True)
        embed = discord.Embed(title=f"*{member} was unbanned!*", description=f"{member.mention} was unbanned. ", colour=discord.Colour.green())
        await ctx.send(embed = embed)

    # Delete raid channel and all of its messages.
    @commands.command(name = 'delete', pass_context = True, aliases=['d', 'del'])
    async def delete(self, ctx):
        channelName = ctx.message.channel
        embed = discord.Embed(title=f"*{channelName} was deleted!*", description=f"{channelName} was deleted. ", colour=discord.Colour.gold())
        await ctx.author.send(embed = embed)
        await channelName.delete()

def setup(client):
    client.add_cog(RaidHost(client))