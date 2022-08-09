from discord.ext import commands
import discord
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option
from discord.ext.tasks import loop
import pip._vendor.requests
from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions
import datetime


class ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ban')
    @has_permissions(manage_roles=True, ban_members=True)
    async def ban(self, ctx: SlashContext, user: discord.Member, *, reason="None"):
        try:

            if user == ctx.author:
                await ctx.reply("You cannot ban yourself")
                return

            if reason == None:
                reason = "none"
            await user.ban(reason=reason)
            embed = discord.Embed(
            title="💥 User has been banned!", color=0x00d9ff)
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            embed.add_field(name="User:", value=user.mention, inline=True)
            embed.add_field(name="Banned by: ",
            value=ctx.author.mention, inline=True)
            embed.add_field(name="Reason: ", value=reason, inline=True)
            await ctx.send(embed=embed)
            try:
                await user.send(f"You have been banned from {ctx.guild.name} Reason: " + reason)
            except Exception as e:
                print(e)
        except Exception as e:
            embed = discord.Embed(title=":x: Command Error",
            colour=0x992D22)  # Dark Red
            embed.add_field(name="Error", value=e)
            embed.add_field(name="Guild", value=ctx.guild)
            embed.add_field(name="Channel", value=ctx.channel)
            embed.add_field(name="User", value=ctx.author)
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.reply(embed=embed)


def setup(bot):
    bot.add_cog(ban(bot))
