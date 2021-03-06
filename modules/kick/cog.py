from discord.ext import commands
import discord
import discord_slash
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option
from discord.ext.tasks import loop
from discord_slash import cog_ext
import datetime
from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions


class kick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='kick')
    @has_permissions(manage_roles=True, kick_members=True)
    async def kick(self, ctx, member: discord.User = None, reason=None):
        if member == None or member == ctx.message.author:
            await ctx.channel.send("You cannot kick yourself")
            return
        if reason == None:
            reason = "no reason provided"
        message = f"You have been kicked from {ctx.guild.name} for {reason}"
        await member.send(message)
        await ctx.guild.kick(member)
        await ctx.channel.send(f"{member} has been kicked!")


def setup(bot):
    bot.add_cog(kick(bot))
