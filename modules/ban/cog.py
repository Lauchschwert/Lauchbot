from discord.ext import commands
import discord
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option
from discord.ext.tasks import loop
import pip._vendor.requests
from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions


class ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ban')
    @has_permissions(manage_roles=True, ban_members=True)
    async def ban(self, ctx, member: discord.User = None, reason=None):
        if member == None or member == ctx.message.author:
            await ctx.channel.send("You cannot ban yourself")
            return
        if reason == None:
            reason = "no reason provided"
        message = f"You have been banned from {ctx.guild.name} for {reason}"
        await member.send(message)
        await ctx.guild.ban(member, reason=reason)
        await ctx.channel.send("Ban 🔨 has spoken")
        await ctx.channel.send(f"{member} is now banned!")


def setup(bot):
    bot.add_cog(ban(bot))
