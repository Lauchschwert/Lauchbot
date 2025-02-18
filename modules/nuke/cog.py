
from discord.ext import commands
import discord
from discord.ext.tasks import loop

import datetime


class Nuke(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='nuke')
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    async def nuke(self, ctx, channel: discord.TextChannel = None):

        bot_member = ctx.guild.get_member(self.bot.user.id)
        if not bot_member.guild_permissions.manage_channels:
            return await ctx.reply("I do not have the permission to manage channels.", ephemeral=True)
            
        
        if not ctx.author.guild_permissions.manage_channels:
            embed = discord.Embed(
                title="Permission Error",
                description=f"{interaction.user.mention}, you don't have enough permissions to use this command.",
                color=discord.Color.red()
            ).set_footer(
                text=f"Requested by {interaction.user.name}",
                icon_url=interaction.user.avatar
            )
            return await ctx.reply(embed=embed, ephemeral=True)
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
            await ctx.reply(f"No channel named {channel.name} was found!", ephemeral=True)



async def setup(bot):
    await bot.add_cog(Nuke(bot))
