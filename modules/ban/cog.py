import discord
from discord import app_commands
from discord.ext import commands

class ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="ban", description="Ban someone")
    @discord.app_commands.describe(member="The member you want to ban")
    @discord.app_commands.describe(reason="Why do you want to ban this member?")
    async def ban(self, interaction: discord.Interaction, user: discord.Member, *, reason: str = None):
            if user == interaction.author:
                await interaction.reply("You cannot ban yourself")
                return

            if reason == None:
                reason = "none"
            await user.ban(reason=reason)
            embed = discord.Embed(
            title="💥 User has been banned!", color=0x00d9ff)
            embed.set_author(name=interaction.author, icon_url=interaction.author.avatar_url)
            embed.add_field(name="User:", value=user.mention, inline=True)
            embed.add_field(name="Banned by: ",
            value=interaction.author.mention, inline=True)
            embed.add_field(name="Reason: ", value=reason, inline=True)
            await interaction.send(embed=embed)
            try:
                await user.send(f"You have been banned from {interaction.guild.name} Reason: " + reason)
            except Exception as e:
                print(e)

def setup(bot):
    bot.add_cog(ban(bot))
