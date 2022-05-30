from discord.ext import commands
import discord
import discord_slash
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option
from discord.ext.tasks import loop
from discord_slash import cog_ext
import datetime


class avatar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        

    @commands.command(name='avatar')
    @commands.guild_only()
    async def avatar(self, ctx, member: discord.Member):
            embed = discord.Embed(description="Here is the avatar", color=0x00efdb)
            embed.set_image(url=member.avatar_url)
            await ctx.reply(embed=embed, mention_author=False)




def setup(bot):
    bot.add_cog(avatar(bot))