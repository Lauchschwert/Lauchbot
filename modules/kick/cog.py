from discord.ext import commands
import discord
from discord.ext.tasks import loop
import datetime
from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions


class kick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='kick')
    async def kick(self, interaction: discord.Interaction, member: discord.User = None, reason=None):
        if not interaction.guild.me.guild_permissions.kick_members:
            raise discord.Forbidden("I do not have the permission to kick members.")

        if not interaction.user.guild_permissions.kick_members:
            raise discord.Forbidden("You do not have the permission to kick members.")
            
        if member == None or member == interaction.message.author:
            await interaction.channel.send("You cannot kick yourself")
            return
        if reason == None:
            reason = "no reason provided"
        message = f"You have been kicked from {interaction.guild.name} for {reason}"
        await member.send(message)
        await interaction.guild.kick(member)
        await interaction.response.send_message(f"{member} has been kicked!")

async def setup(bot):
    await bot.add_cog(kick(bot))
