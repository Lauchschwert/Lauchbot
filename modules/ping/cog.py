from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option
from discord.ext.tasks import loop
from discord_slash import cog_ext
import datetime
import asyncio
import urllib



class ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        

    @commands.command(name='ping')
    async def ping(self, ctx):
        await ctx.send(f"Pong! In {round(self.bot.latency * 1000)}ms")

        
def setup(bot):
    bot.add_cog(ping(bot))
