from discord.ext import commands
import discord
import discord_slash
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option
from discord.ext.tasks import loop
from discord_slash import cog_ext
import datetime


class youtube(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='youtube')
    @commands.guild_only()
    async def youtube(self, ctx: discord.Member):
        try:
            await ctx.send("https://www.youtube.com/channel/UCn71e_JrhNVYbvETHl4MNJw")
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
    bot.add_cog(youtube(bot))
