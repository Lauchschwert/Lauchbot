from discord.ext import commands
import discord
import discord_slash
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option
from discord.ext.tasks import loop
from discord_slash import cog_ext
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
        link = "http://tinyurl.com/api-create.php?url=" + str(url)
        from urllib.request import urlopen
        with urlopen(link) as webpage:
            f = webpage.read().decode()
        await ctx.send(f"Your short-link is: {f}")


def setup(bot):
    bot.add_cog(short(bot))
