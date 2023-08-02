from discord.ext import commands
import discord
from discord.ext.tasks import loop
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
        try:
            if "https://youtu.be/" in url:
                url.replace("https://youtu.be/",
                            "https://www.youtube.com/watch?v=")

            vgm_url = 'https://8downloader.com/download?v=' + url
            html_text = pip._vendor.requests.get(vgm_url).text
            soup = BeautifulSoup(html_text, 'html.parser')
            download = soup.find('a', href=True, text='Download')['href']

            link = "http://tinyurl.com/api-create.php?url=" + str(download)
            from urllib.request import urlopen
            with urlopen(link) as webpage:
                f = webpage.read().decode()
                
            embed=discord.Embed(title="Click here to download your Video", url=f, color=0xff0000)
            embed.set_author(name="Your download link is ready")
            await ctx.reply(embed=embed)
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
    bot.add_cog(download(bot))
