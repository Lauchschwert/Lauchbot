from discord.ext import commands
from discord.ext.tasks import loop
import requests
import discord
import datetime


class fact(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='fact')
    async def fact(self, interaction: discord.Interaction):
        url = "https://uselessfacts.jsph.pl/random.json?language=en"
        response = requests.get(url)
        value = response.json()["text"]
        await interaction.response.send_message("Here is a random and useless fact: " + value)


async def setup(bot):
    await bot.add_cog(fact(bot))
