from discord.ext import commands
from discord.ext.tasks import loop
import requests
import discord
import datetime


class factde(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='factde')
    async def factde(self, interaction: discord.Interaction):
        try:
            url = "https://uselessfacts.jsph.pl/random.json?language=de"
            response = requests.get(url)
            value = response.json()["text"]
            await interaction.send("Hier ist eine zufälliger und nutzloser Fakt: " + value)
        except Exception as e:
            embed = discord.Embed(title=":x: Command Error",
            colour=0x992D22)  # Dark Red
            embed.add_field(name="Error", value=e)
            embed.add_field(name="Guild", value=interaction.guild)
            embed.add_field(name="Channel", value=interaction.channel)
            embed.add_field(name="User", value=interaction.author)
            embed.timestamp = datetime.datetime.utcnow()
            await interaction.reply(embed=embed)

async def setup(bot):
    await bot.add_cog(factde(bot))
