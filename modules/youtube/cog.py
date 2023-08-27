from discord.ext import commands
import discord
import datetime


class youtube(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='youtube')
    @commands.guild_only()
    async def youtube(self, interaction: discord.Interaction):
        await interaction.response.send_message("https://www.youtube.com/channel/UCn71e_JrhNVYbvETHl4MNJw")

async def setup(bot):
    await bot.add_cog(youtube(bot))
