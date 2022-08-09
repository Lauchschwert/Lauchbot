from discord.ext import commands
import discord
import discord_slash
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option
from discord.ext.tasks import loop
from discord_slash import cog_ext
import datetime
import asyncio
import urllib
import pip._vendor.requests


class userinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
        

    @commands.command(name='userinfo')
    async def userinfo(self, ctx, user: discord.Member):
        try:
            embed = discord.Embed(title=f"{user.name}'s Info", color=0x00ff00)
            embed.add_field(name="Name", value=user.name, inline=True)
            embed.add_field(name="ID", value=user.id, inline=True)
            embed.add_field(name="Highest role", value=user.top_role)
            embed.add_field(name="Joined At", value=user.joined_at.strftime("%A, %B %d %Y @ %H:%M:%S %p"))
            embed.set_thumbnail(url=user.avatar_url)


            await ctx.reply(embed=embed, mention_author=False)
        
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
    bot.add_cog(userinfo(bot))
