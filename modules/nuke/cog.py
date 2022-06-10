from discord.ext import commands
import discord
import discord_slash
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option
from discord.ext.tasks import loop
from discord_slash import cog_ext
import datetime


class nuke(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='nuke')
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    async def Nuke(self, ctx: SlashContext, channel: discord.TextChannel = None):
        try:
            if channel == None:
                channel = ctx.channel
            nuke_channel = discord.utils.get(
                ctx.guild.channels, name=channel.name)

            if nuke_channel is not None:
                new_channel = await nuke_channel.clone(reason="Has been Nuked!")
                await nuke_channel.delete()
                await new_channel.send("THIS CHANNEL HAS BEEN NUKED!")
                await new_channel.send("https://tenor.com/view/xqc-spotify-mood-want-a-break-bruh-gif-24599734")

            else:
                await ctx.send(f"No channel named {channel.name} was found!")
        except Exception as e:
            await ctx.reply(e)


def setup(bot):
    bot.add_cog(nuke(bot))
