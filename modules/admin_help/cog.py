import asyncio
from multiprocessing.connection import wait
from discord.ext import commands
import discord
from discord.ext.tasks import loop
from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions
import datetime


class admin_help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='admin_help')
    @commands.guild_only()
    @has_permissions(administrator=True)
    async def admin_help(self, ctx):
        try:
            embed = discord.Embed(
                description="Here are the commands!", color=0x00efdb)
            embed.set_image(url="https://i.imgur.com/ZnZmLfc.png")
            await ctx.reply(embed=embed, mention_author=True)
            await asyncio.sleep(1000)
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
    bot.add_cog(admin_help(bot))
