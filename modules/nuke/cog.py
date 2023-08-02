
from discord.ext import commands
import discord
from discord.ext.tasks import loop

import datetime


class nuke(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='nuke')
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    async def Nuke(self, interaction: discord.Interaction, channel: discord.TextChannel = None):
        if channel == None:
            channel = interaction.channel
        nuke_channel = discord.utils.get(
            interaction.guild.channels, name=channel.name)

        if nuke_channel is not None:
            new_channel = await nuke_channel.clone(reason="Has been Nuked!")
            await nuke_channel.delete()
            await new_channel.send("THIS CHANNEL HAS BEEN NUKED!")
            await new_channel.send("https://tenor.com/view/xqc-spotify-mood-want-a-break-bruh-gif-24599734")

        else:
            await interaction.response.send_message(f"No channel named {channel.name} was found!", ephemeral=True)



def setup(bot):
    bot.add_cog(nuke(bot))
