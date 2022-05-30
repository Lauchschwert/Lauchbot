from discord.ext import commands
import discord
import discord_slash
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option
from discord.ext.tasks import loop
from discord_slash import cog_ext
import datetime
import asyncio


class clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        

    @commands.command(name='clear')
    @commands.guild_only()
    async def clear(self, ctx, limit: int):
        await ctx.send("Deleted " + str(limit) + "(maximum) messages")
        asyncio.sleep(3000)
        await ctx.channel.purge(limit=limit+2)




def setup(bot):
    bot.add_cog(clear(bot))