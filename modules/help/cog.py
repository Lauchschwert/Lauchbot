import asyncio
from multiprocessing.connection import wait
from discord.ext import commands
import discord
from discord.ext.tasks import loop
import datetime


class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='help')
    @commands.guild_only()
    async def help(self, interaction: discord.Interaction):
        embed = discord.Embed(
            description="Here are the commands!", color=0x00efdb)
        embed.set_image(url="https://i.imgur.com/vMp7vWq.png")
        await interaction.response.send_message(embed=embed, ephemeral=True)
        await asyncio.sleep(1000)

def setup(bot):
    bot.add_cog(help(bot))
