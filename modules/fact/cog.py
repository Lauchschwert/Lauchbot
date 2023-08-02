from discord.ext import commands
from discord.ext.tasks import loop
import requests
import discord
import datetime


class fact(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='fact')
    async def fact(self, ctx):
        try:
            url = "https://uselessfacts.jsph.pl/random.json?language=en"
            response = requests.get(url)
            value = response.json()["text"]
            await ctx.send("Here is a random and useless fact: " + value)
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
    bot.add_cog(fact(bot))
