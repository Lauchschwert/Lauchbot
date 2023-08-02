from discord.ext import commands
import discord
from discord.ext.tasks import loop
import datetime


class github(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='github')
    @commands.guild_only()
    async def github(self, interaction: discord.Member):
        await interaction.send("https://www.github.com/Lauchschwert")
        await interaction.send("https://www.github.com/anditv21")


def setup(bot):
    bot.add_cog(github(bot))
