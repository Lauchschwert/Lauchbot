from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option
from discord.ext.tasks import loop
from discord_slash import cog_ext
import datetime
import asyncio
import urllib
import requests



class bitcoin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        

    @commands.command(name='bitcoin')
    async def bitcoin(self, ctx):
        url = "https://api.coindesk.com/v1/bpi/currentprice/BTC.json"
        response = requests.get(url)
        value = response.json()["bpi"]["USD"]["rate"]
        await ctx.send("Current Bitcoin Price is: $" + value)

        
def setup(bot):
    bot.add_cog(bitcoin(bot))
