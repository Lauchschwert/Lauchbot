from discord.ext import commands
import discord
import discord_slash
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option
from discord.ext.tasks import loop
from discord_slash import cog_ext
import datetime


class website(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='website')
    @commands.guild_only()
    async def website(self, ctx):
        await ctx.send("My Website => https://www.lauchschwert.xyz")
        await ctx.send("Anditv's Website => https://gamekiller.at")


def setup(bot):
    bot.add_cog(website(bot))
