from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option
from discord.ext.tasks import loop
from discord_slash import cog_ext
import datetime
import asyncio
import urllib



class reverse(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        

    @commands.command(name='reverse')
    async def reverse(self, ctx, text):
        await ctx.send(text[::-1])

        
        
        
         




def setup(bot):
    bot.add_cog(reverse(bot))
