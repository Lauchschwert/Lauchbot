from discord.ext import commands
import discord
from discord.ext.tasks import loop
import datetime
import asyncio
from bs4 import BeautifulSoup
import urllib
import pip._vendor.requests


class short(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='short')
    async def short(self, ctx, url):
        try:
            link = "http://tinyurl.com/api-create.php?url=" + str(url)
            from urllib.request import urlopen
            with urlopen(link) as webpage:
                f = webpage.read().decode()
            await ctx.send(f"Your short-link is: {f}")
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
    bot.add_cog(short(bot))
