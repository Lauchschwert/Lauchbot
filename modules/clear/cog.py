import discord
from discord import app_commands
from discord.ext import commands
import requests
import asyncio


class clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='clear')
    @commands.guild_only()
    async def clear(self, interaction: discord.Interaction, limit: int):
        try:
            await interaction.send("Deleted " + str(limit) + "(maximum) messages")
            asyncio.sleep(3000)
            await interaction.channel.purge(limit=limit+2)
        except Exception as e:
            embed = discord.Embed(title=":x: Command Error",
            colour=0x992D22)  # Dark Red
            embed.add_field(name="Error", value=e)
            embed.add_field(name="Guild", value=interaction.guild)
            embed.add_field(name="Channel", value=interaction.channel)
            embed.add_field(name="User", value=interaction.author)
            await interaction.response.send_message(embed=embed)         


async def setup(bot):
    await bot.add_cog(clear(bot))
