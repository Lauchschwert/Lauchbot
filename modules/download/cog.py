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


class download(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        

    @commands.command(name='download')
    async def download(self, ctx, url):
        vgm_url = 'https://8downloader.com/download?v=' + url
        html_text = pip._vendor.requests.get(vgm_url).text
        soup = BeautifulSoup(html_text, 'html.parser')
        download = soup.find('a', href=True, text='Download')['href']
        print(str(download))

        link = "http://tinyurl.com/api-create.php?url=" + str(download)
        from urllib.request import urlopen
        with urlopen(link) as webpage:
            f = webpage.read().decode()
        await ctx.send(f"Download Link to your Youtube Video (limited time only): {f}")
        
        
        
         




def setup(bot):
    bot.add_cog(download(bot))
