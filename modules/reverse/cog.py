from discord.ext import commands
from discord.ext.tasks import loop
import datetime
import asyncio
import urllib
import discord
import datetime


class reverse(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='reverse')
    async def reverse(self, interaction: discord.Interaction, text):
        await interaction.response.send_message(text[::-1])

async def setup(bot):
   await bot.add_cog(reverse(bot))
