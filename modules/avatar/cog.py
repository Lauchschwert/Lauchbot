import discord
from discord import app_commands
from discord.ext import commands

class Avatar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='avatar', description="Get admin commands help")
    async def avatar(self, interaction,):
        embed = discord.Embed(title=f"Test", color=0x00EFDB)
        embed.set_image(url=interaction.user.avatar)
        await interaction.context.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Avatar(bot))