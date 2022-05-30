from discord.ext import commands
import discord
import discord_slash
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option
from discord.ext.tasks import loop
from discord_slash import cog_ext
import datetime


class github(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        

    @commands.command(name='github')
    @commands.guild_only()
    async def github(self, ctx: discord.Member):
            await ctx.send("https://www.github.com/Lauchschwert")
            await ctx.send("https://www.github.com/anditv21")




def setup(bot):
    bot.add_cog(github(bot))


         