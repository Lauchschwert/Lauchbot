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
    async def short(self, interaction: discord.Interaction, url):
        link = "http://tinyurl.com/api-create.php?url=" + str(url)
        from urllib.request import urlopen
        with urlopen(link) as webpage:
            f = webpage.read().decode()
        await interaction.response.send_message(f"Your short-link is: {f}")


async def setup(bot):
    await bot.add_cog(short(bot))
