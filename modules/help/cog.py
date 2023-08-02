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
    async def help(self, ctx):
        try:
            embed = discord.Embed(
                description="Here are the commands!", color=0x00efdb)
            embed.set_image(url="https://i.imgur.com/vMp7vWq.png")
            await ctx.reply(embed=embed, mention_author=True)
            await asyncio.sleep(1000)
        except Exception as e:
            embed = discord.Embed(title=":x: Command Error",
            colour=0x992D22)  # Dark Red
            embed.add_field(name="Error", value=e)
            embed.add_field(name="Guild", value=ctx.guild)
            embed.add_field(name="Channel", value=ctx.channel)
            embed.add_field(name="User", value=ctx.author)
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.reply(embed=embed)

def setup(bot):
    bot.add_cog(help(bot))
