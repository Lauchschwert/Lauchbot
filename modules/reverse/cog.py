from discord.ext import commands
from discord.ext.tasks import loop
import datetime
import asyncio
import urllib
import discord
import datetime


class reverse(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='reverse')
    async def reverse(self, ctx, text):
        try:
            await ctx.send(text[::-1])
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
    bot.add_cog(reverse(bot))
