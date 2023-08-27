from discord.ext import commands
import discord
from discord.ext.tasks import loop
import datetime


class twitch(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='twitch')
    @commands.guild_only()
    async def twitch(self, interaction: discord.Interaction):
            await interaction.response.send_message("https://www.twitch.tv/Lauchschwert")

async def setup(bot):
    await bot.add_cog(twitch(bot))
