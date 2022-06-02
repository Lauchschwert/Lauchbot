from discord.ext import commands
import discord
from discord.ext.tasks import loop
from discord import guild
from discord.ext.commands import has_permissions
from discord.utils import get
from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions



class rpc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        

    @commands.command(name='rpc')
    @commands.guild_only()
    @has_permissions(administrator=True)
    async def rpc(self, ctx, activity, name):
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




def setup(bot):
    bot.add_cog(rpc(bot))