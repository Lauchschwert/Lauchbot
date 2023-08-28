import discord
from discord.ext import commands

class bot_download(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

@commands.command(name='download')
async def download(self, ctx):
    view = download()
    view.add_item(discord.ui.Button(label="Direct Download", style=discord.ButtonStyle.link, url="https://github.com/Lauchschwert/Lauchbot/archive/refs/heads/main.zip", emoji="<a:X_Freddy:879860891397521448>"))

async def setup(bot):
    await bot.add_cog(bot_download(bot))