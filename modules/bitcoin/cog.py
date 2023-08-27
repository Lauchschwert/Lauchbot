import discord
from discord import app_commands
from discord.ext import commands
import requests


class bitcoin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='bitcoin')
    async def bitcoin(self, interaction: discord.Interaction):
        url = "https://api.coindesk.com/v1/bpi/currentprice/BTC.json"
        response = requests.get(url)
        value = response.json()["bpi"]["USD"]["rate"]
        await interaction.response.send_message("Current Bitcoin Price is: $" + value)


async def setup(bot):
    await bot.add_cog(bitcoin(bot))
