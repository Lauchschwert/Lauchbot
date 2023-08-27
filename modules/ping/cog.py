from discord.ext import commands
from discord.ext.tasks import loop
import datetime
import asyncio
import urllib
import discord
import datetime


class ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ping')
    async def ping(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"Pong! In {round(self.bot.latency * 1000)}ms")



async def setup(bot):
    await bot.add_cog(ping(bot))
