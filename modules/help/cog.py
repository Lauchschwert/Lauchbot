import asyncio
from multiprocessing.connection import wait
from discord.ext import commands
import discord
import discord_slash
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option
from discord.ext.tasks import loop
from discord_slash import cog_ext
import datetime


class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='help')
    @commands.guild_only()
    async def help(self, ctx):
        embed = discord.Embed(
            description="Here are the commands!", color=0x00efdb)
        embed.set_image(url="https://i.imgur.com/vMp7vWq.png")
        await ctx.reply(embed=embed, mention_author=True)
        await asyncio.sleep(1000)


def setup(bot):
    bot.add_cog(help(bot))
