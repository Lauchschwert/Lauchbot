from discord.ext import commands
from discord.ext.tasks import loop
import datetime
import asyncio
import urllib
import requests
import discord


class bitcoin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='bitcoin')
    async def bitcoin(self, ctx):
        try:
            url = "https://api.coindesk.com/v1/bpi/currentprice/BTC.json"
            response = requests.get(url)
            value = response.json()["bpi"]["USD"]["rate"]
            await ctx.send("Current Bitcoin Price is: $" + value)
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
    bot.add_cog(bitcoin(bot))
