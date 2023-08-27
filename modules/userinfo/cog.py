from discord.ext import commands
import discord
from discord.ext.tasks import loop
import datetime
import asyncio
import urllib
import pip._vendor.requests


class userinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
        

    @commands.command(name='userinfo')
    async def userinfo(self, interaction: discord.Interaction, user: discord.Member):
        embed = discord.Embed(title=f"{user.name}'s Info", color=0x00ff00)
        embed.add_field(name="Name", value=user.name, inline=True)
        embed.add_field(name="ID", value=user.id, inline=True)
        embed.add_field(name="Highest role", value=user.top_role)
        embed.add_field(name="Joined At", value=user.joined_at.strftime("%A, %B %d %Y @ %H:%M:%S %p"))
        embed.add_field(name="Account created on", value=user.created_at.strftime("&A, %B &d %Y @ %H:%M:&S %p"))
        embed.set_thumbnail(url=user.avatar_url)


        await interaction.response.send_message(embed=embed, mention_author=False)
    





async def setup(bot):
    await bot.add_cog(userinfo(bot))
