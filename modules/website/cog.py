from discord.ext import commands
import discord
import datetime


class website(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='website')
    @commands.guild_only()
    async def website(self, interaction: discord.Interaction):
        await interaction.response.send_message("My Website => https://www.lauchschwert.xyz")

def setup(bot):
    bot.add_cog(website(bot))
