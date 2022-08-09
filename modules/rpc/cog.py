from discord.ext import commands
import discord
from discord.ext.tasks import loop
from discord import guild
from discord.ext.commands import has_permissions
from discord.utils import get
from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions
import datetime



class rpc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        

    @commands.command(name='rpc')
    @commands.guild_only()
    @has_permissions(administrator=True)
    async def rpc(self, ctx, activity, name):
        try:
            if activity == 'p' or activity == 'P':
                game = discord.Game(name)
                await self.bot.change_presence(activity=game)
                await self.bot.change_presence(status=discord.Status.dnd)
                await ctx.reply("Updated Discord RPC to playing " + name, mention_author=False)
            if activity == 'l' or activity == 'L':
                await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=name))
                await self.bot.change_presence(status=discord.Status.dnd)
                await ctx.reply("Updated Discord RPC to listening to " + name, mention_author=False)
            if activity == 'w' or activity == 'W':
                await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=name))
                await self.bot.change_presence(status=discord.Status.dnd)
                await ctx.reply("Updated Discord RPC to watching " + name, mention_author=False)


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
    bot.add_cog(rpc(bot))